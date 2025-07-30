# Demo-2025 - Tic-Tac-Toe Game

A simple and interactive Tic-Tac-Toe game demo built with vanilla HTML, CSS, and JavaScript.

## Features

- **Interactive Gameplay**: Click on any cell to place your mark (X or O)
- **Turn-based System**: Alternates between Player X and Player O automatically
- **Win Detection**: Automatically detects winning conditions and highlights winning cells
- **Draw Detection**: Recognizes when the game ends in a draw
- **Score Tracking**: Keeps track of wins for both players and draws across multiple games
- **Persistent Scores**: Scores are saved in browser's local storage
- **Responsive Design**: Works on desktop and mobile devices
- **Smooth Animations**: Enhanced user experience with CSS animations and transitions

## How to Run

### Option 1: Direct File Opening
1. Clone or download this repository
2. Open the `index.html` file in any modern web browser
3. Start playing immediately!

### Option 2: Local Server (Recommended)
If you have Python installed:
```bash
# Navigate to the project directory
cd Demo-2025

# Python 3
python -m http.server 8000

# Python 2
python -m SimpleHTTPServer 8000
```

Then open your browser and go to `http://localhost:8000`

### Option 3: Using Node.js
If you have Node.js installed:
```bash
# Install a simple server globally
npm install -g http-server

# Navigate to the project directory and run
cd Demo-2025
http-server
```

Then open the provided URL in your browser.

## How to Play

1. **Starting the Game**: Player X always goes first
2. **Making a Move**: Click on any empty cell to place your mark
3. **Winning**: Get three of your marks in a row (horizontally, vertically, or diagonally)
4. **Reset**: Click the "Reset Game" button to start a new round
5. **Scores**: View your cumulative scores at the bottom of the game

## Game Rules

- Players take turns placing their marks (X and O) on a 3×3 grid
- The first player to get three marks in a row wins
- If all cells are filled without a winner, the game is a draw
- Scores are automatically tracked and persist between browser sessions

## Technical Details

- **No Dependencies**: Built with vanilla web technologies
- **Browser Compatibility**: Works in all modern browsers
- **Mobile Friendly**: Responsive design adapts to different screen sizes
- **Local Storage**: Scores persist between browser sessions
- **Clean Code**: Well-structured and commented JavaScript

## File Structure

```
Demo-2025/
├── index.html      # Main HTML structure
├── style.css       # Game styling and animations
├── script.js       # Game logic and interactivity
└── README.md       # This file
```

## Development

This demo is perfect for:
- Learning web development basics
- Understanding game logic implementation
- Exploring CSS animations and responsive design
- Demonstrating JavaScript DOM manipulation

Feel free to modify and enhance the game with additional features!