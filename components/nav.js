class NavBlog extends HTMLElement {
    constructor() {
        // no idea what this does...
        super();
    }

    connectedCallback() {
        this.innerHTML = `
        <nav>
            <div>
                <a class="monospace" href="index.html">Work</a>
                <a class="monospace" href="about.html">About</a>
                <a class="monospace" href="blog.html">Blog</a>
            </div>
            <div>
                <a class="monospace button-call-to-action" href="mailto:contact@shinjipons.com">Contact</a>
            </div>
        </nav>
        `;
    }
}

customElements.define('nav-component', NavBlog);