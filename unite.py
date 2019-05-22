import csv
import pdb

class Unite:
  def __init__(self, origin_test, vec_result, output_folder):
    self.origin_test = origin_test
    self.vec_result = vec_result
    self.output_folder = output_folder

  def unite_resuts(self):
    with open(self.origin_test, 'r+') as file:
      origin_lines_with_spaces = file.readlines()
      origin_lines = []

      for line in origin_lines_with_spaces:
        if len(line) > 2:
          origin_lines.append(line)

    with open(self.vec_result, 'r+') as file:
      predicted_lines = file.readlines()

    i = 0
    predicted_label = predicted_lines[i].split()[1]

    while i < len(origin_lines):
      token = origin_lines[i].split()[0]
      true_label = origin_lines[i].split()[1]

      if (token != predicted_lines[i].split()[0]):
        print("WARNING! Token from gold file and predicted file is not the same at {}".format(i))

      with open("{}/unite_result.txt".format(self.output_folder), "a+") as file:
        file.write("{} {} {}\n".format(token, true_label, predicted_label))

      i+=1

      if i < len(predicted_lines):
        predicted_label = predicted_lines[i].split()[1]

