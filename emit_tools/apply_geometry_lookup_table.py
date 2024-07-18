import numpy as np

from .constants import *

# Function to Apply the GLT to an array
def apply_GLT(swath_array: np.ndarray, GLT_one_based_array: np.ndarray, fill_value: int = FILL_VALUE, GLT_nodata_value: int = GLT_NODATA_VALUE) -> np.ndarray:
    """
    This function applies the geometry look-up table array from an EMIT dataset to a numpy array of an EMIT data variable of either 2 or 3 dimensions.

    Parameters:
    swath_array: numpy array of the desired EMIT hyperspectral variable
    GLT_one_based_array: a GLT array constructed from EMIT GLT data

    Returns:
    ortho_array: a numpy array of orthorectified data.
    """
    latitude_length = GLT_one_based_array.shape[0]
    longitude_length = GLT_one_based_array.shape[1]
    wavelength_length = swath_array.shape[-1]
    ortho_array_shape = (latitude_length, longitude_length, wavelength_length)

    # if this is a 2-dimensional image instead of a hyperspectral cube, then make the band dimension size 1
    if swath_array.ndim == 2:
        swath_array = swath_array[:, :, np.newaxis]
    
    # initialize orthorectified data array
    ortho_array = np.full(ortho_array_shape, fill_value, dtype=np.float32,)

    # create mask of valid indices
    valid_GLT = np.all(GLT_one_based_array != GLT_nodata_value, axis=-1)

    # make a copy of the one-based indices
    GLT_zero_based_array = GLT_one_based_array.copy()
    # decrement the one-based indices to zero-based indices for use with numpy 
    GLT_zero_based_array[valid_GLT] -= 1
    # query the one-based indices of 
    ortho_array[valid_GLT, :] = swath_array[GLT_zero_based_array[valid_GLT, 1], GLT_zero_based_array[valid_GLT, 0], :]

    return ortho_array
