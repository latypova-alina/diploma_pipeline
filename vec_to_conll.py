import csv
import pdb

class VecToConll:
  def __init__(self, vector, original_file, output_folder):
    self.vector = vector
    self.original_file = original_file
    self.output_folder = output_folder
    self.output_file = "{}/absa_conll_result.txt".format(self.output_folder)

  def convert(self):
    predicted_entities = []

    with open(self.vector, 'rt') as csvfile:
      spamreader = csv.reader(csvfile, delimiter=' ', quoting=csv.QUOTE_NONE)
      for row in spamreader:
        predicted_entities.append("{}".format(row[0]))

    with open(self.original_file, 'r+') as file:
      i = 0
      lines = file.readlines()
      while i < len(lines):
        line = lines[i].split()
        with open(self.output_file, "a") as out_file:
          if line[1] == "O":
            out_file.write("{} {}\n".format(line[0], line[1]))
            i += 1
          else:
            if predicted_entities[0] == "1":
              new_label = "{}-ADR".format(lines[i].split()[1][0])
              out_file.write("{} {}\n".format(lines[i].split()[0], new_label))

              i += 1
              while i < len(lines) and lines[i].split()[1] != "O" and lines[i].split()[1][0] != "B":
                new_label = "{}-ADR".format(lines[i].split()[1][0])
                out_file.write("{} {}\n".format(lines[i].split()[0], new_label))

                i += 1
              del predicted_entities[0]
            else:
              new_label = "{}-DIS".format(lines[i].split()[1][0])
              out_file.write("{} {}\n".format(lines[i].split()[0], new_label))

              i += 1
              while i < len(lines) and lines[i].split()[1] != "O" and lines[i].split()[1][0] != "B":
                new_label = "{}-DIS".format(lines[i].split()[1][0])
                out_file.write("{} {}\n".format(lines[i].split()[0], new_label))

                i += 1
              del predicted_entities[0]
