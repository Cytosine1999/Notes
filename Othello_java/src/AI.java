import java.io.IOException;

import Board.IllegalMoveException;
import BoardStack.BoardHeap;

public class AI {
    private Game game;
    private boolean first;
    private int[] result = new int[2];
    private int[][] access;
    private int accessNum;
    private BoardHeap theBoard;

    public AI(Game a, boolean b) throws IOException {
        first = b;
        game = a;
    }

    static final int[][] weight = {{50, -15, 10, 5, 5, 10, -15, 50}, {-15, -20, -10, -5, -5, -10, -20, -15}, {10, -10, 2, 1, 1, 2, -10, 10}, {5, -5, 1, 1, 1, 1, -5, 5}, {5, -5, 1, 1, 1, 1, -5, 5}, {10, -10, 2, 1, 1, 2, -10, 10}, {-15, -20, -10, -5, -5, -10, -20, -15}, {50, -15, 10, 5, 5, 10, -15, 50}};

    public int[] move() throws IllegalMoveException {
        result = new int[2];
        theBoard = new BoardHeap(game.getBoard(game.getTurn()));
        access = theBoard.getBoard();
        accessNum = theBoard.getAccessNum();
        miniMax(2);
        int y = (int) Math.floor(accessNum * Math.random()) + 1;
        for (int n = 0; n < 8; n++) {
            for (int m = 0; m < 8; m++) {
                if (access[n][m] > 0) y--;
                if (y == 0) {
                    result[0] = n;
                    result[1] = m;
                    return result;
                }
            }
        }
        return null;
    }

    private void miniMax(int depth) throws IllegalMoveException {

    }

    private void evaluator(BoardHeap board) {
        int result = 0;
        if (board.end()) {
            int a = board.getNumber(true);
            int b = board.getNumber(false);
            if ((a > b) == first) result = 30000;
            else result = -30000;
        } else {
            int a[][] = board.getBoard();
            for (int n = 0; n < 8; n++) {
                for (int m = 0; m < 8; m++) {
                    if (a[n][m] == -1) if (first) result += weight[n][m];
                    else result -= weight[n][m];
                    else if (a[n][m] == -2) if (first) result -= weight[n][m];
                    else result += weight[n][m];
                }
            }
        }
        board.value = result;
    }
}