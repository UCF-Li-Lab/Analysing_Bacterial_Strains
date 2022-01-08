import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def get_data():
    f1 = open('./data/Figure2_data.bed','r')
    lines1 = f1.readlines()
    BHap_P = []
    BHap_R = []
    BHap_F = []
    BHap_abun = []
    BHap_real = []
    BHap_pre = []
    BHap_abs = []

    EVORha_P = []
    EVORha_R = []
    EVORha_F = []
    EVORha_abun = []
    EVORha_real = []
    EVORha_pre = []
    EVORha_abs = []

    MetaSNV_P = []
    MetaSNV_R = []
    MetaSNV_F = []
    MetaSNV_abun = []
    MetaSNV_real = []
    MetaSNV_pre = []
    MetaSNV_abs = []

    strainphlan_P = []
    strainphlan_R = []
    strainphlan_F = []
    strainphlan_abun = []
    strainphlan_real = []
    strainphlan_pre = []
    strainphlan_abs = []

    strainfinder_P = []
    strainfinder_R = []
    strainfinder_F = []
    strainfinder_abun = []
    strainfinder_real = []
    strainfinder_pre = []
    strainfinder_abs = []

    MixtureS_P = []
    MixtureS_R = []
    MixtureS_F = []
    MixtureS_abun = []
    MixtureS_real = []
    MixtureS_pre = []
    MixtureS_abs = []

    for line1 in lines1[1:]:
        Bhap = [float(i) for i in line1.split('\t')[3].split('(')[1].split(')')[0].split(',')]
        # print(Bhap)
        BHap_P.append(Bhap[0])
        BHap_R.append(Bhap[1])
        BHap_F.append(Bhap[2])
        BHap_abun.append(float(line1.split('\t')[3].split(')')[1]))
        BHap_real.append(float(line1.split('\t')[1].split('(')[0]))
        BHap_pre.append(float(line1.split('\t')[3].split('(')[0]))
        BHap_abs.append(abs(float(line1.split('\t')[1].split('(')[0])-float(line1.split('\t')[3].split('(')[0])))

        EVORha = [float(i) for i in line1.split('\t')[4].split('(')[1].split(')')[0].split(',')]
        EVORha_P.append(EVORha[0])
        EVORha_R.append(EVORha[1])
        EVORha_F.append(EVORha[2])
        EVORha_abun.append(float(line1.split('\t')[4].split(')')[1]))
        EVORha_real.append(float(line1.split('\t')[1].split('(')[0]))
        EVORha_pre.append(float(line1.split('\t')[4].split('(')[0]))
        EVORha_abs.append(abs(float(line1.split('\t')[1].split('(')[0]) - float(line1.split('\t')[4].split('(')[0])))

        MetaSNV = [float(i) for i in line1.split('\t')[5].split('(')[1].split(')')[0].split(',')]
        MetaSNV_P.append(MetaSNV[0])
        MetaSNV_R.append(MetaSNV[1])
        MetaSNV_F.append(MetaSNV[2])
        MetaSNV_abun.append(float(line1.split('\t')[5].split(')')[1]))
        MetaSNV_real.append(float(line1.split('\t')[1].split('(')[0]))
        MetaSNV_pre.append(float(line1.split('\t')[5].split('(')[0]))
        MetaSNV_abs.append(abs(float(line1.split('\t')[1].split('(')[0]) - float(line1.split('\t')[5].split('(')[0])))

        strainphlan = [float(i) for i in line1.split('\t')[6].split('(')[1].split(')')[0].split(',')]
        strainphlan_P.append(strainphlan[0])
        strainphlan_R.append(strainphlan[1])
        strainphlan_F.append(strainphlan[2])
        strainphlan_abun.append(float(line1.split('\t')[6].split(')')[1]))
        strainphlan_real.append(float(line1.split('\t')[1].split('(')[0]))
        strainphlan_pre.append(float(line1.split('\t')[6].split('(')[0]))
        strainphlan_abs.append(abs(float(line1.split('\t')[1].split('(')[0]) - float(line1.split('\t')[6].split('(')[0])))

        strainfinder = [float(i) for i in line1.split('\t')[7].split('(')[1].split(')')[0].split(',')]
        strainfinder_P.append(strainfinder[0])
        strainfinder_R.append(strainfinder[1])
        strainfinder_F.append(strainfinder[2])
        strainfinder_abun.append(float(line1.split('\t')[7].split(')')[1]))
        strainfinder_real.append(float(line1.split('\t')[1].split('(')[0]))
        strainfinder_pre.append(float(line1.split('\t')[7].split('(')[0]))
        strainfinder_abs.append(abs(float(line1.split('\t')[1].split('(')[0]) - float(line1.split('\t')[7].split('(')[0])))


        MixtureS = [float(i) for i in line1.split('\t')[8].strip().split('(')[1].split(')')[0].split(',')]
        MixtureS_P.append(MixtureS[0])
        MixtureS_R.append(MixtureS[1])
        MixtureS_F.append(MixtureS[2])
        MixtureS_abun.append(float(line1.split('\t')[8].strip().split(')')[1]))
        MixtureS_real.append(float(line1.split('\t')[1].strip().split('(')[0]))
        MixtureS_pre.append(float(line1.split('\t')[8].strip().split('(')[0]))
        MixtureS_abs.append(abs(float(line1.split('\t')[1].strip().split('(')[0]) - float(line1.split('\t')[8].strip().split('(')[0])))


    P_list = [BHap_P,EVORha_P,MetaSNV_P,MixtureS_P,strainfinder_P,strainphlan_P]
    R_list = [BHap_R,EVORha_R,MetaSNV_R,MixtureS_R,strainfinder_R,strainphlan_R]
    F_list = [BHap_F,EVORha_F,MetaSNV_F,MixtureS_F,strainfinder_F,strainphlan_F]
    abun_list = [BHap_abun, EVORha_abun, MetaSNV_abun,MixtureS_abun, strainfinder_abun,strainphlan_abun]
    real_list = [BHap_real, EVORha_real, MetaSNV_real, MixtureS_real, strainfinder_real, strainphlan_real]
    pre_list = [BHap_pre, EVORha_pre, MetaSNV_pre, MixtureS_pre, strainfinder_pre, strainphlan_pre]
    abs_list = [BHap_abs, EVORha_abs, MetaSNV_abs, MixtureS_abs, strainfinder_abs, strainphlan_abs]
    return [P_list,R_list,F_list,abun_list,real_list,pre_list,abs_list]

def get_data_group7():
    f1 = open('./data/Figure2_data.bed','r')
    lines1 = f1.readlines()
    BHap_P = []
    BHap_R = []
    BHap_F = []
    BHap_abun = []
    BHap_real = []
    BHap_pre = []
    BHap_abs = []

    EVORha_P = []
    EVORha_R = []
    EVORha_F = []
    EVORha_abun = []
    EVORha_real = []
    EVORha_pre = []
    EVORha_abs = []

    MetaSNV_P = []
    MetaSNV_R = []
    MetaSNV_F = []
    MetaSNV_abun = []
    MetaSNV_real = []
    MetaSNV_pre = []
    MetaSNV_abs = []

    strainphlan_P = []
    strainphlan_R = []
    strainphlan_F = []
    strainphlan_abun = []
    strainphlan_real = []
    strainphlan_pre = []
    strainphlan_abs = []

    strainfinder_P = []
    strainfinder_R = []
    strainfinder_F = []
    strainfinder_abun = []
    strainfinder_real = []
    strainfinder_pre = []
    strainfinder_abs = []

    MixtureS_P = []
    MixtureS_R = []
    MixtureS_F = []
    MixtureS_abun = []
    MixtureS_real = []
    MixtureS_pre = []
    MixtureS_abs = []

    for line1 in lines1[1:]:
        if 'USh' in line1.split('\t')[0]:
            Bhap = [float(i) for i in line1.split('\t')[3].split('(')[1].split(')')[0].split(',')]
            BHap_P.append(Bhap[0])
            BHap_R.append(Bhap[1])
            BHap_F.append(Bhap[2])
            BHap_abun.append(float(line1.split('\t')[3].split(')')[1]))
            BHap_real.append(float(line1.split('\t')[1].split('(')[0]))
            BHap_pre.append(float(line1.split('\t')[3].split('(')[0]))
            BHap_abs.append(abs(float(line1.split('\t')[1].split('(')[0]) - float(line1.split('\t')[3].split('(')[0])))

            EVORha = [float(i) for i in line1.split('\t')[4].split('(')[1].split(')')[0].split(',')]
            EVORha_P.append(EVORha[0])
            EVORha_R.append(EVORha[1])
            EVORha_F.append(EVORha[2])
            EVORha_abun.append(float(line1.split('\t')[4].split(')')[1]))
            EVORha_real.append(float(line1.split('\t')[1].split('(')[0]))
            EVORha_pre.append(float(line1.split('\t')[4].split('(')[0]))
            EVORha_abs.append(abs(float(line1.split('\t')[1].split('(')[0]) - float(line1.split('\t')[4].split('(')[0])))

            MetaSNV = [float(i) for i in line1.split('\t')[5].split('(')[1].split(')')[0].split(',')]
            MetaSNV_P.append(MetaSNV[0])
            MetaSNV_R.append(MetaSNV[1])
            MetaSNV_F.append(MetaSNV[2])
            MetaSNV_abun.append(float(line1.split('\t')[5].split(')')[1]))
            MetaSNV_real.append(float(line1.split('\t')[1].split('(')[0]))
            MetaSNV_pre.append(float(line1.split('\t')[5].split('(')[0]))
            MetaSNV_abs.append(abs(float(line1.split('\t')[1].split('(')[0]) - float(line1.split('\t')[5].split('(')[0])))

            strainphlan = [float(i) for i in line1.split('\t')[6].split('(')[1].split(')')[0].split(',')]
            strainphlan_P.append(strainphlan[0])
            strainphlan_R.append(strainphlan[1])
            strainphlan_F.append(strainphlan[2])
            strainphlan_abun.append(float(line1.split('\t')[6].split(')')[1]))
            strainphlan_real.append(float(line1.split('\t')[1].split('(')[0]))
            strainphlan_pre.append(float(line1.split('\t')[6].split('(')[0]))
            strainphlan_abs.append(
                abs(float(line1.split('\t')[1].split('(')[0]) - float(line1.split('\t')[6].split('(')[0])))

            strainfinder = [float(i) for i in line1.split('\t')[7].split('(')[1].split(')')[0].split(',')]
            strainfinder_P.append(strainfinder[0])
            strainfinder_R.append(strainfinder[1])
            strainfinder_F.append(strainfinder[2])
            strainfinder_abun.append(float(line1.split('\t')[7].split(')')[1]))
            strainfinder_real.append(float(line1.split('\t')[1].split('(')[0]))
            strainfinder_pre.append(float(line1.split('\t')[7].split('(')[0]))
            strainfinder_abs.append(
                abs(float(line1.split('\t')[1].split('(')[0]) - float(line1.split('\t')[7].split('(')[0])))

            MixtureS = [float(i) for i in line1.split('\t')[8].strip().split('(')[1].split(')')[0].split(',')]
            MixtureS_P.append(MixtureS[0])
            MixtureS_R.append(MixtureS[1])
            MixtureS_F.append(MixtureS[2])
            MixtureS_abun.append(float(line1.split('\t')[8].strip().split(')')[1]))
            MixtureS_real.append(float(line1.split('\t')[1].strip().split('(')[0]))
            MixtureS_pre.append(float(line1.split('\t')[8].strip().split('(')[0]))
            MixtureS_abs.append(
                abs(float(line1.split('\t')[1].strip().split('(')[0]) - float(line1.split('\t')[8].strip().split('(')[0])))

    P_list = [BHap_P, EVORha_P, MetaSNV_P, MixtureS_P, strainfinder_P, strainphlan_P]
    R_list = [BHap_R, EVORha_R, MetaSNV_R, MixtureS_R, strainfinder_R, strainphlan_R]
    F_list = [BHap_F, EVORha_F, MetaSNV_F, MixtureS_F, strainfinder_F, strainphlan_F]
    abun_list = [BHap_abun, EVORha_abun, MetaSNV_abun, MixtureS_abun, strainfinder_abun, strainphlan_abun]
    real_list = [BHap_real, EVORha_real, MetaSNV_real, MixtureS_real, strainfinder_real, strainphlan_real]
    pre_list = [BHap_pre, EVORha_pre, MetaSNV_pre, MixtureS_pre, strainfinder_pre, strainphlan_pre]
    abs_list = [BHap_abs, EVORha_abs, MetaSNV_abs, MixtureS_abs, strainfinder_abs, strainphlan_abs]
    return [P_list, R_list, F_list, abun_list, real_list, pre_list, abs_list]


def get_data_group10():
    f1 = open('./data/Figure2_data.bed', 'r')
    lines1 = f1.readlines()
    BHap_P = []
    BHap_R = []
    BHap_F = []
    BHap_abun = []
    BHap_real = []
    BHap_pre = []
    BHap_abs = []

    EVORha_P = []
    EVORha_R = []
    EVORha_F = []
    EVORha_abun = []
    EVORha_real = []
    EVORha_pre = []
    EVORha_abs = []

    MetaSNV_P = []
    MetaSNV_R = []
    MetaSNV_F = []
    MetaSNV_abun = []
    MetaSNV_real = []
    MetaSNV_pre = []
    MetaSNV_abs = []

    strainphlan_P = []
    strainphlan_R = []
    strainphlan_F = []
    strainphlan_abun = []
    strainphlan_real = []
    strainphlan_pre = []
    strainphlan_abs = []

    strainfinder_P = []
    strainfinder_R = []
    strainfinder_F = []
    strainfinder_abun = []
    strainfinder_real = []
    strainfinder_pre = []
    strainfinder_abs = []

    MixtureS_P = []
    MixtureS_R = []
    MixtureS_F = []
    MixtureS_abun = []
    MixtureS_real = []
    MixtureS_pre = []
    MixtureS_abs = []

    for line1 in lines1[1:]:
        if 'USh' not in line1.split('\t')[0]:
            Bhap = [float(i) for i in line1.split('\t')[3].split('(')[1].split(')')[0].split(',')]
            BHap_P.append(Bhap[0])
            BHap_R.append(Bhap[1])
            BHap_F.append(Bhap[2])
            BHap_abun.append(float(line1.split('\t')[3].split(')')[1]))
            BHap_real.append(float(line1.split('\t')[1].split('(')[0]))
            BHap_pre.append(float(line1.split('\t')[3].split('(')[0]))
            BHap_abs.append(abs(float(line1.split('\t')[1].split('(')[0]) - float(line1.split('\t')[3].split('(')[0])))

            EVORha = [float(i) for i in line1.split('\t')[4].split('(')[1].split(')')[0].split(',')]
            EVORha_P.append(EVORha[0])
            EVORha_R.append(EVORha[1])
            EVORha_F.append(EVORha[2])
            EVORha_abun.append(float(line1.split('\t')[4].split(')')[1]))
            EVORha_real.append(float(line1.split('\t')[1].split('(')[0]))
            EVORha_pre.append(float(line1.split('\t')[4].split('(')[0]))
            EVORha_abs.append(
                abs(float(line1.split('\t')[1].split('(')[0]) - float(line1.split('\t')[4].split('(')[0])))

            MetaSNV = [float(i) for i in line1.split('\t')[5].split('(')[1].split(')')[0].split(',')]
            MetaSNV_P.append(MetaSNV[0])
            MetaSNV_R.append(MetaSNV[1])
            MetaSNV_F.append(MetaSNV[2])
            MetaSNV_abun.append(float(line1.split('\t')[5].split(')')[1]))
            MetaSNV_real.append(float(line1.split('\t')[1].split('(')[0]))
            MetaSNV_pre.append(float(line1.split('\t')[5].split('(')[0]))
            MetaSNV_abs.append(
                abs(float(line1.split('\t')[1].split('(')[0]) - float(line1.split('\t')[5].split('(')[0])))

            strainphlan = [float(i) for i in line1.split('\t')[6].split('(')[1].split(')')[0].split(',')]
            strainphlan_P.append(strainphlan[0])
            strainphlan_R.append(strainphlan[1])
            strainphlan_F.append(strainphlan[2])
            strainphlan_abun.append(float(line1.split('\t')[6].split(')')[1]))
            strainphlan_real.append(float(line1.split('\t')[1].split('(')[0]))
            strainphlan_pre.append(float(line1.split('\t')[6].split('(')[0]))
            strainphlan_abs.append(
                abs(float(line1.split('\t')[1].split('(')[0]) - float(line1.split('\t')[6].split('(')[0])))

            strainfinder = [float(i) for i in line1.split('\t')[7].split('(')[1].split(')')[0].split(',')]
            strainfinder_P.append(strainfinder[0])
            strainfinder_R.append(strainfinder[1])
            strainfinder_F.append(strainfinder[2])
            strainfinder_abun.append(float(line1.split('\t')[7].split(')')[1]))
            strainfinder_real.append(float(line1.split('\t')[1].split('(')[0]))
            strainfinder_pre.append(float(line1.split('\t')[7].split('(')[0]))
            strainfinder_abs.append(
                abs(float(line1.split('\t')[1].split('(')[0]) - float(line1.split('\t')[7].split('(')[0])))

            MixtureS = [float(i) for i in line1.split('\t')[8].strip().split('(')[1].split(')')[0].split(',')]
            MixtureS_P.append(MixtureS[0])
            MixtureS_R.append(MixtureS[1])
            MixtureS_F.append(MixtureS[2])
            MixtureS_abun.append(float(line1.split('\t')[8].strip().split(')')[1]))
            MixtureS_real.append(float(line1.split('\t')[1].strip().split('(')[0]))
            MixtureS_pre.append(float(line1.split('\t')[8].strip().split('(')[0]))
            MixtureS_abs.append(
                abs(float(line1.split('\t')[1].strip().split('(')[0]) - float(
                    line1.split('\t')[8].strip().split('(')[0])))

    P_list = [BHap_P, EVORha_P, MetaSNV_P, MixtureS_P, strainfinder_P, strainphlan_P]
    R_list = [BHap_R, EVORha_R, MetaSNV_R, MixtureS_R, strainfinder_R, strainphlan_R]
    F_list = [BHap_F, EVORha_F, MetaSNV_F, MixtureS_F, strainfinder_F, strainphlan_F]
    abun_list = [BHap_abun, EVORha_abun, MetaSNV_abun, MixtureS_abun, strainfinder_abun, strainphlan_abun]
    real_list = [BHap_real, EVORha_real, MetaSNV_real, MixtureS_real, strainfinder_real, strainphlan_real]
    pre_list = [BHap_pre, EVORha_pre, MetaSNV_pre, MixtureS_pre, strainfinder_pre, strainphlan_pre]
    abs_list = [BHap_abs, EVORha_abs, MetaSNV_abs, MixtureS_abs, strainfinder_abs, strainphlan_abs]
    return [P_list, R_list, F_list, abun_list, real_list, pre_list, abs_list]

import seaborn as sns
def get_df(list1):
    BHap_P = list1[0]
    EVORha_P = list1[1]
    MetaSNV_P = list1[2]
    MixtureS_P = list1[3]
    strainfinder_P = list1[4]
    strainphlan_P = list1[5]
    data = []
    ticks = ['BHap', 'EVORhA', 'MetaSNV','MixtureS','StrainFinder','StrainPhIAn']
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


def get_df2(P_list,R_list,F1_list):

    data = []
    ticks = ['BHap', 'EVORhA', 'MetaSNV', 'MixtureS', 'StrainFinder', 'StrainPhIAn']

    for i in range(len(P_list)):
        tool_name = ticks[i]
        type = 'precision'
        for j in P_list[i]:
            val = j
            data.append([val,tool_name,type])

    for i in range(len(R_list)):
        tool_name = ticks[i]
        type = 'recall'
        for j in R_list[i]:
            val = j
            data.append([val,tool_name,type])

    for i in range(len(F1_list)):
        tool_name = ticks[i]
        type = 'F1'
        for j in F1_list[i]:
            val = j
            data.append([val,tool_name,type])

    df = pd.DataFrame(data, columns=['Accuracy', 'software',''])

    return df


def get_df3(list1):
    BHap_P = list1[0]
    EVORha_P = list1[1]
    MetaSNV_P = list1[2]
    MixtureS_P = list1[3]
    strainfinder_P = list1[4]
    strainphlan_P = list1[5]
    data = []
    ticks = ['BHap', 'EVORhA', 'MetaSNV','MixtureS','StrainFinder','StrainPhIAn']
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

    df =pd.DataFrame(data,columns=['#strain difference','software'])

    return df

def get_df4():

    data = []

    temp = [16,'BHap']
    data.append(temp)

    temp = [7,'EVORhA']
    data.append(temp)

    temp = [0, 'MetaSNV']
    data.append(temp)

    temp = [33, 'MixtureS']
    data.append(temp)

    temp = [0, 'StrainFinder']
    data.append(temp)

    temp = [0, 'StrainPhIAn']
    data.append(temp)

    df =pd.DataFrame(data,columns=['# of samples','software'])

    return df


def get_df4_1():
    data = []

    temp = [22, 'BHap']
    data.append(temp)

    temp = [10, 'EVORhA']
    data.append(temp)

    temp = [0, 'MetaSNV']
    data.append(temp)

    temp = [45, 'MixtureS']
    data.append(temp)

    temp = [0, 'StrainFinder']
    data.append(temp)

    temp = [0, 'StrainPhIAn']
    data.append(temp)

    df = pd.DataFrame(data, columns=['# of samples', 'software'])

    return df


def get_df4_2():
    data = []

    temp = [38, 'BHap']
    data.append(temp)

    temp = [17, 'EVORhA']
    data.append(temp)

    temp = [0, 'MetaSNV']
    data.append(temp)

    temp = [78, 'MixtureS']
    data.append(temp)

    temp = [0, 'StrainFinder']
    data.append(temp)

    temp = [0, 'StrainPhIAn']
    data.append(temp)

    df = pd.DataFrame(data, columns=['# of samples', 'software'])

    return df


data = get_data()

data_a = data[0]  # ave_precision
data_b = data[1] # ave_recall
data_c = data[2] # ave_F1
data_abun = data[3]
data_real = data[4]
data_pre = data[5]
data_abs = data[6]

df_score = get_df2(data_a,data_b,data_c)
df_abun = get_df(data_abun)
df_num = get_df3(data_abs)
df_sample = get_df4_2()

data_group7 = get_data_group7()

data_group7_a = data_group7[0]  # ave_precision
data_group7_b = data_group7[1] # ave_recall
data_group7_c = data_group7[2] # ave_F1
data_group7_abun = data_group7[3]
data_group7_real = data_group7[4]
data_group7_pre = data_group7[5]
data_group7_abs = data_group7[6]

group7_df_score = get_df2(data_group7_a,data_group7_b,data_group7_c)
group7_df_abun = get_df(data_group7_abun)
group7_df_num = get_df3(data_group7_abs)
group7_df_sample = get_df4()

data_group10 = get_data_group10()

data_group10_a = data_group10[0]  # ave_precision
data_group10_b = data_group10[1] # ave_recall
data_group10_c = data_group10[2] # ave_F1
data_group10_abun = data_group10[3]
data_group10_real = data_group10[4]
data_group10_pre = data_group10[5]
data_group10_abs = data_group10[6]

group10_df_score = get_df2(data_group10_a,data_group10_b,data_group10_c)
group10_df_abun = get_df(data_group10_abun)
group10_df_num = get_df3(data_group10_abs)
group10_df_sample = get_df4_1()








ticks = ['BHap', 'EVORhA', 'MetaSNV','MixtureS','StrainFinder','StrainPhIAn']


# sns.set_theme(style="white", palette=None)
# fig = plt.figure(dpi=100)
fig = plt.figure(dpi=100)
# fig.set_figheight(10)
# fig.set_figwidth(28)
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"
sns.set(font_scale = 1.55)
sns.set_style("white")
plt.subplot(4, 3, 1)
# sns.set(font_scale = 1.5)
ax1 = sns.violinplot(x='software', y='Accuracy',hue = '', data=group7_df_score)
# ax2.set_xticklabels(ax2.get_xticks(), size = 14)
# ax2.set_yticklabels(ax2.get_yticks(), size = 14)
ax1.set(xlabel=None,ylim=(0, 1))
# plt.legend(loc='upper right')
plt.legend(loc='lower center', bbox_to_anchor=(0.5, 1.1), ncol=3)
# plt.setp(ax1.get_legend().get_texts(), fontsize='8')
plt.title('Unshared',size=14,fontweight="bold")

plt.subplot(4, 3, 2)
# sns.set(font_scale = 1.5)
ax1 = sns.violinplot(x='software', y='Accuracy',hue = '', data=group10_df_score)
# ax2.set_xticklabels(ax2.get_xticks(), size = 14)
# ax2.set_yticklabels(ax2.get_yticks(), size = 14)
plt.legend(loc='lower center', bbox_to_anchor=(0.5, 1.1), ncol=3)
ax1.set(xlabel=None,ylim=(0, 1))
plt.title('Shared',size=14,fontweight="bold")

plt.subplot(4, 3, 3)
# sns.set(font_scale = 1.5)
ax1 = sns.violinplot(x='software', y='Accuracy',hue = '', data=df_score)
# ax2.set_xticklabels(ax2.get_xticks(), size = 14)
# ax2.set_yticklabels(ax2.get_yticks(), size = 14)
ax1.set(xlabel=None,ylim=(0, 1))
plt.legend(loc='lower center', bbox_to_anchor=(0.5, 1.1), ncol=3)
plt.title('All',size=14,fontweight="bold")




plt.subplot(4, 3, 4)
# sns.set(font_scale = 1.5)
ax1 = sns.violinplot(x='software', y='MAE', data=group7_df_abun)
# ax2.set_xticklabels(ax2.get_xticks(), size = 14)
# ax2.set_yticklabels(ax2.get_yticks(), size = 14)
ax1.set(xlabel=None,ylim=(0, 0.6))
plt.title('Unshared',size=14,fontweight="bold")


plt.subplot(4, 3, 5)
# sns.set(font_scale = 1.5)
ax2 = sns.violinplot(x='software', y='MAE', data=group10_df_abun)
# ax1.set_xticklabels(ax1.get_xticks(), size = 14)
# ax1.set_yticklabels(ax1.get_yticks(), size = 14)
ax2.set(xlabel=None,ylim=(0, 0.6))
plt.title('Shared',size=14,fontweight="bold")


plt.subplot(4, 3, 6)
# ax = sns.violinplot(x='software', y='MAE', data=df_abun)
ax3 = sns.violinplot(x='software', y='MAE', data=df_abun)

# ax.set_xticklabels(ax.get_xticks(), size = 14)
# ax.set_yticklabels(ax.get_yticks(), size = 14)
ax3.set(xlabel=None,ylim=(0, 0.6))
plt.title('All',size=14,fontweight="bold")


plt.subplot(4, 3, 7)
# sns.set(font_scale = 1.5)
ax1 = sns.violinplot(x='software', y='#strain difference', data=group7_df_num)
# ax2.set_xticklabels(ax2.get_xticks(), size = 14)
# ax2.set_yticklabels(ax2.get_yticks(), size = 14)
ax1.set(xlabel=None,ylim=(0, 6))
plt.title('Unshared',size=14,fontweight="bold")


plt.subplot(4, 3, 8)
# sns.set(font_scale = 1.5)
ax2 = sns.violinplot(x='software', y='#strain difference', data=group10_df_num)
# ax1.set_xticklabels(ax1.get_xticks(), size = 14)
# ax1.set_yticklabels(ax1.get_yticks(), size = 14)
ax2.set(xlabel=None,ylim=(0, 6))
plt.title('Shared',size=14,fontweight="bold")


plt.subplot(4, 3, 9)
# ax = sns.violinplot(x='software', y='MAE', data=df_abun)
ax3 = sns.violinplot(x='software', y='#strain difference', data=df_num)

# ax.set_xticklabels(ax.get_xticks(), size = 14)
# ax.set_yticklabels(ax.get_yticks(), size = 14)
ax3.set(xlabel=None,ylim=(0, 6))
plt.title('All',size=14,fontweight="bold")



plt.subplot(4, 3, 10)
# sns.set(font_scale = 1.5)
ax1 = sns.barplot(x='software', y='# of samples', data=group7_df_sample)
# ax2.set_xticklabels(ax2.get_xticks(), size = 14)
# ax2.set_yticklabels(ax2.get_yticks(), size = 14)
ax1.set(xlabel=None,ylim=(0, 80))
plt.title('Unshared',size=14,fontweight="bold")


plt.subplot(4, 3, 11)
# sns.set(font_scale = 1.5)
ax2 = sns.barplot(x='software', y='# of samples', data=group10_df_sample)
# ax1.set_xticklabels(ax1.get_xticks(), size = 14)
# ax1.set_yticklabels(ax1.get_yticks(), size = 14)
ax2.set(xlabel=None,ylim=(0, 80))
plt.title('Shared',size=14,fontweight="bold")


plt.subplot(4, 3, 12)
# ax = sns.violinplot(x='software', y='MAE', data=df_abun)
ax3 = sns.barplot(x='software', y='# of samples', data=df_sample)

# ax.set_xticklabels(ax.get_xticks(), size = 14)
# ax.set_yticklabels(ax.get_yticks(), size = 14)
ax3.set(xlabel=None,ylim=(0, 80))
plt.title('All',size=14,fontweight="bold")


# plt.tight_layout()
# plt.savefig("/media/saidi/Elements/Project/Project_for_Min/paper_writing_updated/revised_12132021/Figure2.png")
# plt.savefig('boxcompare.png')
plt.show()
