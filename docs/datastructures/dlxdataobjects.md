Module exact_cover_solver.datastructures.dlxdataobjects
=======================================================
Circular doubly linked list object definitions.

Classes
-------

`ColumnObject()`
:   Column object representing matrix columns.
    
    Set column size, link column object to itself.

    ### Ancestors (in MRO)

    * exact_cover_solver.datastructures.dlxdataobjects.DataObject

    ### Methods

    `attach(self)`
    :   Attach column object back to its original position in header list.

    `deattach(self)`
    :   Deattach column object from header list, but don't erase it from memory.

`DataObject(column, row=None)`
:   Data object representing 1s in matrix.
    
    Link data object to column object, optionally set row name.

    ### Descendants

    * exact_cover_solver.datastructures.dlxdataobjects.ColumnObject

    ### Methods

    `attach(self)`
    :   Attach data object back to its original position in linked list.

    `deattach(self)`
    :   Deattach data object from linked list, but don't erase it from memory.