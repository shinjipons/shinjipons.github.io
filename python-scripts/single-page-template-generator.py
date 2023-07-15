import os

project_title = "Template"
project_description = "The mesmerizing dance of autumn leaves, carried by the whimsical wind, creates a vibrant tapestry of colors on the forest floor. Nature's brushstrokes paint a breathtaking landscape, as golden hues mingle with fiery reds and rustic oranges. It's a fleeting masterpiece, reminding us of the beauty in transition and the passage of time."

slug = project_title.lower().replace(" ", "-")
images_folder_path = "./images/" + slug

# Navigate to the corresponding images folder
os.chdir(images_folder_path)

# Create all the <img> tags from all the images in that folder
images_file_names = os.listdir()
image_tags = ""

for image_file_name in images_file_names:
    image_tags += ("<img src=" + "\"" + images_folder_path + "/" + image_file_name + "\"" + " alt=\"\">\n\t\t\t")

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

    <!-- This is the navigation, to "templatize" later -->
    <div class="grid">

        <div>
            <p>Shinji Pons</p>
        </div>
    
        <div>
            <ul>
                <li><a href="index.html">Work</a></li>
                <li><a href="about.html">About</a></li>
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

            <!-- All project images go here -->
            {}
        </div>
    </div>
</body>
</html>
"""

# Formatting the string with the provided values
formatted_html_code = html_code.format(project_title, project_title, project_description, image_tags)

# Navigate to the root folder, which is up two levels from the current working directory
current_dir = os.getcwd()
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
grandparent_dir = os.path.abspath(os.path.join(parent_dir, ".."))
os.chdir(grandparent_dir)
updated_dir = os.getcwd()

# Create a new HTML file and write the HTML code into it
with open("template.html", "w") as file:
    file.write(formatted_html_code)