import pandas as pd

fac_pd = pd.read_csv('faculty.csv')

fac_pd[' email'].to_csv('emails.csv', index=False)
