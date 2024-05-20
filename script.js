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
    } else {
        // then "close" the menu by adding and removing the right class
        menu.classList.remove('menu-open');
        menu.classList.add('menu-closed');
    }
}