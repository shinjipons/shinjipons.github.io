from pages_data import pages as pages_data

# Read the shared footer from a file
with open('python/shared_footer.html', 'r') as file:
    shared_footer = file.read()

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shinji Pons - {title}</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>

    <nav>
        <div class="inner-section">
            <div>
                <a href="index.html">Close</a>
            </div>
            <div>
                <p>{title}</p>
            </div>
        </div>
    </nav>

    <section>
        <div>
            <p>{paragraph_1}</p>
        </div>
    </section>

    <!-- Pack 1 images -->    
    <section class="one-col-grid">
        <img src="https://picsum.photos/2000/1200">
        <img src="https://picsum.photos/2000/1600">
    </section>
    
    <section>
        <p>{paragraph_2}</p>
    </section>
    
    <!-- Pack 2 images -->    
    <section class="one-col-grid">
        <img src="https://picsum.photos/2000/800">
        <img src="https://picsum.photos/800/1200">
        <img src="https://picsum.photos/900/600">
        <img src="https://picsum.photos/800/1400">
    </section>

    {shared_footer}

</body>
</html>"""

# You can then generate each page by using the key for that page
def generate_page(page_key):
    page_data = pages_data.get(page_key)
    if page_data is not None:
        page_data['shared_footer'] = shared_footer
        formatted_html = html_template.format(**page_data)
        with open(f"{page_key}.html", "w") as html_file:
            html_file.write(formatted_html)
        print(f"{page_key.capitalize()} page created successfully!")
    else:
        print(f"No data found for the {page_key} page.")

# Generate all pages
for page_key in pages_data.keys():
    generate_page(page_key)