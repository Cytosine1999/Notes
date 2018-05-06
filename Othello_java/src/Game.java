import Board.Board;
import Board.IllegalMoveException;

public class Game {
    private Board[] boardRecord = new Board[61];
    private int turn;

    public Game() {
        boardRecord[0] = new Board();
        turn = 0;
    }

    public boolean getPlayer() {
        return boardRecord[turn].getFirst();
    }

    public int getWinner() {
        int number[] = new int[2];
        number[0] = boardRecord[turn].getNumber(true);
        number[1] = boardRecord[turn].getNumber(false);
        if (number[0] > number[1]) return 1;
        else if (number[0] < number[1]) return 2;
        else return 0;
    }

    public Board getBoard(int n) {
        return boardRecord[n];
    }

    public boolean end() {
        return !boardRecord[turn].end();
    }

    public int getTurn() {
        return turn;
    }

    public void unDo(boolean a) {
        if (a) {
            if (turn > 0) {
                turn -= 1;
                System.out.println("悔棋");
                System.out.println(this);
            } else System.out.println("无法悔棋");
        } else if (turn > 1) {
            turn -= 2;
            System.out.println("悔棋");
            System.out.println(this);
        } else System.out.println("无法悔棋");
    }

    public String toString() {
        String a;
        if (boardRecord[turn].getTurn() == 0) a = "\n游戏开始\n";
        else a = "第" + boardRecord[turn].getTurn() + "手\n";
        a += boardRecord[turn].toString() + "\n";
        return a;
    }

    public boolean move(int a, int b) {
        try {
            boardRecord[turn + 1] = new Board(boardRecord[turn], a, b);
            turn++;
        } catch (IllegalMoveException e) {
            return false;
        }
        return true;
    }
}