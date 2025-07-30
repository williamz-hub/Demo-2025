class TicTacToe {
    constructor() {
        this.board = Array(9).fill('');
        this.currentPlayer = 'X';
        this.gameActive = true;
        this.scores = {
            X: 0,
            O: 0,
            draw: 0
        };
        
        this.winningConditions = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ];
        
        this.initializeGame();
    }
    
    initializeGame() {
        this.statusDisplay = document.getElementById('status');
        this.gameBoard = document.getElementById('gameBoard');
        this.resetBtn = document.getElementById('resetBtn');
        this.scoreX = document.getElementById('scoreX');
        this.scoreO = document.getElementById('scoreO');
        this.scoreDraw = document.getElementById('scoreDraw');
        
        this.cells = document.querySelectorAll('.cell');
        
        this.addEventListeners();
        this.updateDisplay();
        this.loadScores();
    }
    
    addEventListeners() {
        this.cells.forEach((cell, index) => {
            cell.addEventListener('click', () => this.handleCellClick(index));
        });
        
        this.resetBtn.addEventListener('click', () => this.resetGame());
    }
    
    handleCellClick(index) {
        if (this.board[index] !== '' || !this.gameActive) {
            return;
        }
        
        this.board[index] = this.currentPlayer;
        this.updateCellDisplay(index);
        
        if (this.checkWinner()) {
            this.gameActive = false;
            this.highlightWinningCells();
            this.statusDisplay.textContent = `Player ${this.currentPlayer} wins!`;
            this.scores[this.currentPlayer]++;
            this.updateScoreDisplay();
            this.saveScores();
            return;
        }
        
        if (this.checkDraw()) {
            this.gameActive = false;
            this.statusDisplay.textContent = "It's a draw!";
            this.scores.draw++;
            this.updateScoreDisplay();
            this.saveScores();
            return;
        }
        
        this.currentPlayer = this.currentPlayer === 'X' ? 'O' : 'X';
        this.statusDisplay.textContent = `Player ${this.currentPlayer}'s turn`;
    }
    
    updateCellDisplay(index) {
        const cell = this.cells[index];
        cell.textContent = this.currentPlayer;
        cell.classList.add(this.currentPlayer.toLowerCase());
        cell.classList.add('disabled');
    }
    
    checkWinner() {
        return this.winningConditions.some(condition => {
            const [a, b, c] = condition;
            return this.board[a] && 
                   this.board[a] === this.board[b] && 
                   this.board[a] === this.board[c];
        });
    }
    
    checkDraw() {
        return this.board.every(cell => cell !== '');
    }
    
    highlightWinningCells() {
        this.winningConditions.forEach(condition => {
            const [a, b, c] = condition;
            if (this.board[a] && 
                this.board[a] === this.board[b] && 
                this.board[a] === this.board[c]) {
                this.cells[a].classList.add('winning-cell');
                this.cells[b].classList.add('winning-cell');
                this.cells[c].classList.add('winning-cell');
            }
        });
    }
    
    resetGame() {
        this.board = Array(9).fill('');
        this.currentPlayer = 'X';
        this.gameActive = true;
        
        this.cells.forEach(cell => {
            cell.textContent = '';
            cell.classList.remove('x', 'o', 'disabled', 'winning-cell');
        });
        
        this.statusDisplay.textContent = `Player ${this.currentPlayer}'s turn`;
    }
    
    updateDisplay() {
        this.statusDisplay.textContent = `Player ${this.currentPlayer}'s turn`;
    }
    
    updateScoreDisplay() {
        this.scoreX.textContent = this.scores.X;
        this.scoreO.textContent = this.scores.O;
        this.scoreDraw.textContent = this.scores.draw;
    }
    
    saveScores() {
        localStorage.setItem('ticTacToeScores', JSON.stringify(this.scores));
    }
    
    loadScores() {
        const savedScores = localStorage.getItem('ticTacToeScores');
        if (savedScores) {
            this.scores = JSON.parse(savedScores);
            this.updateScoreDisplay();
        }
    }
}

// Initialize the game when the DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new TicTacToe();
});

// Add some fun animations and effects
document.addEventListener('DOMContentLoaded', () => {
    // Add a subtle animation to the title
    const title = document.querySelector('h1');
    title.style.opacity = '0';
    title.style.transform = 'translateY(-20px)';
    
    setTimeout(() => {
        title.style.transition = 'all 0.6s ease';
        title.style.opacity = '1';
        title.style.transform = 'translateY(0)';
    }, 100);
    
    // Add staggered animation to game board cells
    const cells = document.querySelectorAll('.cell');
    cells.forEach((cell, index) => {
        cell.style.opacity = '0';
        cell.style.transform = 'scale(0.8)';
        
        setTimeout(() => {
            cell.style.transition = 'all 0.3s ease';
            cell.style.opacity = '1';
            cell.style.transform = 'scale(1)';
        }, 200 + index * 50);
    });
});