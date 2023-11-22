################################################
### IC Photo Renamer ###########################
### Written by Christopher Eide ################
### 10 January 2023 ############################
### Direct inquiries to ceide@trumbullps.org ###
################################################

import csv, os

CSVFILE = 'C:/Users/ceide/Desktop/Python Scripts/IC Photos/photofiles.csv'
PHOTOSDIR = 'C:/Users/ceide/Desktop/Python Scripts/IC Photos/photos/'

def main():

    # Dictionary for file name lookups
    filenamedict = {}

    # Open the CSV File
    with open(CSVFILE, 'r') as csvfile:
        # Create a dictionary with key-value pairs of current filename -> new filename
        reader = csv.DictReader(csvfile)
        for row in reader:
            currfile = row['FILE_NAME']
            newfile = row['NEW_FILENAME']
            print("currfile: " + currfile)
            print("newfile: " + newfile)
            filenamedict.update( { currfile: newfile } )

    # Iterate through files and rename
    directory = os.fsencode(PHOTOSDIR)

    for file in os.listdir(directory):
        renameFile(file, filenamedict)

def renameFile(file, filenamedict):

    originalname = os.fsdecode(file)
    print("Renaming " + originalname)

    newname = ""
    try:
        if filenamedict[originalname] == "#N/A":
            newname = originalname + "DELETE"
        else:
            newname = filenamedict[originalname]
    except:
        print("File not in dictionary!")
        return

    print("New Name: " + newname)
    try:
        os.rename("photos/" + originalname, "newphotos/" + newname)
    except Exception as e:
        print("ERROR OCCURRED. Ensure there are no duplicate output filenames!")
        print(e)


if __name__=="__main__":
    main()