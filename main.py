import pandas as pd
import numpy as np

# # import pandas_datareader.data as web
# import matplotlib.pyplot as plt
# from matplotlib import style
#
# style.use('ggplot')
# web_stats = {
#     'Day': [1, 2, 3, 4, 5, 6],
#     'Visitors': [23, 43, 31, 45, 64, 48],
#     'Bounce_Rate': [34, 54, 32, 12, 32, 65]
# }
#
# df = pd.DataFrame(web_stats)
#
# print(df.set_index('Day'))
# # print(df.set_index('Day', inplace=True))
# # print(df)
# # print(df['Visitors'])
# # print(df.Visitors)
# # print(df.Visitors.tolist())
# #print(np.array(df[['Visitors', 'Bounce_Rate']]))
# --------------------------------------------------------------------

df1 = pd.DataFrame({'HPI': [80, 85, 88, 85],
                    'Int_rate': [2, 3, 2, 2],
                    'US_GDP_Thousands': [50, 55, 65, 55]},
                   index=[2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'HPI': [80, 85, 88, 85],
                    'Int_rate': [2, 3, 2, 2],
                    'US_GDP_Thousands': [50, 55, 65, 55]},
                   index=[2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'HPI': [80, 85, 88, 85],
                    'Unemployment': [7, 6, 5, 8],
                    'Low_tier_HPI': [50, 52, 50, 53]},
                   index=[2001, 2002, 2003, 2004])

concat = pd.concat([df1, df2, df3])
df4 = df1.append(df3)

print(df4)









