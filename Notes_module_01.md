https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/master/

# 1 - Introduction

## 1.1 What is Machine Learning

- Essentially learning from data by extracting some statistical information

## 1.2 ML vs rules

- Rules based are easy to interpret but inflexible
- Rules can be used to generate features for ML system
- ML system is more flexible and dynamic

## 1.3 Supervised ML

- You need feature, target pairs
- Regression, classification, rankers

## 1.4 CRISP-DM

- Cross-industry standard process for data mining
    - Main pieces
        - Business understanding
        - Data understanding
        - Data preparation
        - Modeling
        - Deployment
    - A lot of reiteration

## 1.5 Model Selection

- Beware of multiple comparison problem
    - Checking many models on the same dataset, one of the models can just by chance get better results
    - Use Train, Val, and Test datasets, where Test dataset acts as a safeguard
    - Once model is selected, you can combine your train and val dataset, train the model again and then predict on test dataset, not to waste val dataset

## 1.6 Setting up environments

- Github codespaces is an amazing option which you can connect from anywhere, work on it using visual studio from the desktop version as well.

## 1.7 Introduction to numpy

- A quick overview but I knew everything already

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

## 1.10 Summary of module 1

- A quick summary of what has been done over the module 1

## 1.11 Homework

- [ ] Homework of the program
- [ ] Investigate more numpy with 3-5 projects from Claude to get deeper into it
- [ ] Investigate mroe pandas with 3-5 projects from Claude to get deepr into it


