import os
import re
import pdb

DATA_FOLDER = "../../src/diploma/pipeline/data"
NER_DIR = "../../../NeuroNER-master"
NER_OUT_DIR = "../../src/diploma/pipeline/output/new_dir"

os.system("cd {}/src && python3.6 main.py --dataset_text_folder={} --output_folder={}".format(NER_DIR, DATA_FOLDER, NER_OUT_DIR))

ner_output_folders = []

for dirpath, dirnames, filenames in os.walk("/home/alina/src/diploma/pipeline/output/new_dir"):
  ner_output_folders = ner_output_folders + [dirname for dirname in dirnames if re.compile("data_2019").match(dirname)]
