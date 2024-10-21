# libraries
import pandas as pd

# fbref League One 2024-2025 League Table link
url_df = 'https://fbref.com/en/comps/15/League-One-Stats'

# Read and get league table
df = pd.read_html(url_df)[0]
#print (df)

# Get list of teams from league table 
print("This is a list of data associated with League One: ") 
print(df.columns)

# Print the list of league one squads in curret league table order 
print(df.Squad)