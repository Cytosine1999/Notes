import java.io.IOException;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import Board.IllegalMoveException;

public class Player {
    private boolean first;
    private String s;
    private boolean human;
    private boolean enemy;
    private AI ai;
    private Game game;
    private Scanner sc;

    public Player(Game c, boolean a, boolean b) throws IOException {
        first = a;
        human = b;
        game = c;
        if (human) {
            ai = null;
            sc = new Scanner(System.in);
        } else {
            ai = new AI(game, first);
            sc = null;
        }
        if (first) s = "O";
        else s = "X";
    }

    public boolean ifHuman() {
        return human;
    }

    public int move() throws AIIlleagalMoveExeption, IllegalMoveException {
        if (human) {
            while (true) {
                int a = -1;
                int b = -1;
                System.out.print("请玩家" + s + "输入下一手的位置：");
                String input = sc.next();
                Pattern x;
                Matcher matcher;
                if (input.equals("1")) game.unDo(enemy);
                else if (input.equals("2")) {
                    return 1;
                } else if (input.equals("3")) {
                    return 2;
                } else if (input.length() == 2) {
                    x = Pattern.compile("[0-7]");
                    matcher = x.matcher(input);
                    if (matcher.find()) a = matcher.group().toCharArray()[0] - 48;
                    x = Pattern.compile("[A-H]");
                    matcher = x.matcher(input);
                    if (matcher.find()) b = matcher.group().toCharArray()[0] - 65;
                    x = Pattern.compile("[a-h]");
                    matcher = x.matcher(input);
                    if (matcher.find()) b = matcher.group().toCharArray()[0] - 97;
                    if (a == -1 | b == -1) {
                        System.out.print("输入不合法 ");
                        continue;
                    }
                    if (game.move(a, b)) return 0;
                    else System.out.print("不合法的移动 ");
                } else System.out.print("输入不合法 ");
            }
        } else {
            int[] c = ai.move();
            System.out.println("玩家" + s + "下" + c[0] + (char) (c[1] + 65) + " ");
            if (game.move(c[0], c[1])) return 0;
            else throw new AIIlleagalMoveExeption();
        }
    }
}