# This script is to generate the project list

projects = [
    "Ragdoll Dynamics",
    "Louvre Abu Dhabi",
    "LEGO Digital Designer Pro",
    "Autodesk Alias SubD",
    "Dynamo for Alias"
]

for project in projects:
    slug = project.lower().replace(" ", "-") + ".html"
    print("<li><a href=\"" + slug + "\">" + project + "</a></li>")

# print should look like this
# <li><a href="ragdoll.html">Ragdoll Dynamics</a></li>