import java.math.BigInteger;

public class Alkane {
    private static int[] element = new int[4];

    public static BigInteger calculate(int x) {
        BigInteger sum = BigInteger.ZERO;
        element[0] = 0;
        element[1] = 0;
        element[2] = 0;
        element[3] = x - 1;
        while (element[2] <= element[3]) {
            sum = sum.add(evaluation4());
            next4();
        }
        element[0] = 1;
        element[1] = x - 1;
        while (element[0] <= element[1]) {
            sum = sum.subtract(evaluation2());
            next2();
        }
        if (x % 2 == 0) {
            sum = sum.add(Alkyl.cache[x / 2]);
        }
        return sum;
    }

    private static void next4() {
        if (element[2] + 1 < element[3]) {
            element[2]++;
            element[3]--;
        } else if (2 * element[1] + 2 < element[2] + element[3]) {
            element[3] += element[2] - element[1] - 2;
            element[1]++;
            element[2] = element[1];
        } else {
            element[3] += element[1] + element[2] - 2 * element[0] - 3;
            element[0]++;
            element[1] = element[0];
            element[2] = element[1];
        }
    }

    private static BigInteger evaluation4() {
        if (element[0] == element[1] & element[1] == element[2] & element[2] == element[3]) {
            BigInteger result = Alkyl.cache[element[0]];
            BigInteger a = result.add(BigInteger.ONE);
            result = result.multiply(a);
            a = a.add(BigInteger.ONE);
            result = result.multiply(a);
            a = a.add(BigInteger.ONE);
            result = result.multiply(a);
            return result.divide(new BigInteger("24"));
        } else if (element[0] == element[1] & element[1] == element[2]) {
            BigInteger result = Alkyl.cache[element[0]];
            BigInteger a = result.add(BigInteger.ONE);
            result = result.multiply(a);
            a = a.add(BigInteger.ONE);
            result = (result.multiply(a)).divide(new BigInteger("6"));
            return result.multiply(Alkyl.cache[element[3]]);
        } else if (element[1] == element[2] & element[2] == element[3]) {
            BigInteger result = Alkyl.cache[element[1]];
            BigInteger a = result.add(BigInteger.ONE);
            result = result.multiply(a);
            a = a.add(BigInteger.ONE);
            result = (result.multiply(a)).divide(new BigInteger("6"));
            return result.multiply(Alkyl.cache[element[0]]);
        } else if (element[0] == element[1] & element[2] == element[3]) {
            BigInteger result = Alkyl.cache[element[0]];
            BigInteger a = result.multiply(result);
            result = (result.add(a)).divide(new BigInteger("2"));
            BigInteger b = Alkyl.cache[element[2]];
            a = b.multiply(b);
            b = (b.add(a)).divide(new BigInteger("2"));
            return result.multiply(b);
        } else if (element[0] == element[1]) {
            BigInteger result = Alkyl.cache[element[0]];
            BigInteger a = result.multiply(result);
            result = (result.add(a)).divide(new BigInteger("2"));
            return result.multiply(Alkyl.cache[element[2]].multiply(Alkyl.cache[element[3]]));
        } else if (element[1] == element[2]) {
            BigInteger result = Alkyl.cache[element[1]];
            BigInteger a = result.multiply(result);
            result = (result.add(a)).divide(new BigInteger("2"));
            return result.multiply(Alkyl.cache[element[0]].multiply(Alkyl.cache[element[3]]));
        } else if (element[2] == element[3]) {
            BigInteger result = Alkyl.cache[element[2]];
            BigInteger a = result.multiply(result);
            result = (result.add(a)).divide(new BigInteger("2"));
            return result.multiply(Alkyl.cache[element[0]].multiply(Alkyl.cache[element[1]]));
        } else {
            return Alkyl.cache[element[0]].multiply(Alkyl.cache[element[1]].multiply(Alkyl.cache[element[2]].multiply(Alkyl.cache[element[3]])));
        }
    }

    private static void next2() {
        element[0]++;
        element[1]--;
    }

    private static BigInteger evaluation2() {
        if (element[0] == element[1]) {
            BigInteger result = Alkyl.cache[element[0]];
            BigInteger a = result.multiply(result);
            return (result.add(a)).divide(new BigInteger("2"));
        } else {
            return Alkyl.cache[element[0]].multiply(Alkyl.cache[element[1]]);
        }
    }
}