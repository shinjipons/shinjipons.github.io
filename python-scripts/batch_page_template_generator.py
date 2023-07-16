# This script will generate multiple html pages using a pre-made template

# for each project, I need: 
# [0] a project title
# [1] a project description
# [2] a slug
# [3] an image folder path

import os
import projects
import menu_generator

# Calling the variables
projects_with_descriptions_slugs_and_folder_paths = projects.projects_with_descriptions

for project in projects_with_descriptions_slugs_and_folder_paths:
    slug = project[2]
    images_folder_path = project[3]

    # Navigate to the corresponding images folder
    os.chdir(images_folder_path)

    # Create all the <img> tags from all the images in that folder
    images_file_names = os.listdir()
    image_tags = ""

    for image_file_name in images_file_names:
        if image_file_name == images_file_names[-1]:
            # no new line character needed
            image_tags += "<img src=" + "\"" + images_folder_path + image_file_name + "\"" + " alt=\"\">\t\t\t\t"
        else:
            image_tags += "<img src=" + "\"" + images_folder_path + image_file_name + "\"" + " alt=\"\">\n\t\t\t\t"

    # The actual HTML code
    html_code = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <!-- project title goes here -->
        <title>{}</title>
        <link rel="stylesheet" href="styles.css" />
    </head>
    <body>

        <div class="grid">
            <div>
                <p>Shinji Pons</p>
            </div>
            <div>
                <ul>
                    <!-- Insert menu here -->
                    {}
                </ul>
            </div>
        </div>

        <div class="grid">
            <div>
                <!-- project title goes here -->
                <p>{}</p>
            </div>
            <div>
                <!-- project description goes here -->
                <p>{}</p>

                <!-- all project images go here -->
                {}
            </div>
        </div>
        
    </body>
    </html>
    """

    # Formatting the string with the provided values
    formatted_html_code = html_code.format(project[0], menu_generator.menu_html, project[0], project[1], image_tags)

    # Navigate to the root folder, which is up two levels from the current working directory
    current_dir = os.getcwd()
    parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
    grandparent_dir = os.path.abspath(os.path.join(parent_dir, ".."))
    os.chdir(grandparent_dir)
    updated_dir = os.getcwd()

    # Create a new HTML file and write the HTML code into it
    with open(slug, "w") as file:
        file.write(formatted_html_code)