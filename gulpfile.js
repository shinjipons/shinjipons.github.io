const gulp = require('gulp');
const sass = require('gulp-sass')(require('sass'));
const browserSync = require('browser-sync').create();

// paths
const paths = {
    scss: {
        src:'src/scss/*.scss',
        dest: './dist/css'
    },
    html: {
        src: '*.html'
    },
    js: {
        src: 'src/js/*.js',
        dest: './dist/js'
    }
}

// Compile SCSS to CSS
function style() {
    return gulp.src(paths.scss.src)
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest(paths.scss.dest))
        .pipe(browserSync.stream());
}

function js() {
    return gulp.src(paths.js.src)
        .pipe(gulp.dest(paths.js.dest))
        .pipe(browserSync.stream()); // I don't think that stream will work
}

// Watch everything and serve
function watch() {
    browserSync.init({
        server: {
            baseDir: './'
        }
    });
    gulp.watch(paths.scss.src, style);
    gulp.watch(paths.html.src).on('change', browserSync.reload);
    gulp.watch(paths.js.src).on('change', browserSync.reload);
}

// Define task in series
const build = gulp.series(style, js, watch);

// Export tasks
exports.style = style;
exports.watch = watch;
exports.build = build;