# Module 1

## 1.8 Linear algebra refresher

- In linear algebra, vectors are columns by default, while in numpy they are row vectors by default.
- Types of two vector multiplication:
    - Element wise multiplication (default in numpy) - gives a vector of the same size
    - Inner product (dot-product) - gives a single number
    - Outer product - gives a matrix, height defined by one vector, width defined by another vector
- Transpose
    - Convert a column vector to row vector or vice versa
- Matrix matrix multiplication
    - X times Y , what you do is that you perform essentially a lot of dot products; every row vector of X is dotted with the column vector of Y. The result of this dot product is assigned row index that of row vector used from X and the column index is used from the column vectors used from Y.
- Matrix inverse
    - A real number inverse is such a number that a times a_inverse = 1
    - Matrix inverse is analogous concept to that. Matrix times its inverse equal Identity matrix.
        - Note that inverse matrix does not always exist

## 1.9 Introduction to Pandas