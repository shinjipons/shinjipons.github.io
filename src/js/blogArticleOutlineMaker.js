// document.addEventListener('DOMContentLoaded', function() {
//     const articleOutline = document.getElementById('article-outline');
//     const headers = document.querySelectorAll('h1');

//     for (var i = 0; i < headers.length; i++) {
//         headers[i].id = i + 1; // off by one
//     }

//     headers.forEach((header, index) => {
//         if (index !== 0) {
//             // All the headers, except the very first one
//             const li = document.createElement('li');
//             const a = document.createElement('a');
//             a.href = `#${header.id}`;
//             a.textContent = header.textContent;
//             li.appendChild(a);
//             articleOutline.appendChild(li);
//         }
//     });
// });