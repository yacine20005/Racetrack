# Racetrack

Racetrack is a Python-based game where players navigate a pawn across a board, avoiding obstacles and aiming to reach the finish line. The game features several play modes and a solver that can automatically complete levels using different algorithms.

---

## Table of Contents

- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Game Rules](#game-rules)
- [Game Modes](#game-modes)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

---

## Project Structure

The codebase is organized into the following files:

- **`main.py`**: Entry point of the game.
- **`affichage.py`**: Handles game display and rendering.
- **`boutons.py`**: Manages game buttons.
- **`conversion.py`**: Handles data conversion for the game.
- **`fltk.py`**: Manages the graphical user interface components.
- **`grillage.py`**: Handles the game grid.
- **`jeu.py`**: Core game logic.
- **`menu.py`**: Manages the game menu.
- **`mouvement.py`**: Controls pawn movement.
- **`sauvegarde.py`**: Manages saving and loading games.
- **`solveur.py`**: Contains algorithms for solving levels automatically.
- **`utilitaire.py`**: Utility functions for various game features.

---

## Getting Started

To run the project, ensure you have Python 3.x installed. Then, execute the following command in your terminal:

```bash
python main.py
```

---

## Game Rules

- Move your pawn across the board while avoiding obstacles.
- The goal is to reach the finish square.
- You can move in eight directions (up, down, left, right, and diagonals).
- Use strategy to avoid traps and reach the end as efficiently as possible.

---

## Game Modes

Racetrack offers several modes:

- **Play Mode**: Start a new game or load a previously saved game.
- **Solver Mode**: Let the game solve a level automatically using various algorithms (Depth-First Search, Breadth-First Search, Random, Bidirectional).
- **Options Mode**: Configure the game (choose map, rules, display options, solver selection).

---

## Dependencies

Before running Racetrack, make sure the following dependencies are installed:

- Python 3.x
- Tkinter (usually included with Python)
- PIL / Pillow (Python Imaging Library) for image handling

You can install Pillow using pip:

```bash
pip install Pillow
```

---
