"""Barcode matching utilities"""

import numpy as np
import Levenshtein


def find_closest_bc(bc, 
                    library, 
                    cutoff=1,
                    use_levenshtein=False):
    '''
    Finds the closest barcode using the Hamming distance metric. 
    If the closest matches have the same distance, it returns both.
    This function assumes the barcodes are all the same case.

    Parameters
    ----------
    bc
        Barcode to find closest match to using the library
    library
        pd.DataFrame object containing 'barcode' column and 'seq' column
    cutoff
        Maximum distance for finding closest match. Set to None to return distances
    use_levenshtein
        Whether to use the Levenshtein distance instead of Hamming
    '''

    if use_levenshtein:
        # Use Levenshtein distance
        distances = np.array([Levenshtein.distance(bc, x) for x in list(library['barcode'])])
    else:
        # Use Hamming distance
        distances = np.array([Levenshtein.hamming(bc, x) for x in list(library['barcode'])])
    if cutoff is not None:
        if sum(distances <= cutoff) != 0:
            return library.iloc[np.argwhere(distances <= cutoff)[:,0]]
        else:
            return None
    else:
        return distances
