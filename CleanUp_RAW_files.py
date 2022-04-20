import os
import re
import shutil
# "CleanUp_RAW_files.py" executable script searches for any RAW image files that are left without any corresponding
# .jpg files after picture sorting. It MOVES the orphaned files to a "ToDelete_folder" (to be deleted as user wants).
#
#                               HOW TO USE:
#
#   1- drop the .py file into the folder you want to clean up.      (it scans all sub-folders!)
#   2- "open" the .py file with Python.      (Python must be installed in Windows)
#   3- after the scan, press "y" to confirm that you want to remove all orphaned files.
#   4- check the "ToDelete_folder" next to the .py file and recycle it as you wish. DONE.
#
#
#   made by Sergejs Dombrovskis  for Python 3.8
#       v1.00    2020-07-27             Tested on Windows 10, but should work on Linux or other OS.
#       v1.01    2022-04-20             changed to more robust working directory detection code.
#
# The logic is:
#   1- find a recognized RAW or Sidecar file among "Known_RAW_File_types" (add any extensions that you need!)
#   2- check if there is any .JPG file that _starts_ with the same filename
#   3- if not, highlight and offer to move away the orphaned RAW/sidecar file for deletion, DONE.
#

# add all file types you want to clean away:   file extensions MUST have 4 characters!!!
Known_RAW_File_types = ['.RW2', '.dop']
ToDelete_folder = '- ToDelete_folder'    # name of the folder where all orphaned files will be MOVED for user to delete.

# todo: add search performance optimization
# init various stuff:
os.system("")  # trick to get colored print-outs   https://stackoverflow.com/a/54955094
Text_Color_RED = '\033[31m'
Text_Color_GREEN = '\033[32m'
Text_Color_CYAN = '\033[36m'
Text_Color_RESET = '\033[0m'
root = os.path.dirname(os.path.realpath(__file__))   # not robust enough:  root = os.getcwd()
LastSubFolder = ''  # must be empty string
FilesToRemove = []  # list of files to delete


print('Started Orphan file scanning for file types: ', str(Known_RAW_File_types), '...')
for directory, subdir_list, file_list in os.walk(root):
    print('Searching for orphans in Directory:', directory)
    for name in subdir_list:
        print('found a Sub-Directory:', name)

    # noinspection SpellCheckingInspection
    for Fname in file_list:
        if Fname[-4:] in Known_RAW_File_types:
            wildName = '^' + Fname[:-4] + '.*(\\.jp)'   # search for any matching .JPG, .jpg, .jpeg file
            OrphanageTest = any(re.match(wildName, elem, flags=re.IGNORECASE) for elem in file_list)
            if OrphanageTest:
                print(Text_Color_GREEN, 'RAW match:', Fname)
            else:
                print(Text_Color_RED, 'To DELETE:', Fname)
                FilesToRemove.append(os.path.join(directory, Fname))

        else:
            print(Text_Color_GREEN, '  OK file:', Fname)

    print(Text_Color_RESET + " ")

print("   SCAN COMPLETE  ")
print("  ")
Go_NoGo = str(input(Text_Color_CYAN + 'Do you want to REMOVE the ' + str(len(FilesToRemove)) + ' orphaned files? '
                                                                                               '(y/n): '))
Go_NoGo = Go_NoGo.lower()
if Go_NoGo.startswith("y"):
    for MoveAwayThis in FilesToRemove:  # Remove the files one by one.
        # os.remove(MoveAwayThis)  is not used, because it does not send files to Recycle Bin!:

        PathAndFilename = os.path.split(MoveAwayThis)
        SubFolder = os.path.split(PathAndFilename[0])
        if LastSubFolder != SubFolder[1]:
            MoveTo_DIR_Path = os.path.join(root, ToDelete_folder, SubFolder[1])
            os.makedirs(MoveTo_DIR_Path, exist_ok=True)     # create folder to move files to
            LastSubFolder = SubFolder[1]

        MoveToPath = os.path.join(root, ToDelete_folder, SubFolder[1], PathAndFilename[1])
        shutil.move(MoveAwayThis, MoveToPath)   # make the move

    print(Text_Color_GREEN, 'All Orphaned files were MOVED to "', os.path.join(root, ToDelete_folder), '"')
else:
    print(Text_Color_CYAN, 'Completed Orphan file scanning without any file changes.')

input(Text_Color_GREEN + 'DONE.  Hit Enter to exit   :)')

#
#
#
# Copyright 2020 Sergejs (and all contributors)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
