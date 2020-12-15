import { create } from 'apisauce';

const api = create({
  baseURL: '/solve',
});

const solvePentomino = async data => {
  console.log(data);
  return await api.post('pentomino', data);
};
const solveSudoku = async data => {
  return await api.post('sudoku', data);
};

export default { solvePentomino, solveSudoku };
