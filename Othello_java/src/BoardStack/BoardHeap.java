package BoardStack;

import Board.Board;
import Board.IllegalMoveException;

public class BoardHeap extends Board {
    private BoardHeap fatherBoard;
    private int fatherIndex;
    private BoardHeap[] sonBoard;
    private int[][] access;
    private int depth;
    private boolean[] sonBoardInitialized;
    public int value;

    public BoardHeap(Board a) {
        super(a);
        fatherBoard = null;
        fatherIndex = -1;
        depth = 0;
        boardHeap();
    }

    private BoardHeap(BoardHeap a, int b, int c, int index) throws IllegalMoveException {
        super(a, b, c);
        fatherBoard = a;
        fatherIndex = index;
        depth = a.depth + 1;
        boardHeap();
    }

    private void boardHeap() {
        sonBoard = new BoardHeap[accessNum];
        access = new int[accessNum][];
        sonBoardInitialized = new boolean[accessNum];
        int index = 0;
        for (int n = 0; n < 8; n++) {
            for (int m = 0; m < 8; m++) {
                if (board[n][m] > 0) {
                    access[index] = new int[]{n, m};
                    index++;
                }
            }
        }
    }

    public BoardHeap getFatherBoard() {
        return fatherBoard;
    }

    public int getFatherIndex() {
        return fatherIndex;
    }

    public int getDepth() {
        return depth;
    }

    public BoardHeap getSonBoard(int x) throws IllegalMoveException {
        if (!sonBoardInitialized[x]) {
            sonBoard[x] = new BoardHeap(this, access[x][0], access[x][1], x);
            sonBoardInitialized[x] = true;
        }
        return sonBoard[x];
    }

    public boolean hasNext() {
        if (fatherBoard == null) return false;
        return fatherIndex + 1 < fatherBoard.accessNum;
    }

    public BoardHeap getNext() throws IllegalMoveException {
        return fatherBoard.getSonBoard(fatherIndex + 1);
    }

    public void sonBoardUnInitialize() {
        for (int n = 0; n < accessNum; n++) {
            if (sonBoardInitialized[n]) {
                sonBoard[n].sonBoardUnInitialize();
                sonBoard[n].fatherBoard = null;
                sonBoard[n] = null;
            }
        }
    }

    public int[] getSonBoardMove(int x) {
        return access[x];
    }
}