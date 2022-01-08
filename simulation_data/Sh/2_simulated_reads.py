import os
from os import listdir
from os.path import isfile,join


################# You need to change this location based on your own path ##############
inGenomeLoc = '/dwgsim/simulated_data_with_evolutionary_relationship/data/mutated_genome_similar/'
resLoc = '/dwgsim/simulated_data_with_evolutionary_relationship/data/simulated_raw/'

# dwgsimLoc = '/media/student/Study/project/project12/tools/dwgsim'
dwgsimLoc = 'dwgsim'
allGenomes = [item for item in listdir('%s' %inGenomeLoc)
              if isfile(join('%s' %inGenomeLoc,item)) and item.startswith('genome')]
genomeNames = ['NC_009515.1','NC_014932.1','NC_020995.1']
insertionLength = 400
randomSeed = '1534513916'
######################################################################################################################
def run_dwgsim(errorRate,insertionLength,coverage,readLen,genome,resName):
    error_single = '{:.5f}'.format(errorRate/2.0)


    command = dwgsimLoc + ' -e ' + str(error_single) + ' -E ' + str(error_single) + \
              ' -d ' + str(insertionLength) + ' -s 50 -C ' + \
              str(coverage) + ' -1 ' + str(readLen) + ' -2 ' + str(readLen) \
              + ' -r 0 -z '+randomSeed+' -n 0 -X 0 -R 0 -c 0 -S 0 -y 0 ' + genome \
              + ' ' + resName
    print command
    os.system(command)



def generate_simulate_data(group,groupID):
    command = 'mkdir -p ' + resLoc+groupID
    os.system(command)
    for genomeName in genomeNames:
        numHaplotype = group[0][0]
        populationTotalCoverages = group[5]
        allCoverageList = group[1]

        mutateList = group[2]
        readList = group[3]
        errorRateList = group[4]
        similarityList = group[6]
        hapTypeList = group[7]

        for hapID in range(1, numHaplotype + 1):
            for coverage in populationTotalCoverages:
                for coverageCouple in allCoverageList:
                    individualCoverageList =  [coverage * c * 1.0 / sum(coverageCouple)
                                               for c in coverageCouple]
                    #for oneCoverage in individualCoverageList:
                    oneCoverage = individualCoverageList[hapID-1]
                    for mutatePercentage in mutateList:
                        for readLen in readList:
                            for errorRate in errorRateList:
                                    for similarity in similarityList:
                                        for hapType in hapTypeList:
                                            inGenomeFile = inGenomeLoc + '_'.join(
                                                ['genome', genomeName,
                                                 str(mutatePercentage),
                                                 str(hapID),str(similarity),
                                                 hapType])

                                            resName = resLoc + groupID + '/' + '_'.join(
                                                [genomeName, str(mutatePercentage),
                                                 str(hapID),
                                                 str(readLen),
                                                 str(insertionLength), str(oneCoverage),
                                                 str(errorRate),str(similarity),
                                                 hapType])

                                            run_dwgsim(errorRate, insertionLength,
                                                       oneCoverage,
                                                       readLen, inGenomeFile, resName)


########################################################################################################################

#1.number of haplotype: 2
#2.proportions: 30/70
#3.mutation rate:   0.01%
#4.read length: 100bp
#5.error rate:  0.1%
#6.coverage:    100
#7.similarity: 0.3


Sh_1 = [[3],[(10,30,60), (5,25,70)],[0.01],[100],[0.001],[200,300,400,500],
          [0.3],['t1']]
generate_simulate_data(Sh_1, 'Sh_1')

Sh_2 = [[4],[(5,15,25,55), (5,10,35,50)],[0.01],[100],[0.001],
          [200,300,400,500],[0.3],['t2']]
generate_simulate_data(Sh_2, 'Sh_2')

Sh_3 = [[4],[(5,15,25,55), (5,10,35,50)],[0.01],[100],[0.001],
          [200,300,400,500],[0.3],['t3']]
generate_simulate_data(Sh_3, 'Sh_3')
