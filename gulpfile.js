const gulp = require('gulp');
const sass = require('gulp-sass')(require('sass'));
const browserSync = require('browser-sync').create();
const fileInclude = require('gulp-file-include');
const concat = require('gulp-concat');

// HTML include task
function html() {
    return gulp.src(['src/html/**/*.html'])
        .pipe(fileInclude({
            prefix: '@@',
            basepath: '@file'
        }))
        .pipe(gulp.dest('dist'))
        .pipe(browserSync.stream());
}

// Compile SCSS to CSS
function style() {
    return gulp.src('src/scss/*.scss')
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest('dist/css'))
        .pipe(browserSync.stream());
}

function js() {
    return gulp.src('src/js/*.js')
        .pipe(concat('script.js'))
        .pipe(gulp.dest('dist/js'))
        .pipe(browserSync.stream());
}

// Watch everything and serve
function watch() {
    browserSync.init({
        server: {
            baseDir: 'dist'
        }
    });
    gulp.watch("src/scss/*.scss", style);
    gulp.watch("src/**/*.html").on('change', html);
    gulp.watch("dist/**/*.html").on('change', browserSync.reload);
    gulp.watch("src/js/*.js").on('change', js);
}

// Define task in series
const build = gulp.series(html, style, js, watch);

// Export tasks
exports.html = html;
exports.style = style;
exports.watch = watch;
exports.build = build;