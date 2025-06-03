# EQUATIONS 

1. What is equation?

    an equation is a mathematical statement that shows two expressions are equal, indicated by an equals sign (=).

    example: 5 + 3 = 8

    Types of Equations: 
    
    1. Linear Equations: 
        
        These are equations where the highest power of the variable is 1. 
        They are represented by the general form 
                
                    ax + b = 0,
             
             where 'a' and 'b' are constants. When graphed, they form a straight line

        <img src = https://github.com/Pallavilathavadlamudi/GENAI/blob/main/STATISTICS/Assets/LinearEquation.png>

    2. Quadratic Equations: 
        
        These equations involve a variable raised to the power of 2. 
        They are typically written as 
        
                    ax² + bx + c = 0, 
            
            where 'a', 'b', and 'c' are constants
        
        <img src = https://github.com/Pallavilathavadlamudi/GENAI/blob/main/STATISTICS/Assets/QuadraticEquation.png>
  
    3. Cubic Equations: 
        
        These equations involve a variable raised to the power of 3 and 
        They are generally represented as 
            
                    ax³ + bx² + cx + d = 0
            
            where 'a', 'b', 'c' and 'd' are constants

        <img src = https://github.com/Pallavilathavadlamudi/GENAI/blob/main/STATISTICS/Assets/CubicEquation.png>

    4. Exponential Equations: 
    
        These equations involve exponential functions, 
        where the variable appears in the exponent 
                   
                    a^x = b

                f(x)=a(1+r)^{x}

            f(x)=	exponential growth function
            a	=	initial amount
            r	=	growth rate
            {x}	=	number of time intervals     

    <img src = https://github.com/Pallavilathavadlamudi/GENAI/blob/main/STATISTICS/Assets/ExponentialEquation.png>

# LINEARITY AND EXPONENTIALITY 

1. Linearity:

    Constant Rate of Change: A linear relationship has a constant rate of change, meaning the value increases or decreases by the same amount over each time period. 
        
        Example: A salary that increases by $1,000 every year is a linear increase. 
    
        Graph: A linear graph is a straight line. 
        
        Equation: y = mx + b, where 'm' is the constant rate of change (slope) and 'b' is the y-intercept

2. Exponentiality:

    An exponential relationship has a constant rate of percent change, meaning the value is multiplied by the same factor (e.g., 1.05 for a 5% increase) over each time period. 
        
        Example: Money in a savings account that earns 5% interest annually is an example of exponential growth. 
        
        Graph: An exponential graph is a curve. 
        
        Equation: y = a * b^x, where 'a' is the initial value and 'b' is the growth factor (base)


# Multiple Linear Equations

    A multiple linear equation is a mathematical representation of a relationship between a dependent variable and two or more independent variables.

    It's a statistical technique used to predict the outcome of a dependent variable by considering the combined influence of multiple factors.
    
    The outcome of the dependent variable is dependent on independent variable

    1. Difference between Linear Equation and multiple linear Equation?

    A linear equation involves variables raised to the power of one, while multiple linear equations incorporate two or more independent variables to predict a dependent variable

                y = b0 + b1x1 + b2x2 + ... + bnxn, 
                
            where y is the dependent variable, x1, x2, ... xn are the independent variables, 
            b0 is the y-intercept, and b1, b2, ... bn are the coefficients for each independent variable.


# Matrix 

1. Introduction to Matrices:

    Matrices are rectangular arrays of numbers, symbols, or characters where all of these elements are arranged in each row and column. 

    A matrix is identified by its order which is given in the form of rows ⨯ and columns and the location of each element is given by the row and column it belongs to.

    A matrix is represented as [P]m⨯n where P is the matrix, m is the number of rows and n is the number of columns. 

    Example: 

    <img src ="https://github.com/Pallavilathavadlamudi/GENAI/blob/main/STATISTICS/Assets/Examplematrix.png">    


2. Order of Matrix:

    The order of a matrix refers to its dimensions, i.e., the number of rows and columns. If a matrix has m rows and n columns, its order is     denoted as m × n.

    How to determine order of matrix?

    The order of the matrix is determined by the number of rows and columns present in the matrix. For example, if a matrix has "m" rows and "n" columns, then the order of the matrix is said to be "m × n."

    <img src = "https://github.com/Pallavilathavadlamudi/GENAI/blob/main/STATISTICS/Assets/Orderofmatrix.png">


3. Types of Matrix:

    1. Singleton matrix :

        A singleton matrix is defined as a matrix that has only one element, i.e., it has only one row and one column. So, the order of a singleton matrix is "1 × 1".

            eaxample : A=[23]

    2. Row matrix :

        A row matrix is defined as a matrix that has only one row. A matrix "A = [aij]" is said to be a row matrix if the order of the matrix is "1 × n".

    3. Column matrix: 

        A column matrix is defined as a matrix that has only one column. The matrix "A = [aij]" is said to be a column matrix if the order of the matrix is "m × 1".
        
    4. Rectangular matrix:

        A rectangular matrix is defined as a matrix that does not have an equal number of rows and columns. The order of a rectangular matrix that has "m" rows and "n" columns is "m × n". 

    5. Square matrix:

        A square matrix is defined as a matrix that has an equal number of rows and columns. The order of a square matrix that has "n" rows and "n" columns is "n × n".

    6. Zero or Null matrix:

        A matrix whose all elements are zero is called a Zero Matrix. A zero matrix is also called as Null Matrix.

    7. Diagonal matrix:

        A square matrix in which the non-diagonal elements are zero is called a Diagonal Matrix.

    8. Scalar matrix:

        A diagonal matrix with equal diagonal elements.

    9. Unit matrix:

        A diagonal matrix whose all diagonal elements are 1 is called a Unit Matrix. A unit matrix is also called an Identity matrix. An identity matrix is represented by 1. 

    10. Upper and Lower Triangular Matrix:

        Upper Triangular Matrix: A square matrix in which all the elements below the diagonal are zero is known as the upper triangular matrix.

        Lower Triangular Matrix: A square matrix in which all the elements above the diagonal are zero is known as the lower triangular matrix.

        <img src ="https://github.com/Pallavilathavadlamudi/GENAI/blob/main/STATISTICS/Assets/Typesofmatrix.png">
    
4. Matrix Operaions: 

    1. Addition:

        Adding matrices is as simple as adding numbers, 
        but there’s one important rule: the matrices must have the same order (i.e., the same number of rows and columns). Once this condition is met, the addition is performed by adding corresponding elements of both matrices to form a new matrix.

    <img src = "https://github.com/Pallavilathavadlamudi/GENAI/blob/main/STATISTICS/Assets/MatrixAddition.png">

        Commutative Law: A + B = B + A
        Associative Law: (A + B) + C = A + (B + C)
        Identity of Matrix: A + O = O + A = A, where O is a zero matrix, which is the Additive Identity of the Matrix
        Additive Inverse: A + (-A) = O = (-A) + A, where (-A) is obtained by changing the sign of every element of A, which is the additive inverse of the matrix.

    2. Subtraction:

        To subtract two matrices, the matrices must have the same order (i.e., the same number of rows and columns). Subtraction is performed by subtracting the corresponding elements of the second matrix from the first matrix to form a new matrix

    <img src = "https://github.com/Pallavilathavadlamudi/GENAI/blob/main/STATISTICS/Assets/MatrixSubtraction.png">

    3. Multiplication: 

        1. Scalar Multiplication:

        For any matrix A = [aij]m×n, if we multiply the matrix A by any scalar (say k), then the scalar is multiplied by each element of the matrix, and this is called the scalar multiplication of matrices.

    <img src = "https://github.com/Pallavilathavadlamudi/GENAI/blob/main/STATISTICS/Assets/ScalarMultiplication.png">

        2. Multiplication:

        Matrix multiplication is the operation that helps us multiply two matrices. 
        This is different from algebraic multiplication, and not all matrices can be multiplied.
            
                number of columns in first matrix = number of rows in second matrix

                            [A]m×n and [B]n×p

    <img src = "https://github.com/Pallavilathavadlamudi/GENAI/blob/main/STATISTICS/Assets/Multiplication.png">

    4. Transpose of a Matrix:

        The transpose operation of a matrix rearranges its rows into columns and its columns into rows. For a matrix A of order m×n, 
        denoted as A = [aij]m×n​, its transpose is represented by AT and is defined as:

                        T
                     (A) = [aji]n×m

    <img src = "https://github.com/Pallavilathavadlamudi/GENAI/blob/main/STATISTICS/Assets/Transpose.png">

        1. Symmetric Matrix:

            A square matrix is symmetric if its transpose is equal to itself.
            In other words, for all i and j, aij = aji.

        2. Asymmetric Matrix: 

            A square matrix is asymmetric if its elements are not equal across the main diagonal
            This means aij ≠ aji for at least one pair of indices (i, j).

    <img src = "https://github.com/Pallavilathavadlamudi/GENAI/blob/main/STATISTICS/Assets/Symmetric%26AsymmetricMatrix.jpg">    

    5. Determinant of a matrix: 
        
        The determinant of a Matrix is defined as a special number that is defined only for square matrices (matrices that have the same number of rows and columns). 
   
    <img src = "https://github.com/Pallavilathavadlamudi/GENAI/blob/main/STATISTICS/Assets/DeterminantofMatrix.png">

    6. Inverse of Matrix:

        The inverse of a matrix is similar to the reciprocal of a number.

                                                          −1
        For a square matrix A, the inverse is denoted as A   , and it satisfies:

                       −1    −1
                    A⋅A   = A  ⋅A = I

    Where I is the identity matrix (like 1 in regular multiplication).     

    <img src = "https://github.com/Pallavilathavadlamudi/GENAI/blob/main/STATISTICS/Assets/Inverseofmatrix.png">

    7. Negative of a Matrix:

        The negative of a matrix is simply a matrix where each element is the additive inverse (i.e., the negative) of the corresponding element in the original matrix.

                A=[aij] Then - A=[-aij]

    <img src = "https://github.com/Pallavilathavadlamudi/GENAI/blob/main/STATISTICS/Assets/Negativematrix.png">

# Optimization

    Optimization is the process of finding the best solution from all possible solutions, usually by maximizing or minimizing a certain value (called an objective function), under constraints.

    Optimization = Best Choice + Conditions

        1. Discrete Optimization :
                
                The variables can only take values from a countable set (usually integers, permutations, or graphs).
                These problems are typically combinatorial in nature.

        2. Continuous Optimization :

                The variables can take values from a continuous range (real numbers).
                The solution lies in a real-valued space, often involving calculus or convex analysis.

# Vectors

1. Vector: 
       
    A vector is a quantity that has both magnitude and direction.

    Example : Velocity of a Car
            
        A car moving at 60 km/h to the north is a vector.
            
        Why? Because it has:
               
        Magnitude: 60 km/h
        Direction: North.

2. Vector Space: 

    A vector space is a collection of vectors that:

    Can be added together
    Can be scaled by numbers (called scalars)


        Example : 1. Images (Grayscale or Color)

            A digital image can be viewed as a vector of pixel values.
    
            An image with 100 pixels is a point in 100-dimensional space!
    
            Vector space: All possible grayscale images of a fixed size.
    
                ✅ Why it’s a vector space:

                You can add two images (blend them)
                You can scale an image (adjust brightness)

3. Calculating Angles between vectors:

    <img src = "https://github.com/Pallavilathavadlamudi/GENAI/blob/main/STATISTICS/Assets/Anglesbetweenvectors.png">

