import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.lang.Math;
import java.util.Scanner;

public class IntInputMatcher {
    public final int result;

    public IntInputMatcher(int start, int end, String prompt, String error) {
        System.out.println(prompt);
        Scanner sc = new Scanner(System.in);
        Pattern x = Pattern.compile("[^0-9]");
        int num;
        int sum;
        while (true) {
            String input = sc.next();
            Matcher match = x.matcher(input);
            if (match.find()) {
                System.out.println(error);
            } else {
                char[] m = input.toCharArray();
                sum = 0;
                int w = input.length();
                for (int n = 0; n < w; n++) {
                    num = m[w - n - 1] - 48;
                    sum += num * Math.pow(10, n);
                }
                if (start <= sum & sum <= end) {
                    result = sum;
                    break;
                }
            }
        }
    }
}