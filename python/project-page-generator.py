# Content to insert in the placeholders
pages_data = {
    "louvre-abu-dhabi": {
        "title": "Louvre Abu Dhabi",
        "paragraph_1": "While at Ateliers Jean Nouvel, I worked on the typographic signage and icon design for the Louvre Abu Dhabi museum. Under the the creative direction of Philippe Apeloig and Clovis Vallois, I sketched, designed and mocked up several physical designs for the typographic system in French, English and Arabic.",
        "paragraph_2": "The graphic designers were in constant collaboration with the architects to decide the size and location of the signage, but also to remove walls where needed to increase signage visibility."
    }
}

shared_footer = """
    <section>
        <div class="four-col-grid">
            <a href="test.html" class="call-to-action two-wide">Get in touch</a>
            <a href="test.html" class="call-to-action two-wide">Book a call</a>
            <a href="https://www.linkedin.com/in/shinjipons/" class="call-to-action" target="_blank">Linkedin</a>
            <a href="https://twitter.com/shinjipons" class="call-to-action" target="_blank">Twitter</a>
            <a href="https://twitter.com/shinjipons" class="call-to-action" target="_blank">Gumroad</a>
            <a href="https://etsy.com/" class="call-to-action" target="_blank">Etsy</a>
        </div>
    </section>"""

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