import os
from pages_data import pages as pages_data

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
    page_data['shared_footer'] = shared_footer
    page_data['first_image'] = first_image_tag
    page_data['other_images'] = '\n'.join(other_image_tags)

    # The HTML template with all the placeholders
    html_template = """<!DOCTYPE html>
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
        <div class="two-col-grid">
            <div class="empty-cell"></div>
            <p>{paragraph_1}</p>
            <div class="empty-cell"></div>
            <p>{paragraph_2}</p>
        </div>
    </section>

    <!-- The first image -->    
    <section class="one-col-grid">
        {first_image}
    </section>
    
    <section>
        <div class="two-col-grid">
            <p>{paragraph_3}</p>
            <div class="empty-cell"></div>
            <p>{paragraph_4}</p>
            <div class="empty-cell"></div>
        </div>
    </section>
    
    <!-- All the other images -->    
    <section class="one-col-grid">
        {other_images}
    </section>

    {shared_footer}

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