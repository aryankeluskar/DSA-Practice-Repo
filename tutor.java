public class tutor {
    public static int functionOne(int x, int y) {
             x = x * 2;
             y = y + x;

             return y;
     }

     public static int functionTwo(int x, int y) {
             return y - x;
     }

     public static String makeWords( ) {
             return "Final output is: ";
     }

     public static void main(String[] args) {

             String words = "?";

             int a = 0;
             int b = 4;
             int c = 2;

             a = functionOne(b, b);
             System.out.println(a);

             a = functionTwo(a, c);
             System.out.println(a);

             b = functionOne(b, a);
             words = makeWords( );
            //  words = words.concat(b);
            // words = words + b;

             System.out.println(words + b +b);

             System.out.println(b + b + words);

             double d = 3.14;
             float ab = 0.5f;

            System.out.println(d + ab);
     }
}
