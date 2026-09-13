# Creating Sudoku solver using backtracking algorithm and recursion method.
# Tkinter is used for the GUI.

import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox


def find_empty_location(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return (r, c)
    return None


def is_valid(board, r, c, num):
    for i in range(9):
        if board[r][i] == num and i != c:
            return False

    for i in range(9):
        if board[i][c] == num and i != r:
            return False

    box_r = (r // 3) * 3
    box_c = (c // 3) * 3
    for i in range(box_r, box_r + 3):
        for j in range(box_c, box_c + 3):
            if board[i][j] == num and (i, j) != (r, c):
                return False

    return True


def solve(board):
    empty_loc = find_empty_location(board)
    if not empty_loc:
        return True

    r, c = empty_loc
    for num in range(1, 10):
        if is_valid(board, r, c, num):
            board[r][c] = num
            if solve(board):
                return True
            board[r][c] = 0
    return False


# Making it look pleasing
BG = "#380202"
BOX_LIGHT = "#ffe6f0"
BOX_DARK = "#e6f7ff"
GIVEN_FG = "#930707"
USER_FG = "#6a0336"
ACCENT = "#A1D6DA"
ACCENT_HOVER = "#ad03b9"
CLEAR_BTN = "#B5EBB5"
CLEAR_HOVER = "#f2ccde"
SAMPLE_BTN = "#cfafd5"
SAMPLE_HOVER = "#a8afd7"
TEXT_DARK = "#FBF5A1"

SAMPLE_PUZZLE = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]


class SudokuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        self.root.configure(bg=BG)

        self.title_font = tkfont.Font(family="Broadway", size=24, weight="bold")
        self.cell_font = tkfont.Font(family="Comic Sans MS", size=16, weight="bold")
        self.btn_font = tkfont.Font(family="Comic Sans MS", size=12, weight="bold")
        self.msg_font = tkfont.Font(family="Comic Sans MS", size=15, weight="bold")
        self.entries = [[None for _ in range(9)] for _ in range(9)]

        self._build_header()
        self._build_grid()
        self._build_buttons()
        self._build_status()

    def _build_header(self):
        tk.Label(
            self.root,
            text="Sudoku Solver",
            font=self.title_font,
            bg=BG,
            fg=TEXT_DARK,
            pady=14,
        ).pack()

    def _build_grid(self):
        grid_frame = tk.Frame(self.root, bg="#FFFFA7", padx=3, pady=3)
        grid_frame.pack(padx=16, pady=8)

        for box_r in range(3):
            for box_c in range(3):
                box_frame = tk.Frame(
                    grid_frame,
                    bg=BOX_LIGHT if (box_r + box_c) % 2 == 0 else BOX_DARK,
                    highlightbackground= "#FFFFA7",
                    highlightthickness=2,
                )

              
                box_frame.grid(row=box_r, column=box_c, padx=1, pady=1)

                for r in range(3):
                    for c in range(3):
                        entry = tk.Entry(
                            box_frame,
                            width=3,
                            font=self.cell_font,
                            justify="center",
                            bd=2,
                            relief="ridge",
                        )
                        entry.grid(row=r, column=c, padx=1, pady=1)
                        self.entries[box_r * 3 + r][box_c * 3 + c] = entry

                        if (box_r + box_c + r + c) % 2 == 0:
                            entry.configure(bg=BOX_LIGHT)
                        else:
                            entry.configure(bg=BOX_DARK)

    def _build_buttons(self):
        button_frame = tk.Frame(self.root, bg=BG)
        button_frame.pack(pady=8)

        tk.Button(
            button_frame,
            text="Solve",
            bg=ACCENT,
            fg="#240003",
            font=self.btn_font,
            width=10,
            command=self.solve_puzzle,
        ).grid(row=0, column=0, padx=8)

        tk.Button(
            button_frame,
            text="Clear",
            bg=CLEAR_BTN,
            fg="#240003",
            font=self.btn_font,
            width=10,
            command=self.clear_board,
        ).grid(row=0, column=1, padx=8)

        tk.Button(
            button_frame,
            text="Sample",
            bg=SAMPLE_BTN,
            fg="#240003",
            font=self.btn_font,
            width=10,
            command=self.load_sample,
        ).grid(row=0, column=2, padx=8)

    def _build_status(self):
        self.status_var = tk.StringVar(value="")
        self.status_label = tk.Label(
            self.root,
            textvariable=self.status_var,
            bg=BG,
            fg=TEXT_DARK,
            font=self.msg_font,
            pady=8,
        )
        self.status_label.pack()

    def _get_board(self):
        board = []
        for r in range(9):
            row = []
            for c in range(9):
                value = self.entries[r][c].get().strip()
                row.append(int(value) if value else 0)
            board.append(row)
        return board

    def _set_board(self, board):
        for r in range(9):
            for c in range(9):
                value = board[r][c]
                self.entries[r][c].delete(0, tk.END)
                if value != 0:
                    self.entries[r][c].insert(0, str(value))
                    self.entries[r][c].configure(fg=GIVEN_FG)
                else:
                    self.entries[r][c].configure(fg=USER_FG)

    def solve_puzzle(self):
        board = self._get_board()
        if not solve(board):
            messagebox.showerror("Sudoku Solver", "This puzzle has no solution 🤺")
            self.status_var.set("No solution found ಥ_ಥ")
            return

        self._set_board(board)
        self.status_var.set("Solved (❤️ ω ❤️)")

    def clear_board(self):
        for r in range(9):
            for c in range(9):
                self.entries[r][c].delete(0, tk.END)
                self.entries[r][c].configure(fg=USER_FG)
        self.status_var.set("Board cleared(✿◕‿◕✿)")

    def load_sample(self):
        self._set_board(SAMPLE_PUZZLE)
        self.status_var.set("Sample puzzle loaded 🐣")

        


if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuApp(root)
    root.mainloop()





