Module exact_cover_solver.datastructures.dlxmatrix
==================================================
Wrappers to represent dancing links data and column objects as matrix.

Classes
-------

`DLXMatrix(universe, set_collection)`
:   Matrix representation and initialization methods for circular linked lists.
    
    Create column and data objects and link them to this matrix object.

    ### Methods

    `create_columns(self, universe)`
    :   Create column columns and attach them to root.

    `create_nodes(self, set_collection)`
    :   Create nodes representing elements in each set in set collection.
        
        All sets are iterated through. For each element in set the element is
        linked to the correct column and columns column. Elements in set are
        also linked together to form a circular row.