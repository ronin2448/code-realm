package wuziqi;

import javax.swing.JFrame;

public class Wuziqi_app extends JFrame {

	private static final long serialVersionUID = -5761346024951445462L;
	private int numberOfPlayers;
	
	
	public Wuziqi_app() {
		this.setSize(1000, 1000);
		this.setTitle("Wuziqi");
		this.setVisible(true);
	}

	public static void main(String[] args) {
		Wuziqi_app game = new Wuziqi_app();
	}

}
