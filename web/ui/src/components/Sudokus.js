import {
  Box,
  NumberInput,
  NumberInputField,
  HStack,
  Button,
  Text,
} from '@chakra-ui/react';
import React from 'react';
import apiService from '../utils/api';
import { Loader } from './Loader';

const SudokuRow = ({ solved, startIndex, rowElements, handleChange }) => {
  const cells = [];
  for (let i = 0; i < rowElements.length; i++) {
    const cellIndex = startIndex + i;
    cells.push(
      <Box key={cellIndex}>
        <NumberInput
          allowMouseWheel
          isReadOnly={solved}
          value={rowElements[i] === 0 ? '' : rowElements[i]}
          onChange={value => handleChange(cellIndex, value)}
        >
          <NumberInputField w="50px" h="50px" />
        </NumberInput>
      </Box>
    );
  }

  return <HStack spacing={0}>{cells}</HStack>;
};

function getInitialState(len) {
  let board = [];
  for (let i = 0; i < len * len; i++) {
    board.push(0);
  }
  return board;
}

const SudokuBoardBrowser = ({ boards, len }) => {
  const [boardIndex, setBoardIndex] = React.useState(0);
  if (!boards || boards.length === 0) return null;
  if (!boards) return null;
  const board = boards[boardIndex].flat();
  const rows = [];
  for (let i = 0; i < len * len; i += len) {
    const rowElements = board.slice(i, i + len);
    rows.push(
      <SudokuRow
        solved={true}
        key={`row_${i}`}
        startIndex={i}
        rowElements={rowElements}
      />
    );
  }
  return (
    <Box>
      {rows}
      <HStack spacing={5} margin={5}>
        <Button
          disabled={boardIndex === 0}
          colorScheme="teal"
          onClick={() => setBoardIndex(boardIndex - 1)}
        >
          Previous
        </Button>
        <Button
          disabled={boardIndex === boards.length - 1}
          colorScheme="teal"
          onClick={() => setBoardIndex(boardIndex + 1)}
        >
          Next
        </Button>
        <Text>
          Solution {boardIndex + 1} / {boards.length}
        </Text>
      </HStack>
    </Box>
  );
};

export const SudokuView = () => {
  const len = 9;
  const initialState = getInitialState(len);
  const [board, setBoard] = React.useState(initialState);
  const [boardStatus, setBoardStatus] = React.useState('idle');
  const [boards, setBoards] = React.useState([]);

  const preloadBoard = () => {
    const preset_boards = [
      [
        8,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        3,
        6,
        0,
        0,
        0,
        0,
        0,
        0,
        7,
        0,
        0,
        9,
        0,
        2,
        0,
        0,
        0,
        5,
        0,
        0,
        0,
        7,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        4,
        5,
        7,
        0,
        0,
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        3,
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        0,
        6,
        8,
        0,
        0,
        8,
        5,
        0,
        0,
        0,
        1,
        0,
        0,
        9,
        0,
        0,
        0,
        0,
        4,
        0,
        0,
      ],
      [
        1,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        2,
        0,
        2,
        0,
        0,
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        3,
        0,
        0,
        0,
        4,
        0,
        0,
        0,
        0,
        0,
        4,
        8,
        3,
        0,
        0,
        0,
        0,
        0,
        0,
        1,
        5,
        2,
        0,
        0,
        0,
        0,
        0,
        0,
        7,
        9,
        6,
        0,
        0,
        0,
        0,
        0,
        6,
        0,
        0,
        0,
        7,
        0,
        0,
        0,
        9,
        0,
        0,
        0,
        0,
        0,
        8,
        0,
        8,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        9,
      ],
    ];
    setBoard(preset_boards[Math.floor(Math.random() * preset_boards.length)]);
  };

  const getSolutionFromServer = async () => {
    setBoardStatus('loading');
    let boardInput = [];
    let row = [];
    for (let i = 0; i <= len * len; i++) {
      if (i !== 0 && i % len === 0) {
        boardInput.push(row);
        row = [];
      }
      if (i !== len * len) row.push(board[i]);
    }
    const data = {
      algorithm: 'DLX',
      sudoku_board: boardInput,
    };
    const result = await apiService.solveSudoku(data);
    if (!result.ok) return;
    setBoardStatus('solved');
    setBoards(result.data.boards);
  };

  const handleChange = (index, val) => {
    if (!Number.isInteger(parseInt(val))) return;
    const intVal = parseInt(val);
    if (intVal < 1 || intVal > len) return;
    const newBoard = board.map(cell => cell);
    newBoard[index] = intVal;
    setBoard(newBoard);
  };

  const rows = [];
  for (let i = 0; i < len * len; i += len) {
    const rowElements = board.slice(i, i + len);
    rows.push(
      <SudokuRow
        key={`row_${i}`}
        startIndex={i}
        rowElements={rowElements}
        handleChange={handleChange}
      />
    );
  }
  return (
    <Box>
      {boardStatus === 'solved' && (
        <SudokuBoardBrowser boards={boards} len={len} />
      )}
      {boardStatus === 'idle' && rows}
      {boardStatus === 'idle' && (
        <HStack spacing={5} margin={5}>
          <Button colorScheme="teal" onClick={() => getSolutionFromServer()}>
            Solve
          </Button>
          <Button colorScheme="teal" onClick={() => preloadBoard()}>
            Preload random sudoku
          </Button>
        </HStack>
      )}
      {boardStatus === 'loading' && <Loader status={boardStatus} />}
    </Box>
  );
};
