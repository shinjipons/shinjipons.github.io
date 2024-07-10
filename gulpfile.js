const gulp = require('gulp');
const sass = require('gulp-sass')(require('sass'));
const browserSync = require('browser-sync').create();

// Paths
const paths = {
    scss: {
        src: 'src/scss/*.scss',
        dest: 'dist/css'
    },
    html: {
        // src: '*.html'
        src: (['*.html', 'blog/*.html'])
    },
    js: {
        src: (['*.js', 'components/*.js'])
    }
};

// Compile SCSS to CSS
function style() {
    return gulp.src(paths.scss.src)
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest(paths.scss.dest))
        .pipe(browserSync.stream());
}

// Watch and Serve
function watch() {
    browserSync.init({
        server: {
            baseDir: "./"
        }
    });
    gulp.watch(paths.scss.src, style);
    gulp.watch(paths.html.src).on('change', browserSync.reload);
    gulp.watch(paths.js.src).on('change', browserSync.reload);
}

// Define complex tasks
const build = gulp.series(style, watch);

// Export tasks
exports.style = style;
exports.watch = watch;
exports.build = build;
