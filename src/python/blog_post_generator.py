import os

# The global variables
OUTPUT_FOLDER_BLOG_POSTS = 'dist/blog'
OUTPUT_FOLDER_BLOG_INDEX = 'dist/'
markdown_src_directory   = "src/markdown"

# CSS classes
ul_list_item_class       = "bullet-point-list-item"
ol_list_item_class       = "numbered-list-item"
quote_line_class         = "blog-callout-block"
code_block_class         = "blog-code-block"
blog_article_item_class  = "blog-article-item"
post_date_class          = "blog-post-date"

# Create the output folder if it doesn't exist
if not os.path.exists(OUTPUT_FOLDER_BLOG_POSTS):
    os.makedirs(OUTPUT_FOLDER_BLOG_POSTS)

# Utility functions
def get_all_markdown_filepaths(directory_path):
    if not os.path.isdir(directory_path):
        raise ValueError(f"The specified path is not a directory: {directory_path}")

    # Ger all markdown files in the directory
    markdown_filepaths = [f"{directory_path}/{f}" for f in os.listdir(directory_path) if f.endswith('.md')]

    return markdown_filepaths

def extract_parentheses(string):
    start = string.find('(')
    if start != -1: # Check if '(' is found
        end = string.find(')', start)
        if end != -1: # Check if ')' is found
            return string[start + 1 : end]
    return None # Return None if parentheses are not found

def extract_brackets(string):
    start = string.find('[')
    if start != -1: # Check if '(' is found
        end = string.find(']', start)
        if end != -1: # Check if ')' is found
            return string[start + 1 : end]
    return None # Return None if parentheses are not found

def replace_link(text):
    start = 0
    result = ""
    while True:
        # Find the next markdown link
        open_bracket = text.find('[', start)
        if open_bracket == -1:
            result += text[start:]
            break

        close_bracket = text.find(']', open_bracket)
        open_paren = text.find('(', close_bracket)
        close_paren = text.find(')', open_paren)

        if -1 in (close_bracket, open_paren, close_paren):
            result += text[start:]
            break

        # Extract link text and URL
        link_text = text[open_bracket + 1:close_bracket]
        link_url = text[open_paren + 1:close_paren]

        # Add text before the link and the converted link
        result += text[start:open_bracket]
        result += f'<a href="{link_url}" target="_blank">{link_text}</a>' # Make links open in new tab

        # Move start to after this link
        start = close_paren + 1
    return result

def replace_bold(text):
    i = 0
    result = ""
    while i < len(text):
        if text[i:i+2] == '**':
            j = i + 2
            while j < len(text) and text[j:j+2] != '**':
                j += 1
            if j < len(text):
                # Add <b> and </b> around the bold text
                result += '<b>' + text[i+2:j] + '</b>'
                i = j + 2
            else:
                result += text[i:]
                break
        else:
            result += text[i]
            i += 1
    return result

def replace_italics(text):
    i = 0
    result = ""
    while i < len(text):
        if text[i:i+2] == '*':
            j = i + 2
            while j < len(text) and text[j:j+2] != '*':
                j += 1
            if j < len(text):
                # Add <b> and </b> around the bold text
                result += '<i>' + text[i+2:j] + '</i>'
                i = j + 2
            else:
                result += text[i:]
                break
        else:
            result += text[i]
            i += 1
    return result

def wrap_list_with_prefix(input_list, prefix, opening_html_tag):
    def create_after_item(item):
        return item[:1] + "/" + item[1:]

    result = input_list.copy()

    i = 0
    while i < len(result):
        if result[i].startswith(prefix):
            # Find the end of the contiguous block
            j = i + 1
            while j < len(result) and result[j].startswith(prefix):
                j += 1

            # Insert items before and after the block
            result.insert(i, opening_html_tag)
            result.insert(j + 1, create_after_item(opening_html_tag))

            # Move the index past the block and new items
            i = j + 2
        else:
            i += 1

    return result

def get_frontmatter_item(markdown_filepath, frontmatter_item):
    result = ""

    with open(markdown_filepath, "r") as file:
        markdown_content = file.read()

    lines = markdown_content.split('\n')

    for line in lines:
        if line.startswith(frontmatter_item):
            result = line.lstrip(f"{frontmatter_item}: ")

    return result

def format_date(date_string):
    year, month, day = date_string.split('-')
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    month_name = months[int(month) - 1]

    # Add original suffix to day
    day_int = int(day)
    if 4 <= day_int <= 20 or 24 <= day_int <= 30:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][day_int % 10 - 1]

    formatted_date = f"{month_name} {day_int}{suffix}, {year}"

    return formatted_date

# Function for converting the markdown into html lines
def generate_html_from_markdown(markdown_filepath):

    with open(markdown_filepath, 'r') as file:
        markdown_content = file.read()

        # Split the markdown content into lines
        lines = markdown_content.split('\n')

        for line in lines:
            if len(line) == 0 or line.startswith(("---", "description: ", "title:", "author:")): # Empty lines and front matter
                pass
            elif line.startswith("date:"):
                post_date_text = format_date(line.lstrip("date: "))
                post_date_html = f"""<p class="{post_date_class}">{post_date_text}</p>"""
            elif line.startswith('#'): # Headers
                header_parts = line.split(' ')
                header_level = len(header_parts[0])
                header_text = ' '.join(header_parts[1:])
                header_html = f'<h{header_level}>{header_text}</h{header_level}>' # need to add the ids? or do it via javascript
                html_lines.append(header_html)
            elif line.startswith('- '): # Unordered list items
                bullet_point_text = line.strip('- ')
                bullet_point_html = f"""\t<li class="{ul_list_item_class}">{bullet_point_text}</li>"""
                html_lines.append(bullet_point_html)
            elif line.startswith(("1", "2", "3", "4", "5", "6", "7", "8", "9")): # Ordered lists (ugly but works)
                numbered_list_item_parts = line.split(". ")
                numbered_list_item_text = ' '.join(numbered_list_item_parts[1:])
                numbered_list_item_html = f"""\t<li class="{ol_list_item_class}">{numbered_list_item_text}</li>"""
                html_lines.append(numbered_list_item_html)
            elif line.startswith('!('): # Media (images and videos)
                media_caption = extract_parentheses(line)
                media_url = extract_brackets(line)
                if media_url.endswith('.mp4'): # Videos, without captions for now
                    video_html = f"""<video autoplay loop><source src="{media_url}" type="video/mp4" /></video>"""
                    html_lines.append(video_html)
                elif len(media_caption) == 0: # image without caption
                    image_html = f"""<picture><img src="{media_url}"></picture>"""
                    html_lines.append(image_html)
                else: # image with caption
                    image_html = f"""<picture><img src="{media_url}"><p class="caption">{media_caption}</p></picture>"""
                    html_lines.append(image_html)
            elif line.startswith('> '): # Quotes
                quote_text = line.lstrip("> ")
                quote_html = f"""<div class="{quote_line_class}"><p>{quote_text}</p></div>"""
                html_lines.append(quote_html)
            else: # Normal text paragraphs
                line_html = f"""<p>{line}</p>"""
                html_lines.append(line_html)

        # At the end, insert the date right below the title which should be the first line...
        html_lines.insert(0, post_date_html)

    return html_lines

# Function for writing a blog post into an html file
def generate_blog_post_html(post_title, post_description, html_lines):
    new_line = "\n"
    html_template = f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1">
        <title>Shinji Pons | Product Designer of 3D Tools & Beyond | {post_title}</title>
        <meta name="description"          content="{post_description}">
        <link rel="stylesheet" href="../css/styles.css">
        <meta property="og:url"           content="https://shinjipons.com">
        <meta property="og:type"          content="website">
        <meta property="og:title"         content="Shinji Pons | Product Designer of 3D Tools & Beyond | {post_title}">
        <meta property="og:description"   content="{post_description}">
        <meta property="og:image"         content="https://www.shinjipons.com/images/opengraph.jpg">
        <meta name="twitter:card"         content="summary_large_image">
        <meta property="twitter:domain"   content="shinjipons.com">
        <meta property="twitter:url"      content="https://shinjipons.com">
        <meta name="twitter:title"        content="Shinji Pons | Product Designer of 3D Tools & Beyond | {post_title}">
        <meta name="twitter:description"  content="{post_description}">
        <meta name="twitter:image"        content="https://www.shinjipons.com/images/opengraph.jpg">
        <link rel="icon" type="image/png" sizes="32x32"   href="/icons/favicon-32x32.png">
        <link rel="icon" type="image/png" sizes="16x16"   href="/icons/favicon-16x16.png">
        <link rel="apple-touch-icon"      sizes="180x180" href="/icons/favicon-ios.png">
    </head>
    <body>
        <nav>
            <!-- <div>
                <a class="monospace" href="index.html">Shinji Pons</a>
            </div> -->
            <div>
                <a class="monospace" href="../index.html">Work</a>
                <a class="monospace" href="../blog.html">Blog</a>
                <a class="monospace" href="https://shinjipons.com/files/Shinji-Pons-Resume.pdf" target="_blank">Resume</a>
            </div>
            <div>
                <a class="monospace button-call-to-action" href="mailto:website@shinjipons.com">Contact</a>
            </div>
        </nav>
        <main>
            <div class="left-column">
                <ul id="article-outline" class="monospace padding-between-items">Outline
                </ul>
            </div>
            <div class="right-column">
                <div class="blog-article-content">
                    <h1>{post_title}</h1>
                    {f"{new_line.join(html_lines)}"}
                </div>
            </div>
        </main>
        <script type="text/javascript" src="../js/script.js"></script>
    </body>
    </html>
    """
    post_filename = post_title.strip("\"").replace(" ", "-").lower()
    output_path = os.path.join(OUTPUT_FOLDER_BLOG_POSTS, f"{post_filename}.html")

    with open(output_path, "w") as html_file:
        html_file.write(html_template)

# The actual execution for making the blog post file
for markdown_filepath in get_all_markdown_filepaths(markdown_src_directory):
    html_lines = []
    html_filename = markdown_filepath.split('/')[-1].strip('.md')
    post_title = html_filename.replace("-", " ").capitalize()
    post_description = get_frontmatter_item(markdown_filepath, "description")

    # Replace the bold ** with <b> tags
    html_lines_b = []
    for line in generate_html_from_markdown(markdown_filepath):
        if "**" in line:
            html_lines_b.append(replace_bold(line))
        else:
            html_lines_b.append(line)

    # Replace the ()[] with <a> tags
    html_lines_b_a = []
    for line in html_lines_b:
        if "](" in line:
            html_lines_b_a.append(replace_link(line))
        else:
            html_lines_b_a.append(line)

    html_lines_b_a_i = []
    for line in html_lines_b_a:
        if "*" in line:
            if "**" in line:
                pass
            else:
                html_lines_b_a_i.append(replace_italics(line))
        else: html_lines_b_a_i.append(line)

    # Wrapping the numbered and unordered list needs to happens outside of the main function, because they need to have "visibility" over the whole list
    html_lines_b_a_i_ul = wrap_list_with_prefix(html_lines_b_a_i, f"\t<li class=\"{ul_list_item_class}\">", "<ul>")
    html_lines_b_a_i_ul_ol = wrap_list_with_prefix(html_lines_b_a_i_ul, f"\t<li class=\"{ol_list_item_class}\">", "<ol>")

    # Now deal with the code block
    html_lines_b_a_i_ul_ol_code = [] # Finished code!
    count = 0
    for line in html_lines_b_a_i_ul_ol:
        if line.lower() == "<p>```</p>":
            if count % 2 == 0: # it's an opening tag
                new_line = f"""<div class=\"{code_block_class}\">"""
                html_lines_b_a_i_ul_ol_code.append(new_line)
                count += 1
            else: # it's a closing tag
                new_line = f"""</div>"""
                html_lines_b_a_i_ul_ol_code.append(new_line)
                count += 1
        else: # don't do anything
            html_lines_b_a_i_ul_ol_code.append(line)

    # Generate a single page
    generate_blog_post_html(post_title, post_description, html_lines_b_a_i_ul_ol_code)

# ################# #
#                   #
#                   #
# Visual separation #
#                   #
#                   #
# ################# #

# Function for making the html lines for linking to all the blog posts
def link_blog_post_html_generator(source_directory):
    result = []
    post_title = ""
    post_date = ""
    post_url = ""

    for markdown_filepath in get_all_markdown_filepaths(source_directory):
        with open(markdown_filepath, "r") as file:
            markdown_content = file.read()
            lines = markdown_content.split('\n')
            for line in lines:
                if line.startswith("title: "):
                    post_title = line.lstrip("title: ")
                elif line.startswith("date: "):
                    post_date = format_date(line.lstrip("date: "))
            post_url = markdown_filepath.removeprefix(markdown_src_directory).removeprefix("/").removesuffix(".md") + ".html"
            post_url = "blog/" + post_url

        html = f"""
        <a href="{post_url}">
            <div class="{blog_article_item_class}">
                <h1>{post_title}</h1>
                <h1>{post_date}</h1>
            </div>
        </a>
        """
        result.append(html)

    return result

# Function for writing the blog.html file into dist/
def blog_html_page_generator(html_lines):
    new_line = "\n"
    blog_html_template = f"""<!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1" />
                <title>Shinji Pons | Product Designer of 3D Tools & Beyond</title>
                <meta name="description" content="Shinji is an experienced 3D software designer based in Toulouse, France. Making 3D tools, workflows and 3D models amongst many other things." />
                <link rel="stylesheet" href="css/styles.css" />
                <meta property="og:url" content="https://shinjipons.com" />
                <meta property="og:type" content="website" />
                <meta property="og:title" content="Shinji Pons | Product Designer of 3D Tools & Beyond" />
                <meta property="og:description" content="Shinji is an experienced 3D software designer based in Toulouse, France. Making 3D tools, workflows and 3D models amongst many other things." />
                <meta property="og:image" content="https://www.shinjipons.com/images/opengraph.jpg" />
                <meta name="twitter:card" content="summary_large_image" />
                <meta property="twitter:domain" content="shinjipons.com" />
                <meta property="twitter:url" content="https://shinjipons.com" />
                <meta name="twitter:title" content="Shinji Pons | Product Designer of 3D Tools & Beyond" />
                <meta name="twitter:description" content="Shinji is an experienced 3D software designer based in Toulouse, France. Making 3D tools, workflows and 3D models amongst many other things." />
                <meta name="twitter:image" content="https://www.shinjipons.com/images/opengraph.jpg" />
                <link rel="icon" type="image/png" sizes="32x32" href="/icons/favicon-32x32.png" />
                <link rel="icon" type="image/png" sizes="16x16" href="/icons/favicon-16x16.png" />
                <link rel="apple-touch-icon" sizes="180x180" href="/icons/favicon-ios.png" />
            </head>
            <body>
                <nav>
                    <!-- <div>
                        <a class="monospace" href="index.html">Shinji Pons</a>
                    </div> -->
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
                    <div class="left-column">
                        <div>
                            <ul class="monospace padding-between-items">About
                                <li>A product designer from France.</li>
                                <li>I specialize in the design and user experience of complex applications for creative professionals.</li>
                            </ul>
                            <ul class="monospace">Previously at
                                <li>Ragdoll Dynamics</li>
                                <li>Electronic Arts</li>
                                <li>The LEGO Group</li>
                                <li>Autodesk</li>
                                <li>Microsoft</li>
                                <li>Thomson Reuters</li>
                            </ul>
                        </div>
                        <ul class="monospace">Status
                            <li class="available-for-work">Available</li>
                        </ul>
                        <ul class="monospace">Online
                            <div class="social-links-block">
                                <a href="https://linkedin.com/in/shinjipons/" target="_blank"><button class="social-button">LinkedIn</button></a>
                                <a href="https://instagram.com/shinji.pons" target="_blank"><button class="social-button">Instagram</button></a>
                                <a href="https://bento.me/shinjipons" target="_blank"><button class="social-button">Bento</button></a>
                            </div>
                        </ul>
                        <ul class="monospace">Location
                            <li>Toulouse, France</li>
                        </ul>
                    </div>
                    <div class="right-column">
                        <div class="blog-articles-list-container">
                            {f"{new_line.join(html_lines)}"}
                        </div>
                    </div>
                </main>
                <script type="text/javascript" src="js/script.js"></script>
            </body>
        </html>
        """

    # continue here
    blog_html_filename = "blog".replace(" ", "-").lower()
    output_path = os.path.join(OUTPUT_FOLDER_BLOG_INDEX, f"{blog_html_filename}.html")

    with open(output_path, "w") as html_file:
        html_file.write(blog_html_template)

# The actual action
blog_html_page_generator(link_blog_post_html_generator(markdown_src_directory))