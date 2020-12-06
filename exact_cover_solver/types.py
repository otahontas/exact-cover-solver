"""Types that are used in different packages inside the program.

Types used:
- UniverseElement: A single, unique element of universe. Could be any sort of object
  that can exist inside a mathematical set, e.g. 1, (1,2), "Cheese".
- Universe: A collection of elements in some universe. Exact cover is a collection of
  subsets, where each element of the universe is contained in exactly one subset.
- SubsetName: Name of the subset, e.g. some number id, like 1 or some string id, like
  "r3c4#9".
- Subset: A collection of universe elements. Collection should have a unique name and
  list of unique elements.
- SubsetCollection: A collection of subsets.
- Solution: List of SubsetNames that identify which disjoint subsets were picked to
  solution.
- ProblemData: Data needed to solve an exact cover problem.
"""
#
from typing import List, Tuple, TypeVar, Union

UniverseElement = TypeVar("UniverseElement")
Universe = List[UniverseElement]
SubsetName = Union[int, str]
Subset = List[UniverseElement]
SubsetCollection = List[Subset]
Solution = List[SubsetName]
ProblemData = Tuple[Universe, SubsetCollection]
