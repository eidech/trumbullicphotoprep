################################################
### IC Photo Renamer ###########################
### Written by Christopher Eide ################
### 10 January 2023 ############################
### Direct inquiries to ceide@trumbullps.org ###
################################################

import csv, os

CSVFILE = 'photofiles.csv'
PHOTOSDIR = 'photos/'

def main():
    # Get the current script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Make the paths for files/directories
    csv_file_path = os.path.join(script_dir, CSVFILE)
    photos_dir_path = os.path.join(script_dir, PHOTOSDIR)

    # Dictionary for file name lookups
    filenamedict = {}

    # Open the CSV File
    with open(csv_file_path, 'r') as csvfile:
        # Create a dictionary with key-value pairs of current filename -> new filename
        reader = csv.DictReader(csvfile)
        for row in reader:
            currfile = row['FILE_NAME']
            newfile = row['NEW_FILENAME']
            print("currfile: " + currfile)
            print("newfile: " + newfile)
            filenamedict.update( { currfile: newfile } )

    # Iterate through files and rename
    directory = os.fsencode(photos_dir_path)

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