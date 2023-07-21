import pandas as pd
import numpy as np

# Read the initial Excel
excel = 'archive/source.xlsx'
df = pd.read_excel(excel)
df.columns = df.columns.astype(str)
pd.set_option('display.max_columns', None)

# Unpivot the Excel data for CSV export
df_unpivot = pd.melt(df, id_vars='Unnamed: 0', value_vars=['2000', '2001', '2002', '2003', '2004', '2005', '2006',
                                                           '2007', '2008', '2009', '2010', '2011', '2012', '2013',
                                                           '2014', '2015', '2016', '2017', '2018', '2019', '2020',
                                                           '2021', '2022', '2023'])
df_unpivot.rename(columns={"Unnamed: 0": "Область", "variable": "Год", "value": "Население"}, inplace=True)
df_unpivot.replace("-", np.nan, inplace=True)
df_unpivot.dropna(axis=0, inplace=True)
df_unpivot = df_unpivot.applymap(lambda x: int(x) if isinstance(x, str) and x.isdigit() else x)


print(df_unpivot)

data_types = df_unpivot.dtypes
print(data_types)

# Export to kazpop.csv
df_unpivot.to_csv('archive/kazpop.csv', index=False)


