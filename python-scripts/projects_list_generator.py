import projects

projects_list_html = ""

for project in projects.projects_with_descriptions:
    project_title = project[0]
    project_slug = project[2]
    project_list_item = "<li><a href=\"" + project_slug + "\">" + project_title + "</a></li>\n\t\t\t\t"
    projects_list_html += project_list_item