# libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# fbref League One 2024-2025 League Table link
url_df = 'https://fbref.com/en/squads/dad7970b/Wrexham-Stats'

# Read and print data
df = pd.read_html(url_df)[0]
print (df)

