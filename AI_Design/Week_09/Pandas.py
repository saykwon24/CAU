"""
Pandas: fundamental library for data science together with NumPy
        functions of Pandas: data loading, cleaning, manipulation, analysis, and visualization(with Matplotlib)
        two fundamental data structures: Series and DataFrame
    
    1) Series    | 1-D sequence of homogeneous elements; essentially 'column'
                   [syntax] empty Series    | <Series Object> = pandas.Series()
                            nonempty Series | <Series Object> = pandas.Series(data, index = idx)
                    
    2) DataFrame | 2-D arrays designed as tables, and each column is Series (collection of Series)
                   potentially columns are different types: list, dict, Series, NumPy ndarray, and so on
                   size is mutable
                   labeled axes: rows and columns
                   can perform arithmetic operations (on row and columns)
                   [syntax] pandas.DataFrame(data, index, columns, dtype, copy)


Series Object Attributes
    Series.index     | returns index of Series
    Series.values    | returns ndarray
    Series.dtype     | returns dtype object of underlying data
    Series.shape     | returns tuple of the shape of underlying data
    Series.nbytes    | returns number of bytes of underlying data
    Series.ndim      | returns the number of dimension
    Series.size      | returns number of elements
    Series.intemsize | returns the size of the dtype
    Series.hasnans   | returns True if there are any NaN
    Series.empty     | returns True if Series object is empty


Difference between Numpy array and Sereis object
    1) Vector operation
        NumPy ndarray: vector operation is possible against similar shape, otherwise raise an Error
        Series object: will be aligned only with matching index, otherwise NaN will be returned
    2) Index
        NumPy ndarray: starts from 0 and always numeric
        Series object: not necessarily starts from 0 and can be any type
"""

import pandas as pd


## 1) Series
# Nonempty Series
ob1 = pd.Series(range(5))
ob2 = pd.Series([3, 5, 4, 4.5])
ob3 = pd.Series({'Jan':31, 'Feb':28, 'Mar':31})

# Series with scalar value
ob4 = pd.Series(10, index=range(0, 3))
ob5 = pd.Series(15, index=range(1, 6, 2))
ob6 = pd.Series('Welcome to BBK', index=['Hema', 'Rahul', 'Anup'])

print(ob1, ob2, ob3, ob4, ob5, ob6, sep='\n')


## 2) DataFrame
# Create a DataFrame
data = {'apples':[3,2,1,0], 'oranges':[0,3,7,2]}
df = pd.DataFrame(data, index=['Ahmad', 'Ali', 'Rashed', 'Hamza'])
print(df)

# pandas.DataFrame.from_dict
data = {'col_1':[3,2,1,0], 'col_2':['a', 'b', 'c', 'd']}
pd.DataFrame.from_dict(data)
pd.DataFrame.from_dict(data, orient='index')
pd.DataFrame.from_dict(data, orient='index', index=['A', 'B', 'C', 'D'])

# Viewing the data
df.head(2)    # default = first 5 rows
df.tail(2)    # default = last 5 rows

# Loading dataset
df = pd.read_csv('dataset.csv')
df = pd.read_json('dataset.json')