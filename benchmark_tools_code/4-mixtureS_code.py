





###################### mixtureS ###############

# Link: http://www.cs.ucf.edu/~xiaoman/mixtureS/


# running code
file = 'sample_name'
input_file1 = '.bam'
output_path1 = 'output_path'
ref_name = 'reference genome path'
ref_length = 'reference genome length'
genome_name = 'reference genome name'
command = 'python /MixtureS/mixture_model.py --sample_name %s --genome_len %s --genome_name %s --genome_file_loc %s --bam_file %s --res_dir %s' % (file, ref_length, genome_name, ref_name, input_file1, output_path1)

