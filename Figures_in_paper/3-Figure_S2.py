import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

def get_data():


    data = []

    temp = [997.4,'BHap']
    data.append(temp)

    temp = [348.6,'EVORhA']
    data.append(temp)

    temp = [18.7, 'MetaSNV']
    data.append(temp)

    temp = [2277.96, 'MixtureS']
    data.append(temp)

    temp = [3656.58, 'StrainFinder']
    data.append(temp)

    temp = [841.13, 'StrainPhIAn']
    data.append(temp)

    df =pd.DataFrame(data,columns=['Average time used(s)','software'])

    return df

def get_data1():


    data = []

    temp = [0.145*32 *1024,'BHap']
    data.append(temp)

    temp = [0.105*32 *1024,'EVORhA']
    data.append(temp)

    temp = [0.027*32 *1024, 'MetaSNV']
    data.append(temp)

    temp = [0.113*32 *1024, 'MixtureS']
    data.append(temp)

    temp = [0.12*32 *1024, 'StrainFinder']
    data.append(temp)

    temp = [0.08*32 *1024, 'StrainPhIAn']
    data.append(temp)

    df =pd.DataFrame(data,columns=['Maximum memory used (megabytes)','software'])

    return df


df1 = get_data()
df2 = get_data1()

fig = plt.figure()
# fig.set_figheight(8)
# fig.set_figwidth(12)
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"

sns.set(font_scale = 2)
sns.set_style("white")
plt.subplot(1, 2, 1)
# sns.set(font_scale = 1.5)
ax1 = sns.barplot(x='software', y='Average time used(s)', data=df1)
# ax2.set_xticklabels(ax2.get_xticks(), size = 14)
# ax2.set_yticklabels(ax2.get_yticks(), size = 14)
ax1.set(xlabel='sowtware')
# plt.legend(loc='upper right')
# plt.setp(ax1.get_legend().get_texts(), fontsize='10')


plt.subplot(1, 2, 2)
# sns.set(font_scale = 1.5)
ax1 = sns.barplot(x='software', y='Maximum memory used (megabytes)', data=df2)
# ax2.set_xticklabels(ax2.get_xticks(), size = 14)
# ax2.set_yticklabels(ax2.get_yticks(), size = 14)
# plt.legend(loc='upper right')
# plt.setp(ax1.get_legend().get_texts(), fontsize='10')
ax1.set(xlabel='software')

# plt.legend()
plt.show()

