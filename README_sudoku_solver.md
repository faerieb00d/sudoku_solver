# 🌸 Cute Sudoku Solver

A pastel-themed Sudoku solver desktop app, built with **Python** and **Tkinter**, powered by a **recursive backtracking algorithm**.

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-ff69b4)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

## ✨ Features

- Solves any valid 9×9 Sudoku puzzle instantly
- Pastel checkerboard grid styling — alternating pink and blue 3×3 boxes
- Given numbers and solved numbers shown in different colors
- One-click sample puzzle loader
- Clear board button
- Friendly status messages after each action

## 🧠 How it works

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

## ▶️ Usage

Clone the repo and run the script:

```bash
git clone https://github.com/<your-username>/cute-sudoku-solver.git
cd cute-sudoku-solver
python sudoku_solver.py
```

Then:
1. Type numbers into the grid (or click **Sample** to load a demo puzzle).
2. Click **Solve** to instantly fill in the rest.
3. Click **Clear** to start over.

## 🗂️ Project structure

```
cute-sudoku-solver/
├── sudoku_solver.py   # Main app: solver logic + Tkinter GUI
├── README.md
├── LICENSE
└── .gitignore
```

## 📸 Screenshots

_Add a screenshot of the app here once you take one — drag an image into this section on GitHub, e.g.:_

```markdown
![App screenshot](screenshots/app.png)
```

## 🛠️ Possible future improvements

- Random puzzle generator (instead of a single fixed sample)
- Step-by-step animated solving mode
- Difficulty levels
- Save/load puzzles from file

## 📄 License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.
