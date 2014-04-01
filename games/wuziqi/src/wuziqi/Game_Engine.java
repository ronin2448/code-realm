package wuziqi;

public class Game_Engine {

	private Board myBoard;
	private boolean isWhitePlayerTurn;
	
	public Game_Engine() {
		reset();
	}

	private void reset() {
		myBoard = new Board();
		isWhitePlayerTurn = true;
	}
	
	
	
}
