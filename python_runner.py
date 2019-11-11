# Importing subprocess 
import subprocess

def run(filename):
  # Your command 
  cmd = "python {}".format(filename)

  # Starting process
  process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

  # Getting the output and errors of the program
  stdout, stderr = process.communicate()
  # Printing the errors 

  # print("stdout: ", stdout)
  # print("stderr: ", stderr)

  sentence = stderr.split()
  errormsg = ""
  capture = False
  for i in range (len(sentence)):
    if "Error" in sentence[i]:
      errormsg += sentence[i]
      capture = True
    elif capture:
      errormsg += " " + sentence[i]

  return {
    'stdout': stdout,
    'stderr': stderr,
    'customerror': errormsg
  }
