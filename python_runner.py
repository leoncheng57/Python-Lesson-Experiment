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

    
  def checklines (lines, truelst, falselst):
    for i in range (len(lines)):
      for j in range (len(truelst)):
        line = 0
        for k in range (len(truelst[j])):
          if len(falselst) == 0:
            if truelst[j][k] in lines[i]:
              return True
              line = i
          else:
            for l in range (len(falselst)):
              if truelst[j][k] in lines[i] and falselst[l] not in lines[i]:
                return True
                line = i
    return False

  sentence = stderr.split()
  lines = stderr.split("\n")
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
  if "SyntaxError" in errormsg and checklines(lines, [["if", "else", "elif"], ["="]], ["=="]):
    helpful = "Remember that how we check if something is equal is different than assigning a value to a variable!"
    anthro = "You're doing great! Don't worry, this is not a huge deal. " + helpful + " You can do it!"
  elif "SyntaxError" in errormsg and checklines(lines, [["if", "else", "elif"], ["==="]], []):
    helpful = "The two options are = or == to either assign a value or check equality!"
    anthro = "Remember the two operators we learned! " + helpful + " Keep going!"
  elif "SyntaxError" in errormsg and checklines(lines, [["if","else","elif"]], [":"]):
    helpful = "How do we mark the end of an if statement?"
    anthro = "Awesome job with this if/elif/else statement so far! " + helpful + " You're almost there!"
  elif "NameError" in errormsg:
    name = ""
    for i in range (len(sentence)):
      if sentence[i][0] == "'":
        name = sentence[i][1:-1]
    helpful = "The variable " + name + " is not defined - it should either have a value assigned to it, or maybe it isn't a variable?"
    anthro = "Keep going! " + helpful
  elif "SyntaxError" in errormsg and checklines(lines, [[":"], ["=="]], ["if", "else", "elif"]):
    helpful = "Don't forget to use the if/elif/else keywords for each different case!"
    anthro = "Great start with your conditional statement! " + helpful + " Just add those key words!"
  elif "IndentationError" in errormsg:
    helpful = "Remember to make all your code indented the same amount, and to only indent when you are inside an if/elif/else statement!"
    anthro = "Indenting can be tricky! " + helpful + " You got this!"

  output = stdout.split("\n")

  if stderr == "" and stdout == "":
    helpful = "Make sure you are printing something out! Remember to use the print keyword!"
    anthro = helpful + "You're so close!"
  elif stderr == "" and len(output) > 2:
    helpful = "How can we use if/elif/else statements to make only one statement print out?"
    anthro = "Great job printing this all out! " + helpful

  return {
    'stdout': stdout,
    'stderr': stderr,
    'customerror': anthro # or helpful
  }
