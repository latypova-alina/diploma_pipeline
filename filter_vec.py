import csv
import pdb

class FilterVec:
  def __init__(self, vec_result):
    self.vec_result = vec_result

  def filter(self):
    with open(self.vec_result, 'r+') as f:
      vectors = f.read()
      last_space = vectors.rfind("\n\n")
      vector = vectors[last_space + 2:]
      f.seek(0)
      f.truncate()
      f.write(vector)
