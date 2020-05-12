# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
test = dataiku.Folder("c0XvFbSC")
test_info = test.get_info()


# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.

rez_df = ... # Compute a Pandas dataframe to write into rez


# Write recipe outputs
rez = dataiku.Dataset("rez")
rez.write_with_schema(rez_df)
