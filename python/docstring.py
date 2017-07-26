"""
This example for making documentation using pydoc. 
Run the following.

    pydoc -w docstring

"""

# coding: utf-8
import pandas as pd
import json
import numpy


def test(para1, para2, name):
    """
    A function for testing

    Parameters
    ----------
    para1 : DataFrame
       This is a joined dataframe with 5 columns.
    para2 : Column Name
       Column name of ID
    name : String
       Your name 

    Returns
    -------
    geojson : dict
    """
    helloworld = name

    return helloworld

def main(para):
    """ 
    Main Function
    """

    print (test(False, False, para))

if __name__ == '__main__':
    main("hello world")
