const gulp = require('gulp');
const sass = require('gulp-sass')(require('sass'));
const browserSync = require('browser-sync').create();
const fileInclude = require('gulp-file-include');

// Paths
const paths = {
    scss: {
        src: 'src/scss/**/*.scss',
        dest: 'dist/css'
    },
    html: {
        src: ['src/**/*.html', 'blog/**/*.html'], // Include partials and source HTML files
        watch: '*.html', // Watch root HTML files
        dest: './'
    },
    js: {
        src: '*.js'
    }
};

// Compile SCSS to CSS
function style() {
    return gulp.src(paths.scss.src)
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest(paths.scss.dest))
        .pipe(browserSync.stream());
}

// Use gulp-file-include to include partials
function fileIncludeTask() {
    return gulp.src(paths.html.src)
        .pipe(fileInclude({
            prefix: '@@',
            basepath: '@file'
        }))
        .pipe(gulp.dest(paths.html.dest));
}

// Watch and Serve
function watch() {
    browserSync.init({
        server: {
            baseDir: "./"
        }
    });
    gulp.watch(paths.scss.src, style);
    gulp.watch(paths.html.src, gulp.series(fileIncludeTask, reload));
    gulp.watch(paths.html.watch).on('change', browserSync.reload);
    gulp.watch(paths.js.src).on('change', browserSync.reload);
}

// Reload browser
function reload(done) {
    browserSync.reload();
    done();
}

// Define complex tasks
const build = gulp.series(fileIncludeTask, style, watch);

// Export tasks
exports.style = style;
exports.fileIncludeTask = fileIncludeTask;
exports.watch = watch;
exports.build = build;