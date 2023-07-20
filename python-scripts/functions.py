import os

def generate_img_tags_from_path(path):
    # Navigate to the folder
    os.chdir(path)

    # Create a list with all the files in that folder
    images_file_names = os.listdir()
    image_tags = ""

    for image_file_name in images_file_names:
        # Default behavior. Do not add a class to the image tags
        if image_file_name == images_file_names[-1]:
            # no new line character needed
            image_tags += "<img src=" + "\"" + path + image_file_name + "\"" + " alt=\"\">\t\t\t\t"
        else:
            image_tags += "<img src=" + "\"" + path + image_file_name + "\"" + " alt=\"\">\n\t\t\t\t"
      
    # Navigate back to the root folder, which is up two levels from the current working directory
    current_dir = os.getcwd()
    parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
    grandparent_dir = os.path.abspath(os.path.join(parent_dir, ".."))
    os.chdir(grandparent_dir)
    
    return image_tags