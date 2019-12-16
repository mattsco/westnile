# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE_MAGIC_CELL
# Automatically replaced inline charts by "no-op" charts
# %pylab inline
import matplotlib
matplotlib.use("Agg")

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
import dataiku
from dataiku import pandasutils as pdu
import pandas as pd

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read the dataset as a Pandas dataframe in memory
# Note: here, we only read the first 100K rows. Other sampling options are available
dataset_westnile_data_joined = dataiku.Dataset("westnile_data_joined")
df = dataset_westnile_data_joined.get_dataframe(limit=100000)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Recipe outputs
newoutpu = dataiku.Dataset("newOutpu")
newoutpu.write_with_schema(pandas_dataframe)