# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 13:47:38 2020

@author: Romain Pic
"""

def SVR(X,Y,auto=True,*params):
    """
    Parameters
    ----------
    X : numpy array
        Numeric variables and their values.
    Y : numpy array
        Target variable.
    auto : boolean, optional
        True if no parameters where specified
        False if parameters specified. The default is True.
    *params : numerical parameters
        parameters if the user specifies them.

    Returns
    -------
    None.

    """
    
    if !auto:
        []=list(params)
        
    else:
        
        return model