# Mystery Code

Mystery Code is a fun and challenging game where players have to crack a secret code within a limited number of tries.

## Table of Contents

- [Introduction](#introduction)
- [Gameplay](#gameplay)
- [Technologies Used](#technologies-used)
- [Code Explanation](#code-explanation)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Running the Game](#running-the-game)
- [Unlock the Code Labyrinth: Customize Length & Attempts](#unlock-the-code-labyrinth-customize-length--attempts)

## Introduction

Mystery Code is a simple yet engaging game where the player must guess a randomly generated code made up of colored pegs. The game provides feedback on each guess, indicating how many colors are correct and in the correct position, as well as how many colors are correct but in the wrong position.

## Gameplay

1. The game will generate a random code consisting of 4 colors.
2. The available colors are: R (Red), G (Green), B (Blue), Y (Yellow), W (White), and O (Orange).
3. The player has 10 tries to guess the code.
4. After each guess, the game will provide feedback:
   - The number of correct colors in the correct position.
   - The number of correct colors in the incorrect position.
5. The game ends when the player guesses the code correctly or runs out of tries.

## Technologies Used

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Code Explanation

### The code consists of the following main components:

- **generate_code:** Generates a random code of 4 colors from the list of available colors.
- **guess_code:** Prompts the player to input their guess and validates it.
- **check_code:** Compares the player's guess to the generated code and provides feedback on the number of correct positions and colors.
- **game:** The main function that runs the game, handles player input, and provides feedback until the game ends.

## Prerequisites

Before running this project locally, ensure you have the following installed:

- Python: You can download it from the official website at [https://www.python.org/downloads/](https://www.python.org/downloads/).
- An IDE such as Visual Studio Code: You can download it from [https://code.visualstudio.com/](https://code.visualstudio.com/).

## Setup

### 1. Clone the repository

- Clone the repository using the following command:

  ```cmd
  git clone https://github.com/mohdimrandev/Mystery-Code.git
  ```

### 2. Navigate to the project directory

- Change to the project directory using the following command:

  ```cmd
  cd Mystery-Code
  ```

## Running the Game

- Start the game using Python:

  ```cmd
  python main.py
  ```

Follow Instructions: The game will display instructions and guide you through the gameplay.

Enjoy playing Mystery Code and challenge yourself to guess the code in the fewest tries possible!

### Unlock the Code Labyrinth: Customize Length & Attempts

- The current configuration allows for a code length of 4 and provides 10 attempts. You can modify these values within the script for customization.
