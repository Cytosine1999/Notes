import java.io.IOException;

import Board.IllegalMoveException;

public class OthelloChar {
    public static void main(String[] args) throws IOException, AIIlleagalMoveExeption, IllegalMoveException {
        Game game;
        Player[] player = new Player[2];
        int flag;
        outerLoop:
        while (true) {
            game = new Game();
            System.out.println("==========OTHELLO==========");
            IntInputMatcher IIM1 = new IntInputMatcher(1, 4, "双人模式请输入1\n人机对战请输入2\n观摩对局请输入3\n结束游戏请输入4", "输入不合法 请重新输入\n双人模式请输入1\n人机对战请输入2\n观摩对局请输入3\n结束游戏请输入4");
            if ( IIM1.result == 1 ) {
                IntInputMatcher IIM2 = new IntInputMatcher( 1 , 2 , "抛掷硬币以决定玩家先后请输入1\n开始游戏请输入2" , "输入不合法 请重新输入\n抛掷硬币以决定玩家先后请输入1\n开始游戏请输入2" ) ;
                if ( IIM2.result == 1 ) {
                    if ( Math.random ( ) < 0.5 ) System.out.println ( "正面" ) ;
                    else System.out.println ( "反面" ) ;
                }
                player [ 0 ] = new Player ( game , true , true ) ;
                player [ 1 ] = new Player ( game , false , true ) ;
            }
            else if (IIM1.result == 2) {
                IntInputMatcher IIM2 = new IntInputMatcher(1, 2, "抛掷硬币以决定玩家先后请输入1\n开始游戏请输入2", "输入不合法 请重新输入\n抛掷硬币以决定玩家先后请输入1\n开始游戏请输入2");
                if (IIM2.result == 1) {
                    if (Math.random() < 0.5) System.out.println("正面");
                    else System.out.println("反面");
                }
                player[0] = new Player(game, true, true);
                boolean human;
                if (IIM2.result == 1) {
                    human = true;
                } else if (IIM2.result == 2) {
                    human = false;
                } else {
                    if (Math.random() < 0.5) {
                        System.out.println("玩家为先手O");
                        human = true;
                    } else {
                        System.out.println("玩家为后手X");
                        human = false;
                    }
                }
                if (human) {
                    player[0] = new Player(game, true, true);
                    player[1] = new Player(game, false, false);
                } else {
                    player[0] = new Player(game, true, false);
                    player[1] = new Player(game, false, true);
                }
            } else if (IIM1.result == 3) {
                player[0] = new Player(game, true, false);
                player[1] = new Player(game, false, false);
            } else {
                System.out.println("游戏已关闭");
                break;
            }
            System.out.println("游戏中可以输入1悔棋，输入2重新开始，输入3结束游戏");
            System.out.println(game);
            while (game.end()) {
                if (game.getPlayer()) flag = player[0].move();
                else flag = player[1].move();
                if (flag == 1) {
                    System.out.println("游戏结束");
                    continue outerLoop;
                } else if (flag == 2) {
                    System.out.println("游戏已关闭");
                    break outerLoop;
                }
                System.out.println(game);
            }
            int i = game.getWinner();
            if (i == 0) System.out.println("游戏结束 平局\n");
            else if (i == 1) System.out.println("游戏结束 玩家O获胜\n");
            else System.out.println("游戏结束 玩家X获胜\n");
        }
    }
}