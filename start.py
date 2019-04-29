import os
import re
import pdb
from filter import Filter
from conll_to_raw import Raw

DATA_FOLDER = "../../src/diploma/pipeline/data"
NER_DIR = "../../../NeuroNER-master"
NER_OUT_DIR = "../../src/diploma/pipeline/output/new_dir"
FULL_OUTPUT_PATH = "/home/alina/src/diploma/pipeline/output/new_dir"
EPOCHS_NUM = 0
ABSA_TRAIN_DIR = "/home/alina/src/ABSA-PyTorch/datasets/medicine/train.raw"
ABSA_DIR = "/home/alina/src/ABSA-PyTorch"
PIPELINE_PATH = "/home/alina/src/diploma/pipeline"

# os.system("cd {}/src && python3.6 main.py --dataset_text_folder={} --output_folder={} --maximum_number_of_epochs={}".format(NER_DIR, DATA_FOLDER, NER_OUT_DIR, EPOCHS_NUM))

#return last created ner folder
def ner_output_folder(ner_output_folders = []):
  for dirpath, dirnames, filenames in os.walk("/home/alina/src/diploma/pipeline/output/new_dir"):
    ner_output_folders = ner_output_folders + [dirname for dirname in dirnames if re.compile("data_2019").match(dirname)]

  return ner_output_folders[-1]

#by default the last epochs test_file is taken
def ner_output_test_file(ner_output_test_file = []):
  output_folder = "{}/{}".format(FULL_OUTPUT_PATH, ner_output_folder())

  for dirpath, dirnames, filenames in os.walk(output_folder):
    #hardcode attention
    ner_output_test_file = ner_output_test_file + [filename for filename in filenames if re.compile("00{}_test.txt".format(EPOCHS_NUM)).match(filename)]

  return output_folder + "/" + ner_output_test_file[0]

filter = Filter(ner_output_test_file())
filtered_file = filter.filtered_file
filter.filter()

converter = Raw(filtered_file)
converter.convert()
raw_filename = "{}/data/test.raw".format(PIPELINE_PATH)

pdb.set_trace()

#copy test and train files to absa directory
os.system("cd {}/datasets && mkdir -p new_dataset && cd new_dataset && cp {} test.raw && cp {} train.raw"
  .format(ABSA_DIR, raw_filename, ABSA_TRAIN_DIR))

