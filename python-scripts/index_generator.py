import os
import projects
import projects_list_generator
import menu_generator

all_packery_items = ""

for project in projects.projects_with_descriptions:        

	project_name = project[0]
	project_image_path = project[-1]
	slug = project[2]

	# navigate to the folder of each project
	os.chdir(project_image_path)

	# get the first image from each project
	first_image = os.listdir()[0]
	first_image_path = project_image_path + first_image

	packery_grid_item_html_code = """
    \t<div class="packery-grid-item">
	\t\t<a href="{}">
	\t\t\t<img src="{}" alt="">
	\t\t\t<div class="packery-grid-item-overlay">
	\t\t\t\t<p>{}<p>
    \t\t\t</div>
	\t\t</a>
	\t</div>\n
	"""
    
	formatted_packery_grid_item_html_code = packery_grid_item_html_code.format(slug, first_image_path, project_name)
	all_packery_items += formatted_packery_grid_item_html_code
    
	# Navigate back to the root folder, which is up two levels from the current working directory
	current_dir = os.getcwd()
	parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
	grandparent_dir = os.path.abspath(os.path.join(parent_dir, ".."))
	os.chdir(grandparent_dir)

# The HTML code
html_code = """
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Shinji Pons</title>
	<link rel="stylesheet" href="styles.css" />
    <script src="https://unpkg.com/packery@2/dist/packery.pkgd.min.js"></script>
	<script src="https://unpkg.com/imagesloaded@5/imagesloaded.pkgd.min.js"></script>
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
        
			<p>Welcome.</p>
            
		</div>

		<div>
        
			<p>I'm a designer. I'm currently not taking extra projects.</p>
			
			<ul>Ways to contact me.
				<li><a target="_blank" href="mailto:mail@shinjipons.com">Email</a></li>
				<li><a target="_blank" href="https://linkedin.com/in/shinjipons/">LinkedIn</a></li>
				<li><a target="_blank" href="https://twitter.com/shinjipons/">Twitter</a></li>
				<li><a target="_blank" href="https://read.cv/shinjipons">Read.cv</a></li>
				<li><a target="_blank" href="https://cal.com/shinjipons">Cal.com</a></li>
			</ul>
			
			<ul>My work.
                <!-- Insert projects list here -->
				{}
			</ul>
            
            <ul>Current and previous clients.
				<li>Ragdoll Dynamics</li>
				<li>Electronic Arts</li>
				<li>Autodesk</li>
				<li>Thomson Reuters</li>
				<li>Microsoft</li>
				<li>Ateliers Jean Nouvel</li>
			</ul>

		</div>

	</div>
    
    <div class="packery-grid">
		<!-- insert all div tags with packery-grid-item class -->
		{}
    </div>
    
    <script src="script.js"></script>

</body>
</html>
"""

# Formatting the string with the provided values
formatted_html_code = html_code.format(menu_generator.menu_html, projects_list_generator.projects_list_html, all_packery_items)

# Create a new HTML file and write the HTML code into it
with open("index.html", "w") as file:
    file.write(formatted_html_code)