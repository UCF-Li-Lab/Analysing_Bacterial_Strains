import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

def get_data():
    f1 = open('./data/FigureS1','r')
    lines1 = f1.readlines()

    print(lines1)
    BHap_P = []
    EVORha_P = []
    MetaSNV_P = []
    strainphlan_P = []
    strainfinder_P = []
    MixtureS_P = []

    for line1 in lines1[1:]:
        if '(' in line1.split('\t')[2]:
            Bhap = [float(i) for i in line1.split('\t')[2].split('(')[1].split(')')[0].split(',')]
            BHap_P.append(Bhap[0])
        if '(' in line1.split('\t')[3]:
            EVORha = [float(i) for i in line1.split('\t')[3].split('(')[1].split(')')[0].split(',')]
            EVORha_P.append(EVORha[0])
        if '(' in line1.split('\t')[4]:
            MetaSNV = [float(i) for i in line1.split('\t')[4].split('(')[1].split(')')[0].split(',')]
            MetaSNV_P.append(MetaSNV[0])
        if '(' in line1.split('\t')[5]:
            strainphlan = [float(i) for i in line1.split('\t')[5].split('(')[1].split(')')[0].split(',')]
            strainphlan_P.append(strainphlan[0])
        if '(' in line1.split('\t')[6]:
            strainfinder = [float(i) for i in line1.split('\t')[6].split('(')[1].split(')')[0].split(',')]
            strainfinder_P.append(strainfinder[0])
        if '(' in line1.split('\t')[7]:
            MixtureS = [float(i) for i in line1.split('\t')[7].strip().split('(')[1].split(')')[0].split(',')]
            MixtureS_P.append(MixtureS[0])

    data = []
    ticks = ['BHap', 'EVORhA', 'MetaSNV', 'MixtureS' , 'StrainFinder','StrainPhIAn']
    for i in range(len(BHap_P)):
        temp = [BHap_P[i],'BHap']
        data.append(temp)

    for i in range(len(EVORha_P)):
        temp = [EVORha_P[i],'EVORhA']
        data.append(temp)

    for i in range(len(MetaSNV_P)):
        temp = [MetaSNV_P[i], 'MetaSNV']
        data.append(temp)

    for i in range(len(MixtureS_P)):
        temp = [MixtureS_P[i], 'MixtureS']
        data.append(temp)



    for i in range(len(strainfinder_P)):
        temp = [strainfinder_P[i], 'StrainFinder']
        data.append(temp)

    for i in range(len(strainphlan_P)):
        temp = [strainphlan_P[i], 'StrainPhIAn']
        data.append(temp)

    df =pd.DataFrame(data,columns=['MAE','software'])

    return df

plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"

sns.set(font_scale = 2)
sns.set_style("white")
data = get_data()
ticks = ['BHap', 'EVORhA', 'MetaSNV', 'MixtureS' , 'StrainFinder','StrainPhIAn']
# sns.set_theme(style="whitegrid")

ax = sns.violinplot(x='software', y='MAE', data=data)
ax.set(ylim=(0, None))
plt.show()

