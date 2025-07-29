import numpy as np
import pandas as pd
from typing import List
import copy

def knot_ceil(vector: np.array, knot: float) -> np.array:
    """
    Apply a ceiling value to elements in a numpy array.

    This function takes a numpy array and a ceiling value (knot). It returns a copy of the array where all elements greater than the ceiling value are replaced by the ceiling value.

    Parameters:
    vector (np.array): The input numpy array.
    knot (float): The ceiling value to apply.

    Returns:
    np.array: A new numpy array with elements capped at the ceiling value.
    
    Example:
    >>> import numpy as np
    >>> vector = np.array([1, 2, 3, 4, 5])
    >>> knot = 3
    >>> knot_ceil(vector, knot)
    array([1, 2, 3, 3, 3])
    """
    
    vector_copy = copy.deepcopy(vector)
    # vector_copy = vector.copy()
    vector_copy[vector_copy > knot] = knot
    return vector_copy


def lspline(series: pd.Series, knots: List[float]) -> np.array:
    """
    Generate a linear spline basis matrix for a given pandas Series and knots.

    This function creates a design matrix for linear splines based on the provided knots. 
    It iteratively applies a ceiling function to the series values at each knot, 
    subtracting the resulting column from the series to prepare for the next knot.

    Parameters:
    series (pd.Series): The input pandas Series.
    knots (List[float]): A list of knot values where the spline should change slope.

    Returns:
    np.array: A design matrix where each column corresponds to a segment of the linear spline.

    Example:
    >>> import pandas as pd
    >>> series = pd.Series([1, 2, 3, 4, 5])
    >>> knots = [2, 4]
    >>> lspline(series, knots)
    array([[1, 0, 0],
           [2, 0, 0],
           [2, 1, 0],
           [2, 2, 0],
           [2, 2, 1]])
    """
    
    if type(knots) != list:
        knots = [knots]
    design_matrix = None
    vector = series.values

    for i in range(len(knots)):
        if i == 0:
            column = knot_ceil(vector, knots[i])
        else:
            column = knot_ceil(vector, knots[i] - knots[i - 1])

        if i == 0:
            design_matrix = column
        else:
            design_matrix = np.column_stack((design_matrix, column))

        vector = vector - column
    design_matrix = np.column_stack((design_matrix, vector))

    return design_matrix