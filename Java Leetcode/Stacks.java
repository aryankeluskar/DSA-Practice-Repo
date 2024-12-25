public class Stacks {
   private int stk[], cap, top;

   public Stacks(int size) {
      cap = size;
      top = -1;
      stk = new int[cap];
   }

   public void Push(int num) {
      if (top < cap - 1) {
         stk[++top] = num;
      } else {
         System.out.println("Overflow");
      }
   }

   public int Pop() {
      if (top >= 0) {
         return stk[top--];
      } else {
         System.out.println("Underflow");
         return -9999;
      }
   }

   public static void main(String[] args) {

      Stacks s = new Stacks(5);
      s.Push(10);
      s.Push(20);
      s.Push(30);
      s.Push(40);
      s.Push(50);
      s.Push(60);
      System.out.println(s.Pop());
      System.out.println(s.Pop());
   }
}