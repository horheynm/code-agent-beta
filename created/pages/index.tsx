import React from 'react';

// Import components
import GameBoard from '../components/GameBoard';
import Status from '../components/Status';

const Home = () => {
  return (
    <div>
      <h1>Next.js Tic Tac Toe</h1>
      <GameBoard />
      <Status />
    </div>
  );
};

export default Home;