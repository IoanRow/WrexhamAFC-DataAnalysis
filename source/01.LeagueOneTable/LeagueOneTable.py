# libraries
import pandas as pd
import matplotlib.pyplot as plt


# fbref League One 2024-2025 League Table link
url_df = 'https://fbref.com/en/comps/15/League-One-Stats'

# Read and get league table
df = pd.read_html(url_df)[0]

print (df)


# Get list of teams from league table 
print("This is a list of data associated with League One: ") 
print(df.columns)


print(df.index[0])

# loop through the rows using iterrows()
team = df.iloc[1]

labels = 'Wins', 'Draws', 'Losses'
sizes = [team.W , team.D , team.L]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels)

