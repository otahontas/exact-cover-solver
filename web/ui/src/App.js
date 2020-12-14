import React from 'react';
import {
  Box,
  ChakraProvider,
  Container,
  HStack,
  theme,
  Button,
  Stack,
  Radio, 
  RadioGroup,
  Text
} from '@chakra-ui/react';
import { useState } from 'react';

const PentominoBoard = ({data}) => {
  return null;
}

const SudokuView = () => {
  return null;
}

const PentominoView = () => {
  const [value, setValue] = React.useState("1")
  return (
    <Box>
      <Text>Please select which pentomino board size to use</Text>
      <RadioGroup onChange={setValue} value={value}>
        <Stack direction="row">
          <Radio value="3x20">3x20</Radio>
          <Radio value="4x15">4x15</Radio>
          <Radio value="5x12">5x12</Radio>
          <Radio value="6x10">6x10</Radio>
        </Stack>
      </RadioGroup>
    </Box>
  )
}

const Content = ({page}) => {
  if (page === "pentomino") {
    return <PentominoView />
  }
  if (page === "sudoku") {
    return <p>Sudoku</p>
  }
  return null
}

function App() {
  const [page, setPage] = useState("")
  
  
  return (
    <ChakraProvider theme={theme}>
      <Container>
        <HStack spacing={8}>
          <Button colorScheme="teal" variant="outline" onClick={() => setPage("pentomino")}>
            Pentomino
          </Button>
          <Button colorScheme="teal" variant="outline" onClick={() => setPage("sudoku")}>
            Sudoku
          </Button>
        </HStack>
        <Content page={page} />
      </Container>
    </ChakraProvider>
  );
}

export default App;
