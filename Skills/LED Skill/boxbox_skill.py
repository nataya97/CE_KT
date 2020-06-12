import subprocess
import os


cmd = './alexaskill.py'
os.system(cmd)

subprocess.Popen(['wc', '-l', './alexaskill.py'], 
           stdout=subprocess.PIPE, 
           stderr=subprocess.STDOUT)
