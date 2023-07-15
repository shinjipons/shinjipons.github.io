import projects_list_generator
import menu_generator

html_code = """
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Shinji Pons</title>
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
        
			<p>Welcome.</p>
            
		</div>

		<div>
        
			<p>I'm a designer.</p>
			
			<ul>Ways to contact me.
				<li><a target="_blank" href="mailto:mail@shinjipons.com">Email</a></li>
				<li><a target="_blank" href="https://linkedin.com/in/shinjipons/">LinkedIn</a></li>
				<li><a target="_blank" href="https://twitter.com/shinjipons/">Twitter</a></li>
				<li><a target="_blank" href="https://read.cv/shinjipons">Read.cv</a></li>
				<li><a target="_blank" href="https://cal.com/shinjipons">Cal.com</a></li>
			</ul>
			
			<ul>This is my work.
                <!-- Insert projects list here -->
				{}
			</ul>
            
            <ul>Previous companies.
				<li>Ragdoll Dynamics</li>
				<li>Electronic Arts</li>
				<li>Autodesk</li>
				<li>Thomson Reuters</li>
				<li>Microsoft</li>
				<li>Ateliers Jean Nouvel</li>
			</ul>

		</div>

	</div>

</body>
</html>
"""

# Formatting the string with the provided values
formatted_html_code = html_code.format(menu_generator.menu_html, projects_list_generator.projects_list_html)

# Create a new HTML file and write the HTML code into it
with open("index.html", "w") as file:
    file.write(formatted_html_code)