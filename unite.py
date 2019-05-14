import csv
import pdb

class Unite:
  def __init__(self, vec_result, origin_test):
    self.origin_test = origin_test
    self.vec_result = vec_result

  def unite_resuts(self):
    with open(self.origin_test, 'r+') as file:
      origin_lines = file.readlines()

    with open(self.vec_result, 'r+') as file:
      predicted_lines = file.readlines()

    i = 0
    while i < len(origin_lines):
      token = origin_lines[i].split()[0]
      true_label = origin_lines[i].split()[1]
      predicted_label = predicted_lines[i].split()[1]

      if (token != predicted_lines[i].split()[0]):
        print("WARNING! Token from gold file and predicted file is not the same at {}".format(i))

      with open("data/unite_resut.txt", "a+") as file:
        file.write("{} {} {}\n".format(token, true_label, predicted_label))

      i+=1
