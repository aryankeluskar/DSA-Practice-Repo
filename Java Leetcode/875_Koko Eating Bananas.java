import java.util.*;

class Solution {

    public static void main(String[] args) {
        System.out.println(3 % 4 == 0);
    }

    public int minEatingSpeed(int[] piles, int h) {
        int minK = 1;
        int maxK = Arrays.stream(piles).max().orElse(0);

        if (piles.length == 1) {
            return piles[0] / h;
        }

        if (h == piles.length) {
            return maxK;
        }

        if (h > Arrays.stream(piles).sum()) {
            return 1;
        }

        return searchHelper(1, maxK, h, piles);
    }

    private int searchHelper(int low, int high, int h, int[] piles) {
        int mid = (low + high) / 2;
        int hours = hoursTaken(mid, piles);

        if (hours == h) {
            for (int i = low; i <= mid; i++) {
                if (hoursTaken(i, piles) == h) {
                    return i;
                }
            }
        }

        if (hours > h) {
            return searchHelper(mid + 1, high, h, piles);
        }

        if (hours < h) {
            return searchHelper(1, mid - 1, h, piles);
        }

        return -1; // or handle other cases based on your requirements
    }

    private int hoursTaken(int k, int[] piles) {
        int sumK = 0;
        for (int i : piles) {
            if (!(i % k == 0)) {
                sumK += 1;
            }
            sumK += (i / k);
        }

        return sumK;
    }
}
