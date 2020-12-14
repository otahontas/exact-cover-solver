import React, { useState } from 'react';
import { Button, ChakraProvider, Container, HStack, theme } from '@chakra-ui/react';
import { PentominoView } from './components/Pentominos';

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
        <HStack spacing={5} margin={5}>
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
