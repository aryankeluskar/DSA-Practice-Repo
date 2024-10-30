class Sets{
    int[] parent;
    int[] size;

    int find_set(int v) {
        if (v == parent[v])
            return v;
        return parent[v] = find_set(parent[v]);
    }

    void make_set(int v) {
        parent[v] = v;
        size[v] = 1;
    }

    void union_sets(int a, int b) {
        a = find_set(a);
        b = find_set(b);
        if (a != b) {
            if (size[a] < size[b]){
                // swap(a, b);
                int temp = a;
                a = b;
                b = temp;
            }

            parent[b] = a;
            size[a] += size[b];
        }
    }

    public static void main(String[] args) {
        // The state of a disjoint set data structure is given as follow.

        // A(1) = -3,

        // A(2) = 1,

        // A(3) = 1,

        // A(4) = 3,

        // A(5) = 1,

        // A(6) = 5,

        // A(7) = 5,

        // A(8) = 7,

        // A(9) = -3,

        // A(10) = 9, 

        // A(11) = 9,

        // A(12) = 11,

        // A(13) = 9,

        // A[14) = 13,

        // A(15) = 13,

        // A(16) = 15.

        // After union(4, 16), what is the value of A(1)?

        Sets dsu = new Sets();
        dsu.parent = new int[17];
        dsu.size = new int[17];

        for (int i = 1; i <= 16; i++)
            dsu.make_set(i);
        
        dsu.union_sets(4, 16);

        System.out.println(dsu.find_set(1));
    }
}