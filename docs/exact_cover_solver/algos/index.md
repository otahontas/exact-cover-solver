Module exact_cover_solver.algos
===============================
Package for algorithms, defines interface for algorithm X implementations.

Sub-modules
-----------
* exact_cover_solver.algos.dlx

Classes
-------

`AlgorithmX()`
:   Abstract base class for algorithm X for solving the exact cover problem.
    
    Algorithm X is a straightforward recursive, nondeterministic, depth-first
    and backtracking algorithm, implemented usually with dancing links technique.

    ### Ancestors (in MRO)

    * abc.ABC

    ### Descendants

    * exact_cover_solver.algos.dlx.DLX

    ### Methods

    `solve(self, *args, **kwargs)`
    :   Concrete solving method that should be implemented by subclasses.