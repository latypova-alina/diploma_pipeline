import csv
import pdb

class Filter:
  def __init__(self, ner_result):
    self.ner_result = ner_result
    self.filtered_file = self.ner_result[:-4] + "_filtered.txt"

  def filter(self):
    with open(self.ner_result, "rt") as csvfile:
      spamreader = csv.reader(csvfile, delimiter=' ', quoting=csv.QUOTE_NONE)
      for row in spamreader:
        filtered_string = [x for x in row if x]

        with open(self.filtered_file, "a") as csv_file:
          writer = csv.writer(csv_file, delimiter=' ')

          if len(filtered_string) != 0:
            del(filtered_string[1])
            del(filtered_string[1])
            del(filtered_string[1])
            writer.writerow(filtered_string)

