// Copy my email address to the clipboard when clicking a button

var copyEmailButton = document.getElementById('copy-email');
var myEmailAddress = 'hello@shinjipons.com';

if (copyEmailButton) {
    copyEmailButton.addEventListener('click', clickToCopyEmail);

    // replace the original text on mouse leave
    copyEmailButton.addEventListener('mouseleave', function() {
        copyEmailButton.innerHTML = myEmailAddress;
    })
}

function clickToCopyEmail() {
    navigator.clipboard.writeText(copyEmailButton.innerHTML)
}

// Create a fake decrypting effect for my work status

const textToModify = document.getElementById('text-to-scramble');
var finalMessage = 'available for work';
var characters = '-abcdefghijklmnopqrstuvwxyz0123456789, [](){}';

function messageInitializer() {
    if (textToModify) {
        var initialMessage = "";
        for (var i = 0; i < finalMessage.length; i++) {
            initialMessage += characters[Math.floor(Math.random() * characters.length)]
        }
        textToModify.innerHTML = initialMessage;
    }
}

function messageDecoder(inputMessage) {
    if (textToModify) {
        for (var i = 0; i < finalMessage.length; i++) {
            var randomIndex = Math.floor(Math.random() * inputMessage.length);
            var outputMessage = inputMessage.slice(0, randomIndex) + finalMessage[randomIndex] + inputMessage.slice(randomIndex + 1)
            textToModify.innerHTML = outputMessage;
        }
    }
}

if (textToModify) {
    messageInitializer(textToModify.innerHTML);

    const intervalId = setInterval(() => {
        messageDecoder(textToModify.innerHTML)

        if (textToModify.innerHTML == finalMessage) {
            clearInterval(intervalId);
            textToModify.classList.add('availability-confirmed');
        }

    }, 3);
}

// Open and close the menu

const menu = document.getElementById('menuPage');
const trigger = document.getElementById('menuTrigger');

trigger.addEventListener('click', function() {
    menuTriggerClickHandler();
})

menu.addEventListener('click', function() {
    menuTriggerClickHandler();
})

function menuTriggerClickHandler() {
    // check if closed
    if (menu.classList.contains('menu-closed')) {
        // then "open" the menu by adding and removing the right class
        menu.classList.remove('menu-closed');
        menu.classList.add('menu-open');

        // make the html non scrollable
        document.body.style.overflow = 'hidden';
    } else {
        // then "close" the menu by adding and removing the right class
        menu.classList.remove('menu-open');
        menu.classList.add('menu-closed');

        // make the html scrollable again
        document.body.style.overflow = 'auto';
    }
}

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
    var indexToSkip = 0;

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