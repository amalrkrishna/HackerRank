import java.util.*;
import java.math.BigInteger;


public class Solution {
    
        public static Map<Integer, Integer> pFactors(int number) {
        int n = number;
        Map<Integer, Integer> factors = new HashMap<>(); 
        for (int i = 2; i <= n / i; i++) {
            while (n % i == 0) {
                factors.put(i, factors.containsKey(i) ? factors.get(i) + 1 : 1);
                n /= i;
            }
        }
        if (n > 1) {
            factors.put(n, factors.containsKey(n) ? factors.get(n) + 1 : 1);
        }
        return factors;
    }

    private static int findSMP(int p, Map<Integer, Integer> pFactors) {
        int s = p - 1;

        List<Integer> xs = new ArrayList<>();
        for (int f : pFactors.keySet()) {
            xs.add(s/f);
        }

        BigInteger pb = BigInteger.valueOf(p);

        for (int g = 2; g <= p - 1; g++) {
            BigInteger gb = BigInteger.valueOf(g);
            boolean isPR = true;

            for (int x : xs) {
                BigInteger val = gb.modPow(BigInteger.valueOf(x), pb);
                if (val.equals(BigInteger.ONE)) {
                    isPR = false;
                    break;
                }
            }

            if (isPR) {
                return g;
            }
        }

        return -1;
    }

    private static int findNPR(int p, Map<Integer, Integer> pFactors) {
        double res = 1;
        for (Map.Entry<Integer, Integer> entry : pFactors.entrySet()) {
            double pi = entry.getKey();
            double ki = entry.getValue();
            res *= (Math.pow(pi, ki) * (1 - (1/pi)));
        }

        return (int)res;
    }
    public static void main(String[] args) {
        final Scanner in = new Scanner(System.in);
        final int p = in.nextInt();
        final Map<Integer, Integer> pFactors = pFactors(p-1);
        final int npr = findNPR(p, pFactors);
        final int sPR = findSMP(p, pFactors);
        System.out.println(sPR + " " + npr);
    }
}
