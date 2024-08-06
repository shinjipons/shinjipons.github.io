# shinjipons.github.io

Portfolio website replacing Webflow

# Windows

## Requirements on Windows

- Use the `bash` terminal (not the `powershell` terminal)
- Install `node` globally
- Install the required packages with `npm install`

## How to run on Windows

Run `npm start` in the `bash` terminal.

# Workflow to cut the images

1. Go on `OneDrive > Design Work > Name of Project`
2. Inside of each relevant folder, there is a `_Portfolio` folder with source images
3. Copy all the source images
4. Paste them in `OneDrive > Portfolio 2023 > Name of Project`
5. Use **Adobe Bridge** to reorder and rename the images using the following scheme: `project-name-NNN`, where `NNN` is the number of the file
6. Copy and paste those renamed images into `./images/project-name` inside of the repository
7. Use **XnConvert** to resize those images to a *maximum width of 2000px* and convert them to `.webp`
8. `project_generator.py` is now ready to use those images as long as `pages_data.py` has the right path