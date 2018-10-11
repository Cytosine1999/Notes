import java.io.IOException;
import java.io.PrintStream;
import java.util.Scanner;
import java.math.BigInteger;
import java.io.FileOutputStream;

public class Alkane_Enumeration {
    public static void main(String[] args) throws IOException {
        System.out.println(" ===== Alkane Enumeration ===== ");
        PrintStream alkane = new PrintStream(new FileOutputStream("Alkane.txt"));
        PrintStream alkyl = new PrintStream(new FileOutputStream("Alkyl.txt"));
        Scanner sc = new Scanner(System.in);
        PrintStream oos = System.out;
        System.out.println(">> 输入 1 计算烷基的同分异构体数目");
        System.out.println("   输入 2 计算烷烃的同分异构体数目");
        System.out.println("   输入3 结束程序");
        while (sc.hasNextInt()) {
            int flag = sc.nextInt();
            if (flag == 1) {
                System.out.println("  >> 输入1输出计算结果");
                System.out.println("     输入 2保存计算结果");
                int flag1 = sc.nextInt();
                if (flag1 == 1) {
                    System.out.println("        请输入需要计算的大小");
                    int sum = sc.nextInt();
                    if (sum > -1) {
                        long start = System.currentTimeMillis();
                        Alkyl.calculate(sum);
                        long end = System.currentTimeMillis();
                        System.out.println("        同分异构体的数目： " + Alkyl.cache[sum]);
                        System.out.println("        运行时间： " + (end - start) + " ms");
                    } else {
                        System.out.println("输入不合法");
                    }
                } else if (flag1 == 2) {
                    System.out.println("        请输入需要计算的大小");
                    int sum = sc.nextInt();
                    if (sum > -1) {
                        long start = System.currentTimeMillis();
                        Alkyl.calculate(sum);
                        long end = System.currentTimeMillis();
                        System.setOut(alkyl);
                        for (int n = 0; n <= sum; n++) {
                            System.out.println(n + " " + Alkyl.cache[n]);
                        }
                        System.setOut(oos);
                        System.out.println("        运行时间：" + (end - start) + " ms");
                    } else {
                        System.out.println("输入不合法");
                    }
                } else {
                    System.out.println("输入不合法");
                }
            } else if (flag == 2) {
                System.out.println("  >> 输入1输出计算结果");
                System.out.println("     输入 2保存计算结果");
                int flag1 = sc.nextInt();
                if (flag1 == 1) {
                    System.out.println("        请输入需要计算的大小");
                    int sum = sc.nextInt();
                    if (sum > -1) {
                        long start = System.currentTimeMillis();
                        Alkyl.calculate(sum);
                        BigInteger result = Alkane.calculate(sum);
                        long end = System.currentTimeMillis();
                        System.out.println("        同分异构体的数目：" + result);
                        System.out.println("        运行时间：" + (end - start) + " ms");
                    } else {
                        System.out.println("输入不合法");
                    }
                } else if (flag1 == 2) {
                    System.out.println("        请输入需要计算的初始值");
                    int sum1 = sc.nextInt();
                    System.out.println("        请输入需要计算的结束值");
                    int sum = sc.nextInt();
                    if (sum > -1) {
                        long start = System.currentTimeMillis();
                        Alkyl.calculate(sum);
                        BigInteger result;
                        System.setOut(alkane);
                        for (int n = sum1; n <= sum; n++) {
                            result = Alkane.calculate(n);
                            System.out.println(n + " " + result);
                        }
                        long end = System.currentTimeMillis();
                        System.setOut(oos);
                        System.out.println("        运行时间：" + (end - start) + " ms");
                    } else {
                        System.out.println("输入不合法");
                    }
                } else {
                    System.out.println("输入不合法");
                }
            } else if (flag == 3) {
                break;
            } else {
                System.out.println("输入不合法");
            }
            System.out.println();
            System.out.println(" ===== Alkane Enumeration ===== ");
            System.out.println(">> 输入 1 计算烷基的同分异构体数目");
            System.out.println("   输入 2 计算烷烃的同分异构体数目");
            System.out.println("   输入3 结束程序");
        }
        sc.close();
    }
}