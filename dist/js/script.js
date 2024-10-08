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
// Code to add a random project to the bottom of each project page

const projects = [
    {
        title: "Autodesk Alias SubD",
        link: "alias-subd.html",
        imageUrl: "./images/alias-subd/alias-subd-01.webp"
    },
    {
        title: "Apple Bubble Letter",
        link: "apple-letter.html",
        imageUrl: "./images/apple-letter/apple-letter-01.webp"
    },
    {
        title: "Computational Typography",
        link: "basiljs.html",
        imageUrl: "./images/basiljs/basiljs-01.webp"
    },
    {
        title: "David Bowie",
        link: "david-bowie.html",
        imageUrl: "./images/david-bowie/david-bowie-01.webp"
    },
    {
        title: "Dynamo for Alias",
        link: "dynamo-for-alias.html",
        imageUrl: "./images/dynamo-for-alias/dynamo-for-alias-01.webp"
    },
    {
        title: "iPod Shuffle Alias Model",
        link: "ipod-shuffle.html",
        imageUrl: "./images/ipod-shuffle/ipod-shuffle-01.webp"
    },
    {
        title: "LEGO Digital Designer Pro",
        link: "lego-digital-designer-pro.html",
        imageUrl: "./images/ldd-pro/ldd-pro-01.webp"
    },
    {
        title: "Louvre Abu Dhabi",
        link: "louvre-abu-dhabi.html",
        imageUrl: "./images/louvre-abu-dhabi/louvre-abu-dhabi-01.webp"
    },
    {
        title: "Modulo",
        link: "modulo.html",
        imageUrl: "./images/modulo/modulo-01.webp"
    },
    {
        title: "Chevrolet Corvette C8 Blender Model",
        link: "corvette.html",
        imageUrl: "./images/corvette/corvette-01.webp"
    }
]

function addNextProject() {
    var link = document.getElementById('next-project-link');
    var title = document.getElementById('next-project-title');
    var image = document.getElementById('next-project-image');
    var path = window.location.pathname;
    var filename = path.split('/').pop();
    var randomIndex = Math.floor(Math.random() * projects.length);

    // catch error or check that the .next-project class exists
    if (link) {
        // check with index matches the current project
        for (var i = 0; i < projects.length; i++) {
            if (projects[i].link == filename) {
                if (randomIndex == i) {
                    randomIndex = (randomIndex * 2) % projects.length;
                    console.log('Whoops, it is a match! Changed!');
                }
            }
        }

        // add the link to the <a> tag
        link.href = projects[randomIndex].link;

        // add the project title
        title.innerHTML = projects[randomIndex].title;

        // add the image of the project
        image.src = projects[randomIndex].imageUrl;
    }
}

addNextProject();