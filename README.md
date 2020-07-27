# CleanUp_RAW_files
"CleanUp_RAW_files.py" executable script searches for any RAW image files that are left without any corresponding
.jpg files after picture sorting. It MOVES the orphaned files to a "ToDelete_folder" (to be deleted as user wants).

## HOW TO USE:
no compilation or installation is needed.
  
1. drop the CleanUp_RAW_files.py file into the folder you want to clean up.      (it scans all sub-folders!)
2. "open" the .py file with Python.      (Python 3 must be installed in Windows)
3. after the scan, press "y" to confirm that you want to remove all orphaned files.
4. check the "ToDelete_folder" next to the .py file and recycle it as you wish. DONE.


### The logic is:
1. find a recognized RAW or Sidecar file among "Known_RAW_File_types" (add any extensions that you need!)
2. check if there is any .JPG file that _starts_ with the same filename
3. if not, highlight and offer to move away the orphaned RAW/sidecar file for deletion, DONE.


##### made by Sergejs Dombrovskis  for Python 3.8
       Tested on Windows 10, but should work on Linux or other OS.


##### Some known discussions around this or similar issues:
[https://stackoverflow.com/questions/48757748/removing-orphaned-sidecar-files-by-extension](https://stackoverflow.com/questions/48757748/removing-orphaned-sidecar-files-by-extension)
[https://www.lightroomqueen.com/community/threads/finding-and-deleting-jpg-sidecar-files.17747/](https://www.lightroomqueen.com/community/threads/finding-and-deleting-jpg-sidecar-files.17747/)
