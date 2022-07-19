module.exports = (grunt) => {
  'use strict'

  require('load-grunt-tasks')(grunt, {
    pattern: ['grunt-*', '!grunt-template-*']
  })

  grunt.initConfig({
    jsonlint: {
      options: { prose: true },
      npm: ['package*.json'],
      htmllint: ['.htmllintrc']
    },
    yamllint: {
      github: ['.github/workflows/**/*.yml']
    },
    htmllint: {
      options: { force: true, htmllintrc: true },
      webapp: ['webapp/**/*/templates/**/*.html']
    },
    csslint: {
      options: {
        import: 2 // strict
        // import: false // lax
      },
      webapp: ['webapp/**/*/static/**/*.css']
    }
  })

  grunt.registerTask('lint:json', ['jsonlint'])
  grunt.registerTask('lint:yaml', ['yamllint'])
  grunt.registerTask('lint:html', ['htmllint'])
  grunt.registerTask('lint:css', ['csslint'])
  grunt.registerTask('lint', ['lint:json', 'lint:yaml', 'lint:html', 'lint:css'])

  grunt.registerTask('default', ['lint'])
}
