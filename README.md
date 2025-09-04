# 🐍 Snake Game (Python - Turtle)

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
[![Status](https://img.shields.io/badge/Status-Completed-brightgreen)](#)  

A classic **Snake Game** built with **Python** and the **Turtle** graphics library.  
The goal is to eat apples, grow the snake, and reach **100 points** to win.  
The game also keeps track of the **High Score** across plays.

---

## 📌 Requirements

- Python 3.8 or higher
- Built-in libraries:
  - `turtle`
  - `time`
  - `random`

---

## ▶️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/zz1-56/snake_game.git
   cd snake_game
Run the main file:
  start_game.py
bash

python start.py
🎮 Controls
Use the arrow keys to control the snake:

⬆️ Up → Move Up

⬇️ Down → Move Down

⬅️ Left → Move Left

➡️ Right → Move Right

🏆 Win & Lose Conditions
Win: Reach 100 points 🎉

Lose: Collision with the wall or with the snake’s own body ❌

📂 Project Structure
bash

snake_game/
│
├── start_game.py         # Main game logic and controls
├── apple.py         # Apple class (spawning and hiding apples)
├── score_board.py   # Scoreboard class (tracks score & high score)
├── snake_body.py    # Snake class (movement & growing the snake)
└── highscore.txt    # Stores the best score between sessions
✨ Preview
<img width="799" height="629" alt="image" src="https://github.com/user-attachments/assets/65bd9169-ec03-47e7-997b-c1536dc4a7f8" />


📌 Notes
The game only uses the built-in turtle, time, and random modules.

High scores are saved in the highscore.txt file.

The snake speeds up slightly each time it eats an apple.
