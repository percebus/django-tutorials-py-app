module.exports = (grunt) => {
  'use strict'

  require('load-grunt-tasks')(grunt, {
    pattern: ['grunt-*', '!grunt-template-*']
  })

  const CSSModes = {
    STRICT: 2,
    RELAX: false
  }

  grunt.initConfig({
    jsonlint: {
      options: { prose: true },
      npm: ['package*.json'],
      csslint: ['.csslintrc'],
      htmllint: ['.htmllintrc'],
      webapp: ['webapp/**/*.json']
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
        // csslintrc: '.csslintrc' // TODO?
        import: CSSModes.STRICT // XXX?

        /* TODO vvv
        // formatters: [
        //   {id: 'junit-xml', dest: 'report/csslint_junit.xml'},
        //   {id: 'csslint-xml', dest: 'report/csslint.xml'}
        // ]
         * TODO ^^^
         */
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
