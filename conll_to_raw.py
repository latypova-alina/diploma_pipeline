import csv
import pdb

class Raw:
  def __init__(self, ner_result):
    self.ner_result = ner_result
    self.new_filename = "data/test.raw"

  def convert(self):
    with open(self.ner_result, 'r+') as file:
      lines_counter = 0
      lines = file.readlines()

      while lines_counter < len(lines)-1:
        #read text part as array of tokens and entities
        text_part_array = []
        while lines_counter < len(lines)-1 and lines[lines_counter][0] != ".":
          text_part_array.append(lines[lines_counter][0:-1])
          lines_counter += 1

        text_part_array.append(lines[lines_counter][0:-1])

        if lines[lines_counter][0] == ".":
          lines_counter += 1

        entities_count = 0
        for token_entity in text_part_array:
          entity = token_entity.split()[1]
          if entity == "B-DIS" or entity == "B-ADR":
            entities_count += 1

        for i in range(0, entities_count):
          token_entity_count = 0
          full_entity = ""
          entity_written = False
          entity_name = "0"

          with open(self.new_filename, "a") as out_file:
            while token_entity_count < len(text_part_array):

              token = text_part_array[token_entity_count].split()[0]
              entity = text_part_array[token_entity_count].split()[1]

              if entity[2:] != "DIS" and entity[2:] != "ADR" or entity_written == True:
                out_file.write("{} ".format(token))
                token_entity_count += 1
              else:
                entity_written = True
                out_file.write("$T$ ".format(token))

                full_entity += text_part_array[token_entity_count].split()[0]

                if entity[2:] == "DIS":
                  entity_name = "0"
                  text_part_array[token_entity_count] = "{} {}".format(text_part_array[token_entity_count].split()[0], "O")
                elif entity[2:] == "ADR":
                  entity_name = "1"
                  text_part_array[token_entity_count] = "{} {}".format(text_part_array[token_entity_count].split()[0], "1")

                token_entity_count += 1

                # Check if token is the last in sentence
                if token_entity_count != len(text_part_array):
                  while token_entity_count < len(text_part_array) and text_part_array[token_entity_count].split()[1] == "I-DIS":
                    full_entity += " {}".format(text_part_array[token_entity_count].split()[0])
                    text_part_array[token_entity_count] = "{} {}".format(text_part_array[token_entity_count].split()[0], "O")

                    token_entity_count += 1

                  while token_entity_count < len(text_part_array) and text_part_array[token_entity_count].split()[1] == "I-ADR":
                    full_entity += " {}".format(text_part_array[token_entity_count].split()[0])
                    text_part_array[token_entity_count] = "{} {}".format(text_part_array[token_entity_count].split()[0], "1")

                    token_entity_count += 1

            out_file.write("\n{}".format(full_entity))
            out_file.write("\n{}".format(entity_name))
            out_file.write("\n")
