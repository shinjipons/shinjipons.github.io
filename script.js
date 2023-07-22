console.log("Hello, World!")

function getRandomNumber(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

// Get all elements with the class .packery-grid-item
const elementsWithClass = document.querySelectorAll('.packery-grid-item');

// Loop through all elements
for (const element of elementsWithClass) {
    // Add random width to each element
    const randomWidth = getRandomNumber(10, 50);
    element.style.width = `${randomWidth}%`;
}

// wait for the document to be fully loaded
document.addEventListener("DOMContentLoaded", function () {
    // Get the container element for your Packery layout
    var container = document.querySelector(".packery-grid");

    // Initialize Packery
    var packery = new Packery(container, {
        // Your Packery options here
        itemSelector: '.packery-grid-item',
        gutter: 0
    });

    // Ensure images are loaded before triggering the layout
    imagesLoaded(container, function () {
        packery.layout();
    })
});