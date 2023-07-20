# This script will generate multiple html pages using a pre-made template

import projects
import menu_generator
import functions

# Calling the variables
projects_with_descriptions_slugs_and_folder_paths = projects.projects_with_descriptions

for project in projects_with_descriptions_slugs_and_folder_paths:
    slug = project[2]
    images_folder_path = project[3]
    image_tags_for_project_page = functions.generate_img_tags_from_path(images_folder_path)

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
    formatted_html_code = html_code.format(project[0], menu_generator.menu_html, project[0], project[1], image_tags_for_project_page)

    # Create a new HTML file and write the HTML code into it
    with open(slug, "w") as file:
        file.write(formatted_html_code)

print("End of script execution.")