## Plan for Next.js Tic Tac Toe App using TypeScript

### Components to be created:
1. **GameBoard Component**: Responsible for rendering the game board and handling game logic.
2. **Square Component**: Represents each square on the game board.
3. **Status Component**: Displays the status of the game (e.g., player turn, winner).
4. **Button Component**: Button to start a new game.
5. **Layout Component**: Wraps all components and provides the overall layout of the app.
6. **Header Component**: Displays the header of the app.

### File Structure:
- **components/**
  - GameBoard.tsx
  - Square.tsx
  - Status.tsx
  - Button.tsx
  - Layout.tsx
  - Header.tsx
- **pages/**
  - index.tsx
- **styles/**
  - global.css

### Third Party Packages:
1. **Next.js**: Framework for building React applications.
   - Installation: `npx create-next-app@latest`
2. **TypeScript**: For static typing.
   - Installation: `npm install --save-dev typescript @types/react @types/node`
3. **Emotion**: For styling components with CSS-in-JS.
   - Installation: `npm install @emotion/react @emotion/styled`

By following this plan, we will have a well-structured Next.js Tic Tac Toe app using TypeScript, with separate components for different functionalities and a clear file structure for easy maintenance and scalability.