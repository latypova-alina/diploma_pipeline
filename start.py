import os
import re
import pdb

DATA_FOLDER = "../../src/diploma/pipeline/data"
NER_DIR = "../../../NeuroNER-master"
NER_OUT_DIR = "../../src/diploma/pipeline/output/new_dir"
EPOCHS_NUM = 0

os.system("cd {}/src && python3.6 main.py --dataset_text_folder={} --output_folder={} --maximum_number_of_epochs={}".format(NER_DIR, DATA_FOLDER, NER_OUT_DIR, EPOCHS_NUM))

#return last created ner folder
def ner_output_folder(ner_output_folders = []):
  for dirpath, dirnames, filenames in os.walk("/home/alina/src/diploma/pipeline/output/new_dir"):
    ner_output_folders = ner_output_folders + [dirname for dirname in dirnames if re.compile("data_2019").match(dirname)]

  return ner_output_folders[-1]

#by default the last epochs test_file is taken
def ner_output_test_file(ner_output_test_file = []):
  for dirpath, dirnames, filenames in os.walk("/home/alina/src/diploma/pipeline/output/new_dir/{}".format(ner_output_folder())):
    #hardcode attention
    ner_output_test_file = ner_output_test_file + [filename for filename in filenames if re.compile("00{}_test.txt".format(EPOCHS_NUM)).match(filename)]

  return ner_output_test_file[0]

ner_output_test_file()
