class Main {
        public static void foo() {
            System.out.println(x);
            x = 4;
        }
        public static int x = 12;
    
        public static void main(String[] args) {
            int x = 24;
            foo();
            System.out.println(x);
            bar();
        }

        public static void bar() {
            System.out.println(x);
        }
    }