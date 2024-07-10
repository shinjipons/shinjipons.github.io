const gulp = require('gulp');
const sass = require('gulp-sass')(require('sass'));
const browserSync = require('browser-sync').create();
const fileInclude = require('gulp-file-include');

// Compile SCSS to CSS

// Watch everything and serve






// inside of package.json, `npm start` triggers `build` defined below...
const build = gulp.series(style, watch);

// Export tasks
exports.style = style;
exports.watch = watch;
exports.build = build;