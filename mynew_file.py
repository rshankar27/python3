#!/export/anaconda3/bin/python

import os
import glob

os.chdir("/export")
for file1 in glob.glob("*.json"):
    file_name = os.path.splitext(file1)[0]
    extension = os.path.splitext(file1)[1]
    new_file_name = file_name[:-6] + extension
    try:
        os.rename(file1, new_file_name)
    except OSError as e:
        print(e)
    else:
        print("Renamed {} to {}".format(file1, new_file_name))
