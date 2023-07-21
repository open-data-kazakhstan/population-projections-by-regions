import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file = 'archive/kazpop.csv'
df_1 = pd.read_csv(file)

file2 = 'data/csv_final.csv'
df_2 = pd.read_csv(file2)
df_2 = df_2.loc[df_2['Год'] > 2023]

df = pd.concat([df_1,df_2])

df['Население'] = df['Население'].fillna(0).astype('int')
df = df.replace(to_replace='Северо-Казахстанская', value='СКО')
df = df.replace(to_replace='Западно-Казахстанская', value='ЗКО')
df = df.replace(to_replace='Восточно-Казахстанская', value='ВКО')
df = df.replace(to_replace='г. Астана', value='Астана')
df = df.replace(to_replace='г. Алматы', value='Алматы')
df = df.replace(to_replace='г. Шымкент', value='Шымкент')
df = df.replace(to_replace='Туркестанская 1', value='Туркестанская')
df = df.replace(to_replace='СевероКазахстанская', value='СКО')
df = df.replace(to_replace='ЗападноКазахстанская', value='ЗКО')
df = df.replace(to_replace='ВосточноКазахстанская', value='ВКО')

def ml_new_regions(region_to_test, region_predict):
    df_vko = df.loc[df['Область'] == region_to_test]
    df_vko = df_vko.loc[df_vko['Год'] < 2022]
    values = df_vko['Население'].values.tolist()
    k = 0
    c = 0
    for i in range(1, len(values)-1):
        x_avg_1 = 0
        y_avg_1 = 0
        for k in range(0,i+1):
            x_avg_1 = (x_avg_1 + values[k])/i+1
            y_avg_1 = (y_avg_1 + values[k+1])/i+1
        k = (values[i]-x_avg_1)*(values[i+1]-y_avg_1)/((values[i]-x_avg_1))**2 + k
        c = y_avg_1 - ((values[i]-x_avg_1)*(values[i+1]-y_avg_1)/((values[i]-x_avg_1))**2)*x_avg_1 + c
    k_final = k/(len(values)-1)
    c_final = c/(len(values)-1)
    list_res = []
    list_yrs = []
    x = df.loc[(df['Область'] == region_predict) & (df['Год'] == 2022), 'Население'].item()
    for i in range (2024, 2051):
        y = x*k_final + c_final
        list_res.append(y)
        x = y
        list_yrs.append(i)
    kval = 0
    for i in list_yrs:
        df['Население'] = np.where((df['Область'] == region_predict) & (df['Год'] == i), list_res[kval], df['Население'])
        kval = kval +1

ml_new_regions(region_predict='Абай', region_to_test='ВКО')
ml_new_regions(region_predict='Ұлытау', region_to_test='Карагандинская')
ml_new_regions(region_predict='Жетісу', region_to_test='Алматинская')

df_final = df[0:0]
regions = []
for i in df['Область']:
    if i not in regions:
        regions.append(i)
for i in regions:
    df_1 = df.loc[df['Область'] == i]
    df_1 = df_1.reset_index()
    df_1.index = df_1.index*10
    last_idx = df_1.index[-1] + 1
    df_expanded = df_1.reindex(range(last_idx))
    df_expanded['Год'] = df_expanded['Год'].fillna(method='ffill')
    df_expanded['Область'] = df_expanded['Область'].fillna(method='ffill')
    df_expanded = df_expanded.interpolate()
    df_final = pd.concat([df_final, df_expanded])

df1 = df_final
li = []
ranks = []
df1 = df1.sort_values(by=['Год', 'Область', 'Население'], ascending=[True, True, True])
for i in df1['Область']:
    if i not in li:
        ranks.append(1)
        li.append(i)
    else:
        x = 1
        for k in li:
            if k == i:
                x = x +1
        ranks.append(x)
        li.append(i)
df1['ranks'] = ranks

df1['Население'] = df1['Население'].fillna(0).astype('int')
df1['Год'] = df1['Год'].fillna(0).astype('int')
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(15,8))
df1.to_csv('data/rsl1.csv')