import random
import string
import json
import os

def generate_random_location(length=3):
    """Generate a random location string"""
    return ''.join(random.choices(string.ascii_uppercase, k=length))

def generate_test_case(n, min_serial=1, max_serial=10**9):
    """Generate a single test case with n nodes"""
    # Generate unique serials
    serials = random.sample(range(min_serial, max_serial), n)
    
    # Create nodes data
    nodes = []
    for i in range(n):
        serial = serials[i]
        next_serial = serials[(i + 1) % n] if i < n - 1 else None
        location = generate_random_location()
        # 70% chance of having a random pointer
        random_serial = random.choice(serials) if random.random() < 0.7 else None
        nodes.append([serial, next_serial, location, random_serial])
    
    return nodes

def generate_test_cases():
    """Generate multiple test cases with varying sizes"""
    test_cases = []
    
    # Small test cases
    test_cases.extend([
        # Example 1 from problem description
        [[3, 7, "ABC", None], [7, 1, "DEF", None], [1, 2, "GHI", None], [2, None, "JKL", None]],
        # Example 2 from problem description
        [[65, 12, "XYZ", None], [12, 71, "LMN", None], [71, 38, "OPQ", None], 
         [38, 43, "RST", None], [43, None, "UVW", None]]
    ])
    
    # Generate random test cases of various sizes
    sizes = [5, 10, 20, 50, 100, 1000]
    for size in sizes:
        test_cases.append(generate_test_case(size))
    
    # Edge cases
    test_cases.extend([
        # Single node
        [[1, None, "ABC", None]],
        # Two nodes
        [[1, 2, "ABC", 2], [2, None, "DEF", 1]],
        # All nodes pointing to themselves as random
        [[1, 2, "ABC", 1], [2, 3, "DEF", 2], [3, None, "GHI", 3]]
    ])
    
    return test_cases

def write_test_cases(test_cases, output_dir="tests"):
    """Write test cases to files"""
    os.makedirs(output_dir, exist_ok=True)
    
    for i, test_case in enumerate(test_cases, 1):
        input_file = os.path.join(output_dir, f"input{i:02d}.txt")
        with open(input_file, "w") as f:
            f.write(f"{len(test_case)}\n")
            for node in test_case:
                # Convert None to "null" for output
                formatted_node = [str(x) if x is not None else "null" for x in node]
                f.write(" ".join(formatted_node) + "\n")

if __name__ == "__main__":
    test_cases = generate_test_cases()
    write_test_cases(test_cases) 