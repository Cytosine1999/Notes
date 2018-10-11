import java.math.BigInteger;

public class Alkyl {
    public static BigInteger[] cache = new BigInteger[1];
    private static int[] element = new int[3];
    private static BigInteger sum = BigInteger.ZERO;

    static {
        cache[0] = BigInteger.ONE;
    }

    public static void calculate(int x) {
        if (x >= cache.length) {
            BigInteger[] cache2 = new BigInteger[x + 1];
            System.arraycopy(cache, 0, cache2, 0, cache.length);
            for (int n = cache.length; n <= x; n++) {
                element[0] = 0;
                element[1] = 0;
                element[2] = n - 1;
                while (element[1] <= element[2]) {
                    sum = sum.add(evaluation());
                    next();
                }
                cache2[n] = sum;
                sum = BigInteger.ZERO;
                cache = cache2;
            }
        }
    }

    private static void next() {
        if (element[1] + 1 < element[2]) {
            element[1]++;
            element[2]--;
        } else {
            element[2] += element[1] - element[0] - 2;
            element[0]++;
            element[1] = element[0];
        }
    }

    private static BigInteger evaluation() {
        if (element[0] == element[1] & element[1] == element[2]) {
            BigInteger result = cache[element[0]];
            BigInteger a = result.add(BigInteger.ONE);
            result = result.multiply(a);
            a = a.add(BigInteger.ONE);
            result = result.multiply(a);
            return result.divide(new BigInteger("6"));
        } else if (element[0] == element[1]) {
            BigInteger result = cache[element[0]];
            BigInteger a = result.multiply(result);
            result = (result.add(a)).divide(new BigInteger("2"));
            return result.multiply(cache[element[2]]);
        } else if (element[1] == element[2]) {
            BigInteger result = cache[element[1]];
            BigInteger a = result.multiply(result);
            result = (result.add(a)).divide(new BigInteger("2"));
            return result.multiply(cache[element[0]]);
        } else {
            return cache[element[0]].multiply(cache[element[1]].multiply(cache[element[2]]));
        }
    }
}