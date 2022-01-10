







############################# MetaSNV Link #################################

# Link: https://metasnv.embl.de/


sample_file = 'input file location'
ref_name = 'reference genome file'


command = 'python metaSNV.py %s %s %s --threads 8' % ('/result',sample_file,ref_name)