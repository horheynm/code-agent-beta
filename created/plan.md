## Plan for Next.js Tic Tac Toe App using Typescript

### Components:
1. Game board component: Responsible for rendering the tic tac toe grid and handling game logic.
2. Square component: Represents each square in the tic tac toe grid.
3. Status component: Displays the status of the game (e.g., winner, current player).
4. Button component: Restart the game.

### File Structure:
- components/
  - GameBoard.tsx
  - Square.tsx
  - Status.tsx
  - Button.tsx
- pages/
  - index.tsx

### Third Party Packages:
1. Next.js: A React framework for building server-side rendered applications.
   - Installation: `npx create-next-app@latest`
2. TypeScript: Adds static typing to JavaScript to improve code quality and developer productivity.
   - Installation: `npm install --save-dev typescript @types/react @types/node`
3. Material-UI: UI components library for React.
   - Installation: `npm install @mui/material @emotion/react @emotion/styled`

By following this plan, we can create a Next.js Tic Tac Toe app using TypeScript with a clear separation of components and a modern UI using Material-UI for a better user experience.