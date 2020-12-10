"""Types that are used in different packages inside the program.

Types used:
- UniverseElement: A single, unique element of universe. Could be any sort of object
  that can exist inside a mathematical set, e.g. int 1, tuple (1,2) or str "Cheese".
- Universe: A collection of universe elements.
- SubsetName: Name of the subset, should uniquely identify subset from other subsets.
  Name should be immutable and hence hashable.
- Subset: A collection of universe elements.
- SubsetCollection: A collection of subsets.
- Solution: List of SubsetNames that identify which disjoint subsets were picked to
  solution.
- ProblemData: Data needed to create an exact cover problem matrix.
"""

from typing import Dict, List, Tuple, TypeVar, Hashable

UniverseElement = TypeVar("UniverseElement")
Universe = List[UniverseElement]
SubsetName = TypeVar("SubsetName", bound=Hashable)
Subset = Dict[SubsetName, List[UniverseElement]]
SubsetCollection = List[Subset]
Solution = List[SubsetName]
ProblemData = Tuple[Universe, SubsetCollection]
