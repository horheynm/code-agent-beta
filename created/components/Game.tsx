import React, { useState } from 'react';

// Interface for the game board state
interface BoardState {
  squares: Array<string>;
  xIsNext: boolean;
}

const Game: React.FC = () => {
  // Initialize the game state
  const [board, setBoard] = useState<BoardState>({
    squares: Array(9).fill(""),
    xIsNext: true,
  });

  // Function to handle click on a square
  const handleClick = (index: number): void => {
    const squares = [...board.squares];

    // If square is already filled or game is over, return
    if (calculateWinner(squares) || squares[index]) {
      return;
    }

    // Update the square with 'X' or 'O' based on the current player
    squares[index] = board.xIsNext ? 'X' : 'O';

    // Update the game board state
    setBoard({
      squares: squares,
      xIsNext: !board.xIsNext,
    });
  };

  // Function to determine the winner of the game
  const calculateWinner = (squares: Array<string>): string | null => {
    const lines = [
      [0, 1, 2],
      [3, 4, 5],
      [6, 7, 8],
      [0, 3, 6],
      [1, 4, 7],
      [2, 5, 8],
      [0, 4, 8],
      [2, 4, 6],
    ];

    for (let i = 0; i < lines.length; i++) {
      const [a, b, c] = lines[i];
      if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
        return squares[a];
      }
    }

    return null;
  };

  // Function to render the game board
  const renderSquare = (index: number): JSX.Element => {
    return (
      <button className="square" onClick={() => handleClick(index)}>
        {board.squares[index]}
      </button>
    );
  };

  // Render the game board
  return (
    <div className="game">
      <div className="board-row">
        {renderSquare(0)}
        {renderSquare(1)}
        {renderSquare(2)}
      </div>
      <div className="board-row">
        {renderSquare(3)}
        {renderSquare(4)}
        {renderSquare(5)}
      </div>
      <div className="board-row">
        {renderSquare(6)}
        {renderSquare(7)}
        {renderSquare(8)}
      </div>
    </div>
  );
};

export default Game;