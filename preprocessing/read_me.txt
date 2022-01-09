

If you only have FastQ format data, you can get a hint from our common preprocessing pipeline. But please check your experimental specification before applying our preprocessing step, because our preprocessing may be not suitable for your specific experiments. So you may need to adjust our preprocessing script based on your own experiments or trim read protocol, like single-end read, trim customized bar code or others.

(1) prerequisite

(A) First, you need to install python (recommend: python 3.6-64bit), which is already installed by default for most of current Linux systems. If there is no python 3.6 installed, you can download and install python from (http://www.python.org/download/). You can use "python -V" command to check whether python is installed and the version of Python.

(B) Install Conda:

https://docs.conda.io/projects/conda/en/latest/user-guide/install/

(C) Bowtie2 2.3 or newer (optional if you are only using our preprocessing script)

Conda install bowtie2

(D) Samtools 1.9 (optional if you are using our preprocessing script)

Conda install samtools=1.9 or https://anaconda.org/bioconda/samtools

(2) Sample command:

python preprocessing.py --sample_name test --pair1 ./example_test_data/test.read1.fastq --pair2 ./example_test_data/test.read2.fastq --process 6 --genome_name ./genomic.fna --res_dir ./test_res_data

--sample_name: sample name

--pair1: forward read for FastQ

--pair2: reverse read for FastQ

--process: # of processor to run

--genome_name: reference genome

--res_dir : result directory
