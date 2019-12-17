# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
unseen_scored = dataiku.Dataset("unseen_scored")
unseen_scored_df = unseen_scored.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

score_df = unseen_scored_df # For this sample code, simply copy input to output


# Write recipe outputs
score = dataiku.Dataset("score")
score.write_with_schema(score_df)
