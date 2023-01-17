Fieldwork Model Triangulation Step
==================================

MAP Client plugin for discretising a fieldwork surface model into a triangulated mesh.

Requires
--------
None

Inputs
------
- **fieldworkmodel** [GIAS3 GeometricField instance] : The Fieldwork mesh to be discretised.

Outputs
-------
- **pointclouds** [list] : A list of discretised vertex coordinates.
- **faces** [list] : A list of the discretised vertex indices of each face.

Configuration
-------------
- **identifier** : Unique name for the step.
- **discretisation**:  How densely the input mesh is to be sampled when evaluating the vertices within each mesh element. Should of the format "d1, d2" where d1 and d2 are the discretisation for each element in each element coordinate direction. E.g. 5,5 means each 2-D quadralateral element will be discretised into 25 vertices.

Usage
-----
This step is used to produce a polygon mesh from a Fieldwork mesh, typically to be written to file (see Polygon Serialiser Step). A Fieldwork mesh is a piece-wise parametric mesh composed of an ensemble of elements interpolated by Lagrange polynomials. For the mesh to be useful for other applications, it is usually necessary to discretise it into a triangulated surface.

While the size and number of triangles produced is not directly definable, it is directly affected by the **discretisation** parameter. Generally, the higher the discretisation factors, the smaller and more numerous the triangles. Note that the size of each triangle is influenced by the size of the element it is in, and the discretisation factor. If a mesh has elements of very difference sizes, for any given discretisation, there will be very difference sizes of triangles produced.

