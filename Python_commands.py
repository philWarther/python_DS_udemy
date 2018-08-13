# python_commands

import numpy as np


# Indexing arrays lecture 9
    Define and array:       arr = np.arange(0,11)
    Call a single entry:    arr[8]
    Slice of an array:      arr[0:5] retrieves [0,1,2,3,4]
                            arr[2: ] retrieves 2 - end
                            arr[: 4] retrieves beginning - 3    
    Copy and array          new_array = arr.copy
    2d array                arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
    Call an entry           arr_2d[1][2]  = 6  -- row 1, column 2
                            arr-2d[1,2]
    size of an array        arr_2d.shape[0]     Number of rows
                            arr_2d.shape[1]     Number of columns
    Transpose of an array   arr_2d.T
                            arr_2d.swapaxes(0,1)
    dot product             np.dot(arr1,arr2)
    element-wise mult       arr1*arr2
    add arrays              np.add(arr1,arr2)
    square root             np.sqrt(arr1)

    element-wise max 
    between two arrays      np.maximum(A,B)

    random normal           A = np.random.randn(dimension)


# Condition List

    for arrays x and y, and boolean condition we can create the array which 
    picks between arrays dependent on the condition:

        array = [(x if condition else y) for x,y,condition in zip(x,y,condition)]

    or we can use

        np.where(condition,x,y)

# Matplot lib basics

    import matplot.lib.pyplot as plt
    % matplotlib inline

    domain = np.arange(x_0,x_n,no_of_steps)
    dx,dy = np.meshgrid(domain,domain)
    z = f(dx,dy)

    plt.imshow(z)
    plt.colorbar()
    plt.title('title')

# Basic stat info for array A

    column sum              A.sum(0)
    row sum                 A.sum(1)
    n-dim sum               A.sum(dim)
    average                 A.mean(dim)
    standard deviation      A.std(dim)
    variance                A.var(dim)

# Boolean array stuff
    True for any instances of true      Bo.any()
    True only if all are true           Bo.True()

# List uniquness/check
    list = ['a','b','c','d','d']

    Return list of unique values    np.unique(list) = ['a','b','c','d']

    Check if values of a new list
    are contained in another        np.in1d(['a','e','b']) = [True, False, True]

# Saving arrays (lecture 13)