# Pong Game

## Introduction

Welcome to the Pong game. It's a simple implementation of the classic Pong arcade game, made with the help of the `pygame` library. Two players can play this game on the same keyboard.

## Prerequisites

Before you can run the game, ensure that you have the following installed:

1. Python: This game was developed using Python. Make sure you have Python installed. You can download it from [Python's official website](https://www.python.org/).

2. Pygame: This game uses the `pygame` library. If you haven't already installed it, you can do so using pip:
   ```bash
   pip install pygame
   ```

## Game Mechanics

### Ball

The ball moves diagonally across the screen. When it touches the top or bottom of the screen, it bounces off. If it touches one of the paddles, its horizontal direction is reversed. If the ball goes past a paddle and touches the side of the screen, the opposing player scores a point.

### Paddles

Each player controls a paddle using the keyboard. The paddles can only move vertically.

- **Left Paddle Controls**:

  - `W`: Move up
  - `S`: Move down

- **Right Paddle Controls**:
  - `Arrow Up`: Move up
  - `Arrow Down`: Move down

## How to Run

To play the game, simply navigate to the directory containing `pong.py` and run:

```bash
python pong.py
```

## Gameplay

The game window will open, and the ball will start moving. Use the keyboard controls to move your paddle and try to prevent the ball from passing it. The score is displayed at the top of the screen. The game continues until you close the game window.

## Closing Thoughts

Enjoy the game! Feel free to modify the code to add more features or adjust the game mechanics. If you encounter any issues or have suggestions, please reach out.
