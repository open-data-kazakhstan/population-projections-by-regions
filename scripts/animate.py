import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

file = 'rsl1.csv'
df = pd.read_csv(file)
print(df)

df['Население'] = df['Население'].fillna(0).astype('int')
df['Год'] = df['Год'].fillna(0).astype('int')
print(df.dtypes)
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(9,16))

def animate(ranks):
    ax.clear()
    filtered = df[df['ranks'] == ranks]
    filt_areas = filtered[filtered['Область'] != 'Республика Казахстан '].sort_values('Население')
    filt_areas.drop(filt_areas[filt_areas['Население'] == 0].index, inplace = True)
    plot = plt.barh(y=filt_areas['Область'], width=filt_areas['Население'], color='#E6825D')

    ax.set_xlim(0, 3_500_000)
    ax.bar_label(plot, padding=3, labels=[f'{round(value,-3):,}' for value in filt_areas['Население']])

    for edge in ['top', 'right', 'bottom', 'left']:
        ax.spines[edge].set_visible(False)
    x = filtered.loc[filtered['Область'] == 'Республика Казахстан ', 'Население'].item()
    y = filtered.loc[filtered['Область'] == 'Республика Казахстан ', 'Год'].item()
    ax.tick_params(left = False)
    ax.get_xaxis().set_visible(False)
    ax.set_title(f'''Популяция Казахстана на {y} год 
{round(x,-3):,}''', size=18, weight='bold')    
plt.rcParams['text.color'] = 'white'
plt.rcParams['axes.labelcolor'] = 'white'
plt.rcParams['xtick.color'] = 'white'
plt.rcParams['ytick.color'] = 'white'

animation = FuncAnimation(fig, animate, frames=range(df['ranks'].min(), df['ranks'].max() +1), interval = 25) # Change interval if you want to change the speed
#animation.save('testv1.gif', dpi=100, writer=PillowWriter(fps=100)) # Script for saving
plt.show()

