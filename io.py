import pymatgen
from pymatgen.io import pwscf
import numpy as np
import subprocess
import os

'''Inputs/Outputs for files. For semi-automated running of Quantum Espresso Cacluations'''

def get_parallel_bash_string(num_processors=1,num_cores=1,parallel_type = "mpi"):
    '''Returns a string for bash command for parallelization'''
    parallel_str =  ""
    if parallel_type == "mpi":
        parallel_str = "mpirun -np "+str(num_processors)
    elif parallel_type == "openmp":
        parallel_str = "export OMP_NUM_THREADS="+str(num_cores)
    return parallel_str
class QESimulation():
    def __init__(self,input_path):
        self.input_file = input_path
        self.pw_input= pwscf.PWInput.from_file(self.input_file)
        filename_base, ext = os.path.splitext(self.input_file)
        self.output_filename = filename_base+".out"
        self.output = None
    def run(self,num_processsors =1,num_cores = 1,parallel_types = ["mpi"]):
        '''Runs the Quantum Espresso simulation'''
        initialiazation_commands = []
        if "openmp" in parallel_types:
            initialiazation_commands.append(get_parallel_bash_string(num_cores=num_cores,parallel_type="openmp"))
        if "mpi" in parallel_types:
            run_prefix = get_parallel_bash_string(num_processors=num_processsors,parallel_type="mpi")
        pwscf_str = run_prefix+" pw.x -i "+self.input_file+" > "+self.output_filename
        for command in initialiazation_commands:
            subprocess.run(command,shell=True)
        subprocess.run(pwscf_str,shell=True)
        self.output = pwscf.PWOutput(self.output_filename)




