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

- There are many options to create a dataframe:
    - Provide a list of lists as data. The inner lists contain information per one sample/instance. To have column names, provide them as a list of column names.
        - ```df = pd.DataFrame(data=data, columns=columns) ```
    - Provide a list of dictionaries, where each dictionary is structured like {col_name_1: value_1, col_name2,: value_2}

- Every column in a dataframe is pandas.Series object. I.e. dataframe is a table that contains multiple series objects.
- To access a column, we can use a dot notation when the column name does not have spaces. You can always use dictionary like access.
- To select several columns, pass a list of column names:
    - ```df[['name_1','name_3','name_8']]```
- To access elements etc. in the DataFrame, you can use:
    - .loc[row_name, column_name]
        - Note that row_name often matches the row_index. By default, the row_name is is an integer that matches the row_index. Same for column names
    - .iloc[row_index, column_index]
        - Accessing by indexes, like a nubmpy array essentially
    - To get multiple rows/columns, pass a list
        - ```df.iloc[[0,1],[0]]```
    - To get every other row, and columns 0 and 1
        - ```df.iloc[0:10:2, [0,1]]```
- To replace index, one option is:
    - ```df.index = ['id1','id2','id3','id4']```
        - Now use 'id1' etc in .loc[]
        - The behaviour of .iloc[] is unchanged
    - To go back to positional index
        - ```df.reset_index()```
        - Note that the previous index will be kept in the dataframe as a column
- Masking in dataframe/series:
    - This creates a mask: ```df['Year'] >= 2015``` (returns a binary series)
    - We can filter it by ```df[df['Year'] >= 2015]```
    - To combine masks:
        ```
        df[
            (df['Make'] == 'Nissan') & (df['Year']>=2015)
        ]
        ```
- String operations
    - ```df['Make'].str.lower()```
        - Note that need to use .str first to use string operations
    - ```df['Make'].str.replace(' ','_')```

- Many of the dataframe methods are not in place but return a modified dataframe
- Summarizing operations
    - ```df['MSRP'].max()```
    - ```df['MSRP'].describe()```
        - Gives general statistical info
    - ```df.describe()```
        - Gives general statical info of all the numerical columns
    - ```df['Make'].nunique()```
    - ```df.nunique()```
    - ```df.isnull()```
    - ```df.isnull().sum()```
- Grouping
    - Can be useful when we want say to have the average price per car make
    - ```df.groupby("Make")['Price'].mean()```
- Converting dataframe to dictionary
    - ```df.to_dict(orient='record')```
        - gives a list of dictionaries, one dictionary per one record
        - without orient, it defaults to giving a dictionary as {column_name_1: {index_1:value, index_2:value}} 




