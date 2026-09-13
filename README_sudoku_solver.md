Sudoku Solver🎀

A pastel-themed Sudoku solver desktop app, built with *Python** and *Tkinter**, using **backtracking algorithm** and **recursive method.**

##  Features🧜‍♀️

- Solves any valid 9×9 Sudoku puzzle instantly
- Pastel checkerboard grid styling — alternating pink and blue 3×3 boxes
- One-click sample puzzle loader
- Clear board button
- Friendly status messages after each action

  ## Screenshots
  <img width="400" height="200" alt="Screenshot 2026-09-13 164246" src="https://github.com/user-attachments/assets/19fcbea9-4fdb-4e72-9af4-5cfbfa2c936b" />
  The main structure

<img width="400" height="200" alt="Screenshot 2026-09-13 164324" src="https://github.com/user-attachments/assets/9fb238d1-a714-463d-adda-f79ce0e3b229" />
Sample Puzzle loaded!

<img width="400" height="200" alt="Screenshot 2026-09-13 164420" src="https://github.com/user-attachments/assets/1d149478-1e80-4b54-881c-debdcd0d9485" />
Sudoku Solved!!

  

##  How it works 🤺

The solver uses **recursive backtracking**:

1. Find the first empty cell.
2. Try placing digits `1–9` in it.
3. For each digit, check the row, column, and 3×3 box for conflicts.
4. If a digit is valid, place it and recurse into the next empty cell.
5. If a later cell has no valid digit, backtrack — undo the last placement and try the next option.
6. Repeat until the board is completely filled (base case), or every option is exhausted.

No external solving libraries — just plain recursion.

## 📦 Requirements

- Python 3.8+
- Tkinter (included with most standard Python installations)

No third-party packages are required.


##  Project structure

```
cute-sudoku-solver/
├── sudoku_solver.py   # Main app: solver logic + Tkinter GUI
├── README.md
├── LICENSE
└── .gitignore
```



##  Possible future improvements

- Step-by-step animated solving mode
- Difficulty levels
- Save/load puzzles from file

##  License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.
