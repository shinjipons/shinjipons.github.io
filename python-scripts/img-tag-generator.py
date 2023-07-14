# Script to generate a bunch of <img> tags from a list of reference image files in a specific path

import os

# Go to the folder containing the images
folder_path = "./images"

# Change the current directory to the specified folder
os.chdir(folder_path)

# Get a list of all the filenames in the folder
file_names = os.listdir()

# Print the file names
print("Here is the result:")
for file_name in file_names:
    print("<img src=" + "\"" + folder_path + "/" + file_name + "\"" + " alt=\"\">")