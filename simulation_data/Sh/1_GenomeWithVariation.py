#!/usr/bin/python
import random
import sys

################# You need to change this location based on your own path ##############
genomeLoc = '/dwgsim/simulated_data_with_evolutionary_relationship/data/original_genome/'
resLoc = '/dwgsim/simulated_data_with_evolutionary_relationship/data/mutated_genome_similar/'

taxonNames = ['GCF_000253015.1_ASM25301v1_genomic.fna',
              'GCF_000016525.1_ASM1652v1_genomic.fna',
              'GCF_000157355.2_ASM15735v2_genomic.fna']

#mutatePercentageList = [0.01,0.02,0.03,0.04,0.05]
hapType_list = ['t1','t2','t3']
#mutatePercentageList = [0.01]
mutatePercentageList = [0.01, 0.02,0.03,0.04,0.05]
#similarity_list = [0.3,0.4,0.5]
similarity_list = [0.1,0.2,0.3,0.4,0.5,0.6] # type1 and type2
similarity_list_2nd = [0.1]
#mutatePercentageList = [0.07,0.1,0.15]
variationCoeff = 100
outFileChunkSize = 70
numGenomeCount = 5
randomSeedDict = {1:1001,2:0101,3:1111,4:1110}
################################################################################
'''
type1: hap1 and hap2 shared SNPs with similarity_ratio, hap3 is independent
type2: hap1 and hap2 shared SNPs with similarity_ratio, hap3 shared 10% with hap1
    and hap2, hap4 is independent
type3: hap1 and hap2 shared SNPs with similarity_ratio,
    hap3 and hap4 shared SNPs with similarity_ratio,
'''
################################################################################
# def test_random_seed():
#     seed = 100
#     testList = [i for i in range(10000)]
#     random.seed(seed)
#
#     for _ in range(10):
#         a = random.sample(testList,1)
#         print a
#
#
# for _ in range(5):
#     print '##################'
#     test_random_seed()
#     print '####################'



def mutateGenome(genomeSeq, variationPercentage,genomeID):
    seed = randomSeedDict[genomeID]*variationPercentage

    random.seed(seed)


    mutated = []
    nlist = ['A', 'C', 'G', 'T']
    for i, nucl in enumerate(genomeSeq):
        if random.randint(1, 100 * variationCoeff) <= variationPercentage:
            mutatedNucl = random.sample([item for item in nlist if item!=nucl],1)
            mutated.append([mutatedNucl[0],i])
            #print mutatedNucl[0]+'\t'+str(i)
        else:
            mutated.append([nucl, -1])


    mutations = [item for item in mutated if item[1] != -1]
    mutated = [item[0] for item in mutated]
    mutatedSeq = "".join(mutated)
    print "Number of mutations", len(mutations)
    return mutatedSeq, mutations


def mutateGenome_similar(genomeSeq, variationPercentage,genomeID,similarity,snps):
    seed = randomSeedDict[genomeID]*variationPercentage

    random.seed(seed)

    #how many to simulat

    mutated = []
    mutated_info_trace = {}
    nlist = ['A', 'C', 'G', 'T']
    similarity_count = 0
    for i, nucl in enumerate(genomeSeq):
        if random.randint(1, 100 * variationCoeff) <= variationPercentage:
            mutatedNucl = random.sample([item for item in nlist if item!=nucl],1)
            mutated.append([mutatedNucl[0],i])
            mutated_info_trace.update({i:[nucl,mutatedNucl[0]]})
            #print mutatedNucl[0]+'\t'+str(i)
        else:
            mutated.append([nucl, -1])

    #fetch all mutations
    mutations = [item for item in mutated if item[1] != -1]

    #information for SNPs
    similarity_num = int(len(snps) *similarity)
    snpsIDList = [i for i in range(len(snps))]
    snp_select_index = random.sample(snpsIDList,similarity_num)
    snp_select_item = [snps[index] for index in snp_select_index]
    snp_select_loc = [int(snps[index][1]) for index in snp_select_index]

    #choose the item should be pop out
    same_id = [index for index,item in enumerate(mutations)
               if item[1] in snp_select_loc]

    #step1: recover the mutated genome, and pop the ones with same ID
    if len(same_id)!=0:
        same_id.sort(reverse=True)
        for index in same_id:
            loc = mutations[index][1]
            mutated[loc] = [mutated_info_trace[loc][0],-1]
            mutations.pop(index)

    #step2: get number of pop for left
    num_left = similarity_num - len(same_id)
    mutations_ID_list = [i for i in range(len(mutations))]
    pop_ID_list = random.sample(mutations_ID_list,num_left)
    pop_ID_list.sort(reverse=True)
    for index in pop_ID_list:
        loc = mutations[index][1]
        mutated[loc] = [mutated_info_trace[loc][0], -1]
        mutations.pop(index)


    #step3: add similar SNPs into genome
    for item in snp_select_item:
        loc = int(item[1])
        nucl = item[0]
        mutations.append([nucl,loc])
        mutated[loc] = [nucl,loc]


    mutated = [item[0] for item in mutated]
    mutatedSeq = "".join(mutated)
    print "Number of mutations", len(mutations)
    return mutatedSeq, mutations


def writeGenome(gen, outfile, name, nuclpline):
    fh = open(outfile, 'w')
    fh.write(">%s\n" % name)
    splits = [gen[i: i + nuclpline] for i in range(0, len(gen), nuclpline)]
    # print splits
    outStr = "\n".join(splits)
    fh.write(outStr)


#the number 1 haplotype
def simulate_hap_one(genomeSeq,variationPercentage,genomeID,genomeName,
                  mutatePercentage,similarity,hapType):
    mutatedGenome, mutations = mutateGenome(genomeSeq, variationPercentage,
                                            genomeID)
    resName = resLoc + '_'.join(['genome_' + genomeName,str(mutatePercentage),
                                 str(genomeID),str(similarity),hapType])

    resGenomeName = '_'.join([genomeName,str(mutatePercentage),str(genomeID),
                              str(similarity),hapType])



    writeGenome(mutatedGenome, resName, resGenomeName, outFileChunkSize)

    resMutateName = resLoc + '_'.join(['mutations_' + genomeName,
                                       str(mutatePercentage),str(genomeID),
                                       str(similarity),hapType])

    mutations = [[item[0], str(item[1])] for item in mutations]
    mutOut = "\n".join([",".join(item) for item in mutations])
    f = open(resMutateName, 'w')
    f.write(mutOut)

def simulate_hap_two(genomeSeq,variationPercentage,genomeID,genomeName,
                  mutatePercentage,similarity,hapType):
    # get SNPs from genomeID = 1
    snps = []
    snps_loc = resLoc + '_'.join(['mutations_' + genomeName,str(mutatePercentage),
                                  str(1),str(similarity),hapType])

    with open('%s' % snps_loc) as f:
        for line in f:
            line = line.strip().split(',')
            snps.append(line)

    mutatedGenome, mutations = mutateGenome_similar(genomeSeq,
                                                    variationPercentage,
                                                    genomeID, similarity,
                                                    snps)

    resName = resLoc + '_'.join(['genome_' + genomeName,str(mutatePercentage),
                                 str(genomeID),str(similarity),hapType])

    resGenomeName = '_'.join([genomeName,str(mutatePercentage),str(genomeID),
                              str(similarity),hapType])

    writeGenome(mutatedGenome, resName, resGenomeName, outFileChunkSize)

    resMutateName = resLoc + '_'.join(['mutations_' + genomeName,
                                       str(mutatePercentage),str(genomeID),
                                       str(similarity),hapType])

    mutations = [[item[0], str(item[1])] for item in mutations]
    mutOut = "\n".join([",".join(item) for item in mutations])
    f = open(resMutateName, 'w')
    f.write(mutOut)


def simulate_hap_three(genomeSeq,variationPercentage,genomeID,genomeName,
                  mutatePercentage,similarity,hapType,similarity_2nd):


    if hapType == 't1':

        mutatedGenome, mutations = mutateGenome(genomeSeq, variationPercentage,
                                                genomeID)

        resName = resLoc + '_'.join(
            ['genome_' + genomeName, str(mutatePercentage),
             str(genomeID), str(similarity), hapType])

        resGenomeName = '_'.join(
            [genomeName, str(mutatePercentage), str(genomeID),
             str(similarity), hapType])

        writeGenome(mutatedGenome, resName, resGenomeName, outFileChunkSize)

        resMutateName = resLoc + '_'.join(['mutations_' + genomeName,
                                           str(mutatePercentage), str(genomeID),
                                           str(similarity), hapType])

        mutations = [[item[0], str(item[1])] for item in mutations]
        mutOut = "\n".join([",".join(item) for item in mutations])
        f = open(resMutateName, 'w')
        f.write(mutOut)

    elif hapType == 't2':
        # get SNPs from genomeID = 1
        snps_hap1 = []
        snps_loc = resLoc + '_'.join(['mutations_' + genomeName,str(mutatePercentage),
                                  str(1),str(similarity),hapType])
        with open('%s' % snps_loc) as f:
            for line in f:
                line = line.strip().split(',')
                snps_hap1.append((line[0],line[1]))

        #get SNPs from genomeID = 2
        snps_hap2 = []
        snps_loc = resLoc + '_'.join(['mutations_' + genomeName,str(mutatePercentage),
                                  str(2),str(similarity),hapType])
        with open('%s' % snps_loc) as f:
            for line in f:
                line = line.strip().split(',')
                snps_hap2.append((line[0],line[1]))


        #find shared SNPs betweeen 1 and 2
        snps = list(set(snps_hap1).intersection(snps_hap2))
        snps = [list(item) for item in snps]
        similarity_relative = similarity_2nd/similarity


        mutatedGenome, mutations = mutateGenome_similar(genomeSeq,
                                                        variationPercentage,
                                                        genomeID, similarity_relative,
                                                        snps)

        resName = resLoc + '_'.join(
            ['genome_' + genomeName, str(mutatePercentage),
             str(genomeID), str(similarity), hapType])

        resGenomeName = '_'.join(
            [genomeName, str(mutatePercentage), str(genomeID),
             str(similarity), hapType])

        writeGenome(mutatedGenome, resName, resGenomeName, outFileChunkSize)

        resMutateName = resLoc + '_'.join(['mutations_' + genomeName,
                                           str(mutatePercentage), str(genomeID),
                                           str(similarity), hapType])

        mutations = [[item[0], str(item[1])] for item in mutations]
        mutOut = "\n".join([",".join(item) for item in mutations])
        f = open(resMutateName, 'w')
        f.write(mutOut)


    elif hapType == 't3':
        mutatedGenome, mutations = mutateGenome(genomeSeq, variationPercentage,
                                                genomeID)

        resName = resLoc + '_'.join(
            ['genome_' + genomeName, str(mutatePercentage),
             str(genomeID), str(similarity), hapType])

        resGenomeName = '_'.join(
            [genomeName, str(mutatePercentage), str(genomeID),
             str(similarity), hapType])

        writeGenome(mutatedGenome, resName, resGenomeName, outFileChunkSize)

        resMutateName = resLoc + '_'.join(['mutations_' + genomeName,
                                           str(mutatePercentage), str(genomeID),
                                           str(similarity), hapType])

        mutations = [[item[0], str(item[1])] for item in mutations]
        mutOut = "\n".join([",".join(item) for item in mutations])
        f = open(resMutateName, 'w')
        f.write(mutOut)
    else:
        sys.exit()


def simulate_hap_four(genomeSeq,variationPercentage,genomeID,genomeName,
                  mutatePercentage,similarity,hapType):

    if hapType == 't2':

        mutatedGenome, mutations = mutateGenome(genomeSeq, variationPercentage,
                                                genomeID)
        resName = resLoc + '_'.join(
            ['genome_' + genomeName, str(mutatePercentage),
             str(genomeID), str(similarity), hapType])

        resGenomeName = '_'.join(
            [genomeName, str(mutatePercentage), str(genomeID),
             str(similarity), hapType])

        writeGenome(mutatedGenome, resName, resGenomeName, outFileChunkSize)

        resMutateName = resLoc + '_'.join(['mutations_' + genomeName,
                                           str(mutatePercentage), str(genomeID),
                                           str(similarity), hapType])

        mutations = [[item[0], str(item[1])] for item in mutations]
        mutOut = "\n".join([",".join(item) for item in mutations])
        f = open(resMutateName, 'w')
        f.write(mutOut)

    elif hapType == 't3':
        # get SNPs from genomeID = 1
        snps = []
        snps_loc = resLoc + '_'.join(['mutations_' + genomeName,str(mutatePercentage),
                                  str(3),str(similarity),hapType])


        with open('%s' % snps_loc) as f:
            for line in f:
                line = line.strip().split(',')
                snps.append((line[0],line[1]))



        mutatedGenome, mutations = mutateGenome_similar(genomeSeq,
                                                        variationPercentage,
                                                        genomeID, similarity,
                                                        snps)

        resName = resLoc + '_'.join(
            ['genome_' + genomeName, str(mutatePercentage),
             str(genomeID), str(similarity), hapType])

        resGenomeName = '_'.join(
            [genomeName, str(mutatePercentage), str(genomeID),
             str(similarity), hapType])

        writeGenome(mutatedGenome, resName, resGenomeName, outFileChunkSize)

        resMutateName = resLoc + '_'.join(['mutations_' + genomeName,
                                           str(mutatePercentage), str(genomeID),
                                           str(similarity), hapType])

        mutations = [[item[0], str(item[1])] for item in mutations]
        mutOut = "\n".join([",".join(item) for item in mutations])
        f = open(resMutateName, 'w')
        f.write(mutOut)



def mutate_single_genome(taxonName,variationPercentage,genomeID,mutatePercentage,
                         similarity,info,similarity_2nd):
    hapType = info[0]
    numHaps = info[1]


    #get genome name
    inName = genomeLoc + taxonName
    fh = open(inName, "r")
    fileLines = fh.readlines()
    fh.close()

    # remove the first line of fasta file that contains information about genome
    firstLine = fileLines.pop(0)
    firstLine = firstLine.split("|")
    genomeName = firstLine[-1]
    genomeName = genomeName.split(" ")
    genomeName = genomeName[0]
    genomeName = genomeName.replace('>','')
    print genomeName



    #fetch all Fasta data and make it into upper character
    stripped = [item.strip() for item in fileLines]
    genomeSeq = "".join(stripped)
    # genomeSeq = "acgttaccgtaccg"
    genomeSeq = genomeSeq.upper()
    genomeLen = len(genomeSeq)
    print "Sequence length is %d bp" % genomeLen



    if genomeID == 1:
        simulate_hap_one(genomeSeq, variationPercentage, genomeID, genomeName,
                         mutatePercentage,similarity,hapType)
    elif genomeID == 2:
        simulate_hap_two(genomeSeq, variationPercentage, genomeID, genomeName,
                         mutatePercentage,similarity,hapType)
    elif genomeID == 3:
        simulate_hap_three(genomeSeq, variationPercentage, genomeID, genomeName,
                           mutatePercentage, similarity ,hapType, similarity_2nd)
    elif genomeID == 4:
        simulate_hap_four(genomeSeq,variationPercentage,genomeID,genomeName,
                          mutatePercentage,similarity,hapType)





################################################################################
# #assemble simulate information
information = [['t1',3],['t2',4],['t3',4]]

for info in information:
    for genomeID in range(1,numGenomeCount+1):
        for taxonName in taxonNames:
            for mutatePercentage in mutatePercentageList:
                variationPercentage = mutatePercentage * variationCoeff
                for similarity in similarity_list:
                    for similarity_2nd in similarity_list_2nd:

                        #if (genomeID!=3) or (info[0]!='t2'):
                        # if (genomeID != 4):
                        #     continue
                        mutate_single_genome(taxonName,variationPercentage,
                                             genomeID,mutatePercentage,similarity,
                                             info,similarity_2nd)


print "finished\n***************************\n\n"
