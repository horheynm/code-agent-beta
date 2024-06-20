import React, { useState } from 'react';
import Square from './Square';

// Interface for the GameBoard component props
interface GameBoardProps {
  // Define props here if needed
}

const GameBoard: React.FC<GameBoardProps> = () => {
  // State to keep track of the squares' values
  const [squares, setSquares] = useState(Array(9).fill(null));

  // Function to handle click on a square
  const handleSquareClick = (index: number) => {
    // Logic to handle square click
  };

  return (
    <div className="game-board">
      <div className="board-row">
        <Square value={squares[0]} onClick={() => handleSquareClick(0)} />
        <Square value={squares[1]} onClick={() => handleSquareClick(1)} />
        <Square value={squares[2]} onClick={() => handleSquareClick(2)} />
      </div>
      <div className="board-row">
        <Square value={squares[3]} onClick={() => handleSquareClick(3)} />
        <Square value={squares[4]} onClick={() => handleSquareClick(4)} />
        <Square value={squares[5]} onClick={() => handleSquareClick(5)} />
      </div>
      <div className="board-row">
        <Square value={squares[6]} onClick={() => handleSquareClick(6)} />
        <Square value={squares[7]} onClick={() => handleSquareClick(7)} />
        <Square value={squares[8]} onClick={() => handleSquareClick(8)} />
      </div>
    </div>
  );
};

export default GameBoard;