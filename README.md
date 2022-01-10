# StrainToolSurvey

The pipeline codes here are used in the paper 'Computational analyses of baterial strains from shotgun reads' by Minerva Fatimae Ventolero and Saidi Wang from UCF.

# 1. Simulation data

(1) First of all, you need to install the simulation tool----dwgsim
Link:  https://github.com/nh13/DWGSIM

(2) The code is run in the python2.7 (You could update the code to use python3.6 but we use python 2.7 code here to make it consistent with the paper)

You need to install python (recommend: python 2.7.x-64bit), which is already installed by default for most of current Linux systems. If there is no python 2.7 installed, you can download and install python from (http://www.python.org/download/). You can use "python -V" command to check whether python is installed and the version of Python.

(3) You need to modify the path of each file based on your location computer.

For example:

'/dwgsim/simulated_data_with_evolutionary_relationship/data/original_genome/' ------> 'Your own path/original_genome/'

As in the paper, we will have 184 GB of simulation data. If you want to generate the corresponding simulation dataset, you could get it using the pipeline here. Also I just upload one example for each of the Sh and USh type dataset to the following link:

Link: https://doi.org/10.6084/m9.figshare.18092846


# 2. Preprocessing

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

# 3. Figures in paper

Tools used

(1) python=3.6 If there is no python 3.6 installed, you can download and install python from (http://www.python.org/download/). You can use "python -V" command to check whether python is installed and the version of Python.

(2) Install Conda:

https://docs.conda.io/projects/conda/en/latest/user-guide/install/

(3) matplotlib

conda install -c conda-forge matplotlib

(4) numpy

conda install -c anaconda numpy

(5) pandas

conda install -c anaconda pandas

(6) seaborn

conda install -c anaconda seaborn

# 4. Benchmark tools code.

We just put the command to run each of the six tools in the paper in different python file. ANd you could check them and run them after you installed the six tools

(1) BHap running code

/benchmark_tools_code/1-BHap_code.py

(2) EVORhA running code

/benchmark_tools_code/2-EVORhA_code.py

(3) MetaSNV running code

/benchmark_tools_code/3-MetaSNV_code.py

(4) mixtureS running code

/benchmark_tools_code/4-mixtureS_code.py

(5) strainFinder running code

/benchmark_tools_code/5-strainFinder_code.py

(6) StrainPhIAn running code

/benchmark_tools_code/6-StrainPhlAn_code.py


# 5. Contact Information

Please do not hesitate to reach out to me if you have questions.

Saidi Wang (tjwangsaidi@knights.ucf.edu)

Minerva Fatimae Ventolero (mventolero@knights.ucf.edu)

Haiyan Nancy Hu (haihu@cs.ucf.edu)

Xiaoman Shawn Li (xiaoman@mail.ucf.edu)
