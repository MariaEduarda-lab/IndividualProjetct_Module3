import numpy as np  # importing numpy

def calculate(list_input):  # creation of the function
   
    if len(list_input) != 9:  # conditional to check the number of elements for a 3x3 matrix
        raise ValueError("List must contain nine numbers.")
    

    matrix = np.array(list_input).reshape(3, 3)  # creation of a 3x3 matrix from the input list
    
    
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),  # mean along columns
            matrix.mean(axis=1).tolist(),  # mean along rows
            matrix.mean().item()           # overall mean (scalar)
        ],
        'variance': [
            matrix.var(axis=0).tolist(),   # variance along columns
            matrix.var(axis=1).tolist(),   # variance along rows
            matrix.var().item()            # overall variance
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),   # standard deviation along columns
            matrix.std(axis=1).tolist(),   # standard deviation along rows
            matrix.std().item()            # overall standard deviation
        ],
        'max': [
            matrix.max(axis=0).tolist(),   # maximum along columns
            matrix.max(axis=1).tolist(),   # maximum along rows
            matrix.max().item()            # overall maximum
        ],
        'min': [
            matrix.min(axis=0).tolist(),   # minimum along columns
            matrix.min(axis=1).tolist(),   # minimum along rows
            matrix.min().item()            # overall minimum
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),   # sum along columns
            matrix.sum(axis=1).tolist(),   # sum along rows
            matrix.sum().item()            # overall sum
        ]
    }
    
    return calculations