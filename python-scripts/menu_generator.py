# Right now I only have the "Projects" item

menu_items = [["Projects", "index"]]

menu_html = ""

for item in menu_items:
    
    if item == menu_items[-1]:
        # no new line character needed
        item_html = "<li><a href=\"" + item[1] + ".html\"" + ">" + item[0] + "</a></li>\t\t\t\t"
    else: 
        item_html = "<li><a href=\"" + item[1] + ".html\"" + ">" + item[0] + "</a></li>\n\t\t\t\t"

    menu_html += item_html