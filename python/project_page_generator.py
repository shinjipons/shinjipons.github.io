import os
from pages_data import pages as pages_data

# Read the shared footer from a file
with open('python/shared_nav.html', 'r') as file:
    shared_nav = file.read()

# Read the shared footer from a file
with open('python/shared_footer.html', 'r') as file:
    shared_footer = file.read()

# Function to get all webp images from a specific folder
def get_image_tags(image_folder):
    # Get all webp images and sort them
    files = sorted([f for f in os.listdir(image_folder) if f.endswith('.webp')])

    # Separate the first image if the list is not empty
    first_img_tag = ''
    other_img_tags = []
    if files:
        # Generate the img tag for the first image
        first_img_tag = f'<img src="{image_folder}/{files[0]}">'
        # Generate img tags for the rest of the images
        other_img_tags = [
            f'\t\t<img src="{image_folder}/{file}">' for file in files[1:]
        ]
    # Purely cosmetic: the first image tag needs more tab spaces
    other_img_tags[0] = other_img_tags[0].replace("\t\t", "")

    return first_img_tag, other_img_tags

# You can then generate each page by using the key for that page
def generate_page(page_key, page_data):
    image_folder = page_data.get('image_folder', '')
    first_image_tag, other_image_tags = get_image_tags(image_folder) if image_folder else ('', [])

    # Include the shared HTML block, the first image, and other image tags in the page data dictionary
    page_data['shared_nav'] = shared_nav
    page_data['shared_footer'] = shared_footer
    page_data['first_image'] = first_image_tag
    page_data['other_images'] = '\n'.join(other_image_tags)

    # The HTML template with all the placeholders
    html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1">
    <title>Shinji Pons - {title}</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="icon" type="image/png" sizes="32x32" href="/icons/favicon-32x32.png">
	<link rel="icon" type="image/png" sizes="16x16" href="/icons/favicon-16x16.png">
	<link rel="apple-touch-icon" sizes="180x180"    href="/icons/favicon-ios.png">
    <meta property="og:image" content="https://www.shinjipons.com/images/opengraph.png" />
	<meta property="og:title" content="Shinji Pons | Product Designer | {title}" />
	<meta property="og:description" content="A multi-disciplinary experience designer for software applications" />
	<meta property="og:url" content="https://www.shinjipons.com/" />
	<meta property="og:type" content="website" />
</head>
<body>

    {shared_nav}

    <!-- The first image -->
    <section class="one-col-grid">
        {first_image}
    </section>

    <section>
        <div class="eight-col-grid project-text-block">
            <div class="project-text">
                <h1 class="monospace">About</h1>
                <p>{paragraph_1}</p>
                <p>{paragraph_2}</p>
                <h1 class="monospace">My role</h1>
                <p>{paragraph_3}</p>
                <p>{paragraph_4}</p>
            </div>
        </div>
    </section>

    <!-- All the other images -->
    <section class="one-col-grid">
        {other_images}
    </section>

    <!-- Next project -->
    <section class="next-project">
        <a href="" id="next-project-link">
            <h1>Next</h1>
            <h1 id="next-project-title">Project Title</h1>
            <img id="next-project-image" src="" alt="">
        </a>
    </section>

    {shared_footer}

    <script type="text/javascript" src="script.js"></script>

</body>
</html>
"""

    formatted_html = html_template.format(**page_data)

    with open(f"{page_key}.html", "w") as html_file:
        html_file.write(formatted_html)
    print(f"{page_key.capitalize()} page created successfully!")

# Generate all pages
for page_key, page_data in pages_data.items():
    generate_page(page_key, page_data)