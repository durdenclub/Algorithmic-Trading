import pandas as pd

df = pd.read_csv('C:\\Users\\anton\PycharmProjects\OrderBookk\Dataa.csv')

df2 = df['start'] = df.bids.str.split(',').str.get(1)
df4 = df['Bids'] = df.bids.str.split(',').str.get(0)
df3 = df['Sas'] = df.asks.str.split(',').str.get(1)
df5 = df['Asks'] = df.asks.str.split(',').str.get(0)

df6 = df2['Amount_Bids'] = df2.str.split(':').str.get(1)
df7 = df4['Price'] = df4.str.split(':').str.get(1)



df8 = (df6 + df7)
df8 = df8.reset_index()
df8.columns = ['Leader', 'Time' ]


print (df8)

