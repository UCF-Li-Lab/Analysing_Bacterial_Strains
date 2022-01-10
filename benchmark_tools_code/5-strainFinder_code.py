







############################# strainFinder Link #################################

# Link: https://github.com/cssmillie/StrainFinder





############################## bam to the count file, you could use other tools to get the count file ##########################################

ref_name = 'reference genome'
bam_file = 'sorted bam file'
command1 = 'pysamstats --fasta %s --type variation %s > %s' % (ref_name,bam_file,'count_file')

################ strainFinder running code ##########################

################ You should make your count file to be the count cPickle file any way you want ##############
input_file = 'count_file.cPickle'
output_file1 = '/em_out.cPickle'
output_file2 = '/out_table.txt'
output_file3 = '/log.txt'
command2 = 'python StrainFinder.py --aln %s -N 5 --max_reps 10 --dtol 1 --ntol 2 --max_time 3600 --converge --em_out %s --otu_out %s --log %s --n_keep 3 --force_update --merge_out --msg' % (
input_file, output_file1, output_file2, output_file3)
