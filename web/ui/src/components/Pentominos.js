import { Box, Button, HStack, Menu, MenuButton, MenuItem, MenuList, Text, VStack } from '@chakra-ui/react';
import React from 'react';
import apiService from '../utils/api';
import { ChevronDownIcon } from '@chakra-ui/icons';
import { Loader } from './Loader';

const PentominoRow = ({ row }) => {
  const colors = {
    'F': 'red.200',
    'I': 'red.800',
    'L': 'orange.400',
    'N': 'yellow.100',
    'P': 'green.300',
    'T': 'green.600',
    'U': 'teal.300',
    'V': 'blue.100',
    'W': 'blue.500',
    'X': 'cyan.200',
    'Y': 'purple.400',
    'Z': 'pink.200',
  };
  return (
    <HStack>
      {row.map(cell => (
        <Box id={cell}
             w='40px'
             h='40px'
             margin={0}
             padding={0}
             bg={colors[cell]}>
        </Box>
      ))}
    </HStack>
  );
};
const PentominoBoard = ({ grid }) => {
  return (
    <VStack>
      {grid.map(row => <PentominoRow id={row} row={row} />)}
    </VStack>
  );
};
const PentominoBoardBrowser = ({ boards }) => {
  const [boardIndex, setBoardIndex] = React.useState(0);
  if (!boards) return null;
  return (
    <Box margin={10}>
      <PentominoBoard grid={boards[boardIndex]} />
      <HStack spacing={5} margin={5}>
        <Button disabled={boardIndex === 0} colorScheme='teal' onClick={() => setBoardIndex(boardIndex - 1)}>
          Previous
        </Button>
        <Button disabled={boardIndex == boards.length - 1} colorScheme='teal'
                onClick={() => setBoardIndex(boardIndex + 1)}>
          Next
        </Button>
        <Text>Solution {boardIndex + 1} / {boards.length}</Text>
      </HStack>
    </Box>
  );
};
export const PentominoView = () => {
  const [boardStatus, setBoardStatus] = React.useState('idle');
  const [boardData, setBoardData] = React.useState(null);

  const startBoardLoading = async (size) => {
    setBoardStatus('loading');
    const [boardHeightStr, boardWidthStr] = size.split('x');
    const data = {
      height: parseInt(boardHeightStr),
      width: parseInt(boardWidthStr),
      algorithm: 'DLX',
    };
    const result = await apiService.solvePentomino(data);
    if (!result.ok) return;
    setBoardStatus('loaded');
    setBoardData(result.data.boards);
  };
  return (
    <Box>
      <Menu>
        <MenuButton as={Button} rightIcon={<ChevronDownIcon />}>
          Select pentomino board size
        </MenuButton>
        <MenuList>
          <MenuItem onClick={() => startBoardLoading('3x20')}>3x20</MenuItem>
          <MenuItem onClick={() => startBoardLoading('4x15')}>4x15</MenuItem>
          <MenuItem onClick={() => startBoardLoading('5x12')}>5x12</MenuItem>
          <MenuItem onClick={() => startBoardLoading('6x10')}>6x10</MenuItem>
        </MenuList>
      </Menu>
      <Box>
        {boardStatus === 'loaded'
          ? <PentominoBoardBrowser boards={boardData} />
          : <Loader status={boardStatus} />
        }
      </Box>
    </Box>
  );
};