// for more information, check out this article
// https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_custom_elements
// https://www.freecodecamp.org/news/reusable-html-components-how-to-reuse-a-header-and-footer-on-a-website/

class HeadBlog extends HTMLElement {
    constructor() {
        // no idea what this does...
        super();
    }

    connectedCallback() {
        this.innerHTML = `
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1">
        <title>Shinji Pons | Product Designer of 3D Tools & Beyond</title>
        <meta name="description" content="Shinji is an experienced 3D software designer based in Toulouse, France. Making 3D tools, workflows and 3D models amongst many other things.">
        <link rel="stylesheet" href="../dist/css/styles.css">

        <!-- Facebook Meta Tags -->
        <meta property="og:url" content="https://shinjipons.com">
        <meta property="og:type" content="website">
        <meta property="og:title" content="Shinji Pons | Product Designer of 3D Tools & Beyond">
        <meta property="og:description" content="Shinji is an experienced 3D software designer based in Toulouse, France. Making 3D tools, workflows and 3D models amongst many other things.">
        <meta property="og:image" content="https://www.shinjipons.com/images/opengraph.jpg">

        <!-- Twitter Meta Tags -->
        <meta name="twitter:card" content="summary_large_image">
        <meta property="twitter:domain" content="shinjipons.com">
        <meta property="twitter:url" content="https://shinjipons.com">
        <meta name="twitter:title" content="Shinji Pons | Product Designer of 3D Tools & Beyond">
        <meta name="twitter:description" content="Shinji is an experienced 3D software designer based in Toulouse, France. Making 3D tools, workflows and 3D models amongst many other things.">
        <meta name="twitter:image" content="https://www.shinjipons.com/images/opengraph.jpg">

        <!-- Favicon Tags -->
        <link rel="icon" type="image/png" sizes="32x32" href="/icons/favicon-32x32.png">
        <link rel="icon" type="image/png" sizes="16x16" href="/icons/favicon-16x16.png">
        <link rel="apple-touch-icon" sizes="180x180"    href="/icons/favicon-ios.png">
        `;
    }
}

customElements.define('head-blog-component', HeadBlog);