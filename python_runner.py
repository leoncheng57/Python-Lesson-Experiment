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

  helpful = ""
  anthro = ""
  if "SyntaxError" in errormsg and "if" in stderr and "=" in stderr and "==" not in stderr:
    helpful = "Remember that how we check if something is equal is different than assigning a value to a variable!"
    anthro = "You're doing great! Don't worry, this is not a huge deal. " + helpful + " You can do it!"
  elif "SyntaxError" in errormsg and ("if" in stderr or "else" in stderr):
    helpful = "How do we mark the end of an if statement?"
    anthro = "Awesome job with the " + ("else" if "else" in stderr else "if") + " statement so far! " + helpful + " You're almost there!"
  elif "NameError" in errormsg:
    name = ""
    for i in range (len(sentence)):
      if sentence[i][0] == "'":
        name = sentence[i][1:-1]
    helpful = "The variable " + name + " is not defined - it should either have a value assigned to it, or maybe it isn't a variable? How could you change this to assign a value or make it a value?"
    anthro = "Keep going! " + helpful + " You can do it!"

  if stderr == "" and stdout == "It is Monday":
    helpful = ""
    anthro = "Yay! You did it!"
  elif stderr == "" and stdout == "":
    helpful = "Make sure you are printing something out! Remember to use the print keyword!"
    anthro = helpful + "You're so close!"
  elif stderr == "" and len(stdout) > 1:
    helpful = "How can we use if/elif/else statements to make only one statement print out?"
    anthro = "Great job printing this all out! " + helpful

  return {
    'stdout': stdout,
    'stderr': stderr,
    'helpfulerror': helpful,
    'anthroerror': anthro
  }
