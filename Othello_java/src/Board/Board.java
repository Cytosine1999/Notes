package Board;

public class Board {
    protected int[][] board = new int[8][8];
    protected int turn;
    protected int[] move;
    protected int accessNum;
    protected boolean first;
    protected boolean end;

    public Board() {
        board[3][3] = -1;
        board[4][4] = -1;
        board[4][3] = -2;
        board[3][4] = -2;
        board[4][2] = 1;
        board[5][3] = 1;
        board[2][4] = 1;
        board[3][5] = 1;
        turn = 0;
        move = null;
        accessNum = 4;
        first = true;
    }

    public Board(Board c, int a, int b) throws IllegalMoveException {
        if (c.getBoard()[a][b] > 0) {
            board = c.getBoard();
            int friend;
            int enemy;
            int x;
            int y;
            if (c.first) {
                friend = -1;
                enemy = -2;
            } else {
                friend = -2;
                enemy = -1;
            }
            x = a - 1;
            while (x > 0 && board[x][b] == enemy) x--;
            if (x > -1 && board[x][b] == friend) for (int n = a; n > x; n--)
                board[n][b] = friend;
            x = a - 1;
            y = b + 1;
            while (x > 0 && y < 7 && board[x][y] == enemy) {
                x--;
                y++;
            }
            if (x > -1 && y < 8 && board[x][y] == friend) {
                int m = b;
                for (int n = a; n > x; n--, m++)
                    board[n][m] = friend;
            }
            y = b + 1;
            while (y < 7 && board[a][y] == enemy) y++;
            if (y < 8 && board[a][y] == friend) for (int m = b; m < y; m++)
                board[a][m] = friend;
            x = a + 1;
            y = b + 1;
            while (x < 7 && y < 7 && board[x][y] == enemy) {
                x++;
                y++;
            }
            if (x < 8 && y < 8 && board[x][y] == friend) {
                int m = b;
                for (int n = a; n < x; n++, m++)
                    board[n][m] = friend;
            }
            x = a + 1;
            while (x < 7 && board[x][b] == enemy) x++;
            if (x < 8 && board[x][b] == friend) for (int n = a; n < x; n++)
                board[n][b] = friend;
            x = a + 1;
            y = b - 1;
            while (x < 7 && y > 0 && board[x][y] == enemy) {
                x++;
                y--;
            }
            if (x < 8 && y > -1 && board[x][y] == friend) {
                int m = b;
                for (int n = a; n < x; n++, m--)
                    board[n][m] = friend;
            }
            y = b - 1;
            while (y > 0 && board[a][y] == enemy) y--;
            if (y > -1 && board[a][y] == friend) for (int m = b; m > y; m--)
                board[a][m] = friend;
            x = a - 1;
            y = b - 1;
            while (x > 0 && y > 0 && board[x][y] == enemy) {
                x--;
                y--;
            }
            if (x > -1 && y > -1 && board[x][y] == friend) {
                int m = b;
                for (int n = a; n > x; n--, m--)
                    board[n][m] = friend;
            }
            if (c.getFirst()) {
                accessNum = test(-2);
            } else {
                accessNum = test(-1);
            }
            if (accessNum == 0) {
                if (c.first) {
                    accessNum = test(-1);
                } else {
                    accessNum = test(-2);
                }
                first = c.first;
            } else first = !c.first;
            if (accessNum == 0) end = true;
            else end = false;
            turn = c.turn + 1;
            move = new int[2];
            move[0] = a;
            move[1] = b;
        } else throw new IllegalMoveException();
    }

    protected Board(Board a) {
        board = a.getBoard();
        try {
            move = a.getMove();
        } catch (NullPointerException e) {
            move = null;
        }
        accessNum = a.accessNum;
        first = a.first;
        end = a.end;
    }

    public int[][] getBoard() {
        int[][] a = new int[8][8];
        for (int n = 0; n < 8; n++)
            for (int m = 0; m < 8; m++)
                a[n][m] = board[n][m];
        return a;
    }

    public int getTurn() {
        return turn;
    }

    public int[] getMove() {
        int a[] = new int[2];
        a[0] = move[0];
        a[1] = move[1];
        return a;
    }

    public int getAccessNum() {
        return accessNum;
    }

    public boolean getFirst() {
        return first;
    }

    public boolean end() {
        return end;
    }

    public int getNumber(boolean first) {
        int num = 0;
        if (first) {
            for (int n = 0; n < 8; n++)
                for (int m = 0; m < 8; m++)
                    if (board[n][m] == -1) num++;
        } else {
            for (int n = 0; n < 8; n++)
                for (int m = 0; m < 8; m++)
                    if (board[n][m] == -2) num++;
        }
        return num;
    }

    public String toString() {
        String a = "   A  B  C  D  E  F  G  H\n";
        for (int n = 0; n < 8; n++) {
            a += n + " ";
            for (int m = 0; m < 8; m++) {
                if (board[n][m] == -1) a += "[O]";
                else if (board[n][m] == -2) a += "[X]";
                else a += "[ ]";
            }
            a += "\n";
        }
        a += "玩家O：" + getNumber(true) + " 玩家X：" + getNumber(false);
        return a;
    }

    private int test(int friend) {
        int enemy = (-3) - friend;
        int sum;
        int a;
        int num = 0;
        int x;
        int y;
        for (int n = 0; n < 8; n++) {
            for (int m = 0; m < 8; m++) {
                if (board[n][m] > -1) {
                    sum = 0;
                    a = 0;
                    x = n - 1;
                    while (x > 0 && board[x][m] == enemy) {
                        a++;
                        x--;
                    }
                    if (x > -1 && board[x][m] == friend) sum += a;
                    a = 0;
                    x = n - 1;
                    y = m + 1;
                    while (x > 0 && y < 7 && board[x][y] == enemy) {
                        a++;
                        x--;
                        y++;
                    }
                    if (x > -1 && y < 8 && board[x][y] == friend) sum += a;
                    a = 0;
                    y = m + 1;
                    while (y < 7 && board[n][y] == enemy) {
                        a++;
                        y++;
                    }
                    if (y < 8 && board[n][y] == friend) sum += a;
                    a = 0;
                    x = n + 1;
                    y = m + 1;
                    while (x < 7 && y < 7 && board[x][y] == enemy) {
                        a++;
                        x++;
                        y++;
                    }
                    if (x < 8 && y < 8 && board[x][y] == friend) sum += a;
                    a = 0;
                    x = n + 1;
                    while (x < 7 && board[x][m] == enemy) {
                        a++;
                        x++;
                    }
                    if (x < 8 && board[x][m] == friend) sum += a;
                    a = 0;
                    x = n + 1;
                    y = m - 1;
                    while (x < 7 && y > 0 && board[x][y] == enemy) {
                        a++;
                        x++;
                        y--;
                    }
                    if (x < 8 && y > -1 && board[x][y] == friend) sum += a;
                    a = 0;
                    y = m - 1;
                    while (y > 0 && board[n][y] == enemy) {
                        a++;
                        y--;
                    }
                    if (y > -1 && board[n][y] == friend) sum += a;
                    a = 0;
                    x = n - 1;
                    y = m - 1;
                    while (x > 0 && y > 0 && board[x][y] == enemy) {
                        a++;
                        x--;
                        y--;
                    }
                    if (x > -1 && y > -1 && board[x][y] == friend) sum += a;
                    board[n][m] = sum;
                    if (sum > 0) num++;
                }
            }
        }
        return num;
    }
}