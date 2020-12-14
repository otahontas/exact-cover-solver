import { Center, Spinner, Text } from '@chakra-ui/react';
import React from 'react';

export const Loader = ({ status }) => {
  switch (status) {
    case 'loading':
      return (
        <Center margin={5}>
          <Text>Calculating solutions, this might take some time.</Text>
          <Spinner />
        </Center>
      );
    default:
      return null;
  }
};