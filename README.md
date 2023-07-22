# shinjipons.github.io

Portfolio website replacing Webflow

# MacOS

# Requirements on MacOS

- Install `node` globally
- Install `gulp` globally 
- Install `browser-sync` locally using `--save-dev`

# Windows

## Requirements on Windows

- Use the `powershell` terminal
- Install `node` globally
- Install `gulp` locally using `--save-dev`
- Install `browser-sync` locally using `--save-dev`

## How to run on Windows

Run `gulp watch` in the `Command Prompt` terminal.

# Todo

- [x] Use Packery to create a cool layout on the index.html with project images
    - [x] each project images is a link to the corresponding project page
    - [x] Use `ImagesLoaded` to ensure that the images are loaded before Packery is triggered (https://chat.openai.com/share/ec78e7ed-3125-4b6f-babc-84474732975c)
- [ ] Come up with a way to take a bunch of images from a given `source-folder` and spit out a bunch of resized *.webp images in the `dist-folder`
- [ ] Make an Opengraph image

# Workflow for images

- place between 3 and 5 images in a folder, for example: `./source/images/louvre-abu-dhabi/`
- have `image-magick` run through all of the images
    - resize them to a certain `max-width`, while maintaining the aspect ratio
    - compress the images so that they all fit within a certain `budget` (something like 200 kb per image)
    - convert them to the `webp` format
    - rename them in the order they came in. For example:
        - `louvre-abu-dhabi-001.webp`
        - `louvre-abu-dhabi-002.webp`
        - `louvre-abu-dhabi-003.webp`
- move the those images in the destination folder, for example: `./dist/images/louvre-abu-dhabi/`
