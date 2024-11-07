# libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def DisplayResults(t):
    print(t)
    titlestring = (t.Squad + " Results")
    dataValues = np.array([t.W, t.D, t.L])
    mylabels = ["Win", "Draw", "Loss"]
    dataColours = ["Green", "Yellow", "Red"]

    plt.pie(dataValues, labels = mylabels, colors=dataColours)
    plt.legend(title = titlestring)
    plt.show() 


# fbref League One 2024-2025 League Table link
url_df = 'https://fbref.com/en/comps/15/League-One-Stats'

# Read and get league table


df = pd.read_html(url_df)[0]
print (df)

# loop through the rows using iterrows()

# Get team at the top of the table
team = df.iloc[0]
DisplayResults(team)

# Get Wrexham from dataframe

#df.set_index('squad')
#wrexham = df.loc[df['Wrexham']]
#print(wrexham)
#DisplayResults(wrexham)
