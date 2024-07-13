const gulp = require('gulp');
const sass = require('gulp-sass')(require('sass'));
const browserSync = require('browser-sync').create();
const fileInclude = require('gulp-file-include');

// paths
const paths = {
    scss: {
        src:'src/scss/*.scss',
        dest: 'dist/css'
    }
}

// Compile SCSS to CSS
function style() {
    return gulp.src(paths.scss.src)
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest(paths.scss.dest))
        .pipe(browserSync.stream());
}

// Watch everything and serve
function watch() {
    browserSync.init({
        server: {
            baseDir: './'
        }
    });
    gulp.watch(paths.scss.src, style);
}

// Define task in series
const build = gulp.series(style, watch);

// Export tasks
exports.style = style;
exports.watch = watch;
exports.build = build;