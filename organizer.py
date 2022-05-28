from pathlib import Path
import os, shutil, os.path, time


downloadAddress = Path(r'C:\Users\USER\Downloads')

# Scan all suffix in download
oldfileType = list(downloadAddress.glob('*'))
fileType = []
for i in oldfileType:
    suffi = i.suffix
    if suffi not in fileType:
        fileType.append(suffi)

for i in fileType:
    a = i + 'Name'
    # I want to use the string element in a list as variable name
    globals()[a] = list(downloadAddress.glob('*' + i))
    print(globals()[a])
    folderName = i + ' Folder'
    globals()[i] = Path(downloadAddress / folderName)


    # Check the path validity
    if globals()[i].is_dir():
        print('The suffix organizer folder has been created')
    else:
        os.makedirs(globals()[i])

    # Move the file
    for o in globals()[a]:
        shutil.move(o,  globals()[i])

    # # Create an empty list in order to add more last modification time in the following loop
    # oldTimelist = []
    # for o in globals()[a]:
    #     # Get last modification time of a file
    #     rawTime = os.path.getmtime(o)
    #     modificationTime = time.strftime('%m/%Y', time.localtime(rawTime))
    #     oldTimelist.append(modificationTime)
    #
    # # Delete the duplicated element in the oldTimelist to be the newTimelist
    # newTimelist = []
    # for o in oldTimelist:
    #     if o not in newTimelist:
    #         newTimelist.append(o)
    #
    # for o in newTimelist:
    #     dateFolder = globals()[i]  / newTimelist
    #     # Check the path validity
    #     if dateFolder.is_dir():
    #         print('The date organizer folder has been created')
    #     else:
    #         os.makedirs(dateFolder)
    #     subFile = list(globals()[i].glob('*'))
    #     for index, item in enumerate(subFile):
    #         rawTime = os.path.getmtime(item)
    #         if rawTime ==







    print(os.listdir( globals()[i]))