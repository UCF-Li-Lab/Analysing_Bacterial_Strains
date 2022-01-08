#!/usr/bin/python
import random

################# You need to change this location based on your own path ##############
genomeLoc = '/dwgsim/simulated_data_without_evolutionary_relationship/data/original_genome/'
resLoc = '/dwgsim/simulated_data_without_evolutionary_relationship/data/mutated_genome/'


taxonNames = ['GCF_000253015.1_ASM25301v1_genomic.fna',
              'GCF_000016525.1_ASM1652v1_genomic.fna',
              'GCF_000157355.2_ASM15735v2_genomic.fna']



mutatePercentageList = [0.01,0.02,0.03,0.04,0.05] # mutation rate percentage is 0.01%
variationCoeff = 100
outFileChunkSize = 70
numGenomeCount = 4
randomSeedDict = {1:1001,2:0101,3:1111,4:1110}
################################################################################

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


def writeGenome(gen, outfile, name, nuclpline):
    fh = open(outfile, 'w')
    fh.write(">%s\n" % name)
    splits = [gen[i: i + nuclpline] for i in range(0, len(gen), nuclpline)]
    # print splits
    outStr = "\n".join(splits)
    fh.write(outStr)

def mutate_single_genome(taxonName,variationPercentage,genomeID):
    mutatedGenomeFile = resLoc
    #get genome name
    inName = genomeLoc + taxonName
    fh = open(inName, "r")
    fileLines = fh.readlines()
    fh.close()

    firstLine = fileLines.pop(0)  # remove the first line of fasta file that contains information about genome
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



    mutatedGenome, mutations = mutateGenome(genomeSeq, variationPercentage,genomeID)
    print "Mutated Genome is ready"


    resName = resLoc+ 'genome_'+genomeName+'_'+str(mutatePercentage)+'_'+str(genomeID)
    resGenomeName = genomeName+'_'+str(mutatePercentage)+'_'+str(genomeID)

    writeGenome(mutatedGenome, resName, resGenomeName, outFileChunkSize)

    resMutateName = resLoc + 'mutations_'+genomeName+'_'+str(mutatePercentage)+'_'+str(genomeID)
    mutations = [[item[0], str(item[1])] for item in mutations]
    mutOut = "\n".join([",".join(item) for item in mutations])
    f = open(resMutateName, 'w')
    f.write(mutOut)

################################################################################
for genomeID in range(1,numGenomeCount+1):
    for taxonName in taxonNames:
        for mutatePercentage in mutatePercentageList:
            variationPercentage = mutatePercentage * variationCoeff
            mutate_single_genome(taxonName,variationPercentage,genomeID)


print "finished\n***************************\n\n"
