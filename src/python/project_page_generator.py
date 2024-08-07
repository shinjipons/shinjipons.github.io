import os
from pages_data import pages as pages_data

# Set the output folder
OUTPUT_FOLDER = 'dist'

# Create the output folder if it doesn't exist
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

# Function to get all webp images from a specific folder
def get_image_tags(image_folder):
    # Get all webp images and sort them
    files = sorted([f for f in os.listdir("dist/" + image_folder) if f.endswith('.webp')])
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
    page_data['first_image'] = first_image_tag
    page_data['other_images'] = '\n'.join(other_image_tags)

    # The HTML template with all the placeholders
    html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1">
    <title>Shinji Pons | Product Designer of 3D Tools & Beyond | {title}</title>
    <meta name="description"          content="{description}">
    <link rel="stylesheet" href="css/styles.css">
    <meta property="og:url"           content="https://shinjipons.com">
    <meta property="og:type"          content="website">
    <meta property="og:title"         content="Shinji Pons | Product Designer of 3D Tools & Beyond | {title}">
    <meta property="og:description"   content="{description}">
    <meta property="og:image"         content="https://www.shinjipons.com/images/opengraph.jpg">
    <meta name="twitter:card"         content="summary_large_image">
    <meta property="twitter:domain"   content="shinjipons.com">
    <meta property="twitter:url"      content="https://shinjipons.com">
    <meta name="twitter:title"        content="Shinji Pons | Product Designer of 3D Tools & Beyond | {title}">
    <meta name="twitter:description"  content="{description}">
    <meta name="twitter:image"        content="https://www.shinjipons.com/images/opengraph.jpg">
    <link rel="icon" type="image/png" sizes="32x32"   href="/icons/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16"   href="/icons/favicon-16x16.png">
    <link rel="apple-touch-icon"      sizes="180x180" href="/icons/favicon-ios.png">
</head>
<body>
    <nav>
        <div>
            <a class="monospace" href="index.html">Shinji Pons</a>
        </div>
        <div>
            <a class="monospace" href="index.html">Work</a>
            <a class="monospace" href="blog.html">Blog</a>
            <a class="monospace" href="https://shinjipons.com/files/Shinji-Pons-Resume.pdf" target="_blank">Resume</a>
        </div>
        <div>
            <a class="monospace button-call-to-action" href="mailto:website@shinjipons.com">Contact</a>
        </div>
    </nav>
    <main>
        <!-- Left column -->
        <div class="left-column">
            <ul class="monospace padding-between-items">About
                <li>{paragraph_1}</li>
                <li>{paragraph_2}</li>
            </ul>
        </div>
        <!-- Right column -->
        <div class="right-column">
            {first_image}
            {other_images}
            <!-- Next project -->
            <section class="next-project">
                <a href="" id="next-project-link">
                    <h1>Next</h1>
                    <h1 id="next-project-title">Project Title</h1>
                    <img id="next-project-image" src="" alt="">
                </a>
            </section>
        </div>
    </main>
    <script type="text/javascript" src="js/script.js"></script>
</body>
</html>
"""

    formatted_html = html_template.format(**page_data)

    output_path = os.path.join(OUTPUT_FOLDER, f"{page_key}.html")
    # with open(f"{page_key}.html", "w") as html_file:
    with open(output_path, "w") as html_file:
        html_file.write(formatted_html)

# Generate all pages
for page_key, page_data in pages_data.items():
    generate_page(page_key, page_data)