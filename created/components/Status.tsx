import React from 'react';

// Status component to display the game status
const Status: React.FC<{ status: string }> = ({ status }) => {
  return (
    <div>
      <p>{status}</p>
    </div>
  );
};

export default Status;