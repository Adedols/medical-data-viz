import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = ((df.weight/ ((df.height/100)**2)) >25).astype(int)

# 3
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['id', 'age', 'sex', 'height', 'weight', 'ap_hi', 'ap_lo', 'cardio'], 
                     value_vars=['cholesterol', 'gluc', 'smoke','alco', 'active', 'overweight'], 
                     var_name='variable', value_name="f_value")


    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'f_value']).size().reset_index(name='total') 
    

    # 7
    cat = sns.catplot(x='variable', y='total', hue='f_value', col='cardio', data=df_cat, kind='bar')



    # 8
    fig = cat.fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[
    (df['height'] >= df['height'].quantile(0.025)) &
    (df['height'] <= df['height'].quantile(0.975)) &
    (df['weight'] >= df['weight'].quantile(0.025)) &
    (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12
    corr = df_heat.corr()
    corr = corr.abs()

    # 13
    mask = np.triu(np.ones_like(np.array(corr), dtype=bool))



    # 14
    fig, ax = plt.subplots()

    # 15
    sns.heatmap(corr, mask=mask, annot=True, cmap='coolwarm', fmt=".1f", linewidths=0.5, ax=ax)
    

    # 16
    fig.savefig('heatmap.png')
    return fig
