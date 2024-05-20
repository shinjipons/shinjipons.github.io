const menu = document.getElementById('menuPage');
const trigger = document.getElementById('menuTrigger');
const textToModify = document.getElementById('text-to-scramble');
var finalMessage = "available for work";
var characters = "-abcdefghijklmnopqrstuvwxyz0123456789, [](){}";

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
    } else {
        // then "close" the menu by adding and removing the right class
        menu.classList.remove('menu-open');
        menu.classList.add('menu-closed');
    }
}

function messageInitializer(inputMessage) {
    var initialMessage = "";
    for (var i = 0; i < finalMessage.length; i++) {
        initialMessage += characters[Math.floor(Math.random() * characters.length)]
    }
    textToModify.innerHTML = initialMessage;
    // return isInitialized = trye
}

function messageDecoder(inputMessage) {
    for (var i = 0; i < finalMessage.length; i++) {
        var randomIndex = Math.floor(Math.random() * inputMessage.length);
        var outputMessage = inputMessage.slice(0, randomIndex) + finalMessage[randomIndex] + inputMessage.slice(randomIndex + 1)
        textToModify.innerHTML = outputMessage;
    }
}

messageInitializer(textToModify.innerHTML);

const intervalId = setInterval(() => {
    messageDecoder(textToModify.innerHTML)

    if (textToModify.innerHTML == finalMessage) {
        clearInterval(intervalId);
        textToModify.classList.add('availability-confirmed');
    }

}, 3);