import React from 'react';

// SquareProps type for Square component props
type SquareProps = {
  value: string;
  onClick: () => void;
};

// Square functional component to represent a single square in the game board
const Square: React.FC<SquareProps> = ({ value, onClick }) => {
  return (
    <button className="square" onClick={onClick}>
      {value}
    </button>
  );
};

export default Square;