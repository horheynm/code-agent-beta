```bash
#!/bin/bash

# Create a new react-app from scratch
npx create-react-app project1

# Move into the project directory
cd project1

# Download all relevant packages
npm install @mui/material @emotion/react @emotion/styled

# Create component folders
mkdir src/components
mkdir src/components/Game
mkdir src/components/Board
mkdir src/components/Square

# Create Game component file
touch src/components/Game/Game.js

# Create Board component file
touch src/components/Board/Board.js

# Create Square component file
touch src/components/Square/Square.js

# Add code for Game component
echo 'import React from "react";

function Game() {
  return (
    <div>
      {/* Game component code here */}
    </div>
  );
}

export default Game;' > src/components/Game/Game.js

# Add code for Board component
echo 'import React from "react";

function Board() {
  return (
    <div>
      {/* Board component code here */}
    </div>
  );
}

export default Board;' > src/components/Board/Board.js

# Add code for Square component
echo 'import React from "react";

function Square() {
  return (
    <button>
      {/* Square component code here */}
    </button>
  );
}

export default Square;' > src/components/Square/Square.js

# Update App.js to include Game component
sed -i 's+import logo from "./logo.svg";+import Game from "./components/Game/Game";+' src/App.js
sed -i 's+<header className="App-header">+<header className="App-header">\n      <Game />\n+' src/App.js
```