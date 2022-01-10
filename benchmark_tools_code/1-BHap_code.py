




#################### BHap Link ####################

# https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6931272/




output_path = 'reference genome name'
ref_name = 'reference genome'
reads1 = 'read file 1'
reads2 = 'read file 2'
read_length = 'read length'
cov = 'input read coverage'
ref_size = 'reference genome size'

command = 'python2.7 ./run_BHap.py -d %s -r %s -t fastq -1 %s -2 %s -l %s -c %s -g %s' % (output_path,ref_name,reads1,reads2,read_length,cov,ref_size)





