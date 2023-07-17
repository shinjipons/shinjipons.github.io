const gulp = require('gulp');
const browserSync = require('browser-sync').create();

// Watch for changes in *.html files and reload the browser automatically
function html() {
  return gulp.src('*.html')
    .pipe(browserSync.reload({ stream: true }));
}

// Watch for changes in *.css files and stream changes to the browser automatically
function css() {
  return gulp.src('*.css')
    .pipe(browserSync.stream());
}

// Watch task to set up the watchers for *.html and *.css files
function watch() {
  browserSync.init({
    server: {
      baseDir: './'
    }
  });

  gulp.watch('*.html', html);
  gulp.watch('*.css', css);
}

exports.watch = watch;
