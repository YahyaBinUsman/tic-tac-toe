import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_widgets()

    def create_widgets(self):
        self.info_label = tk.Label(self.master, text="Player 1's Turn (X)")
        self.info_label.grid(row=0, column=0, columnspan=3)

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.master, text="", width=10, height=4,
                                                command=lambda i=i, j=j: self.on_button_click(i, j))
                self.buttons[i][j].grid(row=i+1, column=j)

        self.restart_button = tk.Button(self.master, text="Restart", command=self.restart_game)
        self.restart_button.grid(row=4, column=0, columnspan=3)

    def on_button_click(self, i, j):
        if self.board[i][j] == ' ':
            self.board[i][j] = self.current_player
            self.buttons[i][j].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Winner", f"Player {self.current_player} wins!")
                self.restart_game()
            elif self.check_draw():
                messagebox.showinfo("Draw", "It's a draw!")
                self.restart_game()
            else:
                self.switch_player()

    def switch_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'
        self.info_label.config(text=f"Player {self.current_player}'s Turn")

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        return False

    def check_draw(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def restart_game(self):
        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")
        self.info_label.config(text="Player 1's Turn (X)")


def main():
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

if __name__ == "__main__":
    main()
