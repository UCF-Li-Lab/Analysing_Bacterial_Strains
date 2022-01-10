






################################## StrainPhlAn Link ###################3

# Link: https://github.com/biobakery/MetaPhlAn



# Step1:

input_file = 'read1.fastq' + ',' + 'read2.fastq'
output_file1 = 'profile.txt'
output_file2 = 'bowtie2.txt'
output_file3 = 'sam.bz2'
command1 = '/metaphlan2_env/bin/metaphlan2.py %s %s --bowtie2out %s --samout %s --input_type fastq' % (input_file, output_file1, output_file2, output_file3)

# step2:

input_file = 'sam.bz2'
output_path = 'output/'
command2 = '/metaphlan2_env/bin/strainphlan_src/sample2markers.py --ifn_samples %s --input_type sam --output_dir %s' % (input_file, output_path)

# step3:

input_file = 'markers'
output_path1 = 'output/'
output_file = 'clades.txt'
command3 = '/metaphlan2_env/bin/strainphlan.py --ifn_samples %s --output_dir %s --print_clades_only > %s' % (input_file, output_path1, output_file)


# step4:

input_file = 'markers'
output_file = 'output/'
ref_path = 'reference.markers.fasta'
ref_path1 ='reference.fna'
spcies_name = 'species name'
command4 = '/metaphlan2_env/bin/strainphlan.py --ifn_samples %s --ifn_markers %s --ifn_ref_genomes %s --output_dir %s --clades %s --marker_in_clade 0.2' % (input_file, ref_path, ref_path1, output_file, spcies_name)





