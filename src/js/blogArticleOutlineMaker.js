document.addEventListener('DOMContentLoaded', function() {
    const articleOutline = document.getElementById('article-outline');
    const headers = document.querySelectorAll('h1[id^="chapter-"], h2[id^="chapter-"], h3[id^="chapter-"]');

    headers.forEach(header => {
        const li = document.createElement('li');
        const a = document.createElement('a');
        a.href = `#${header.id}`;
        a.textContent = header.textContent;
        li.appendChild(a);
        articleOutline.appendChild(li);
    });
});
