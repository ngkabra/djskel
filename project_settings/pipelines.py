PIPELINE_CSS = {
    '{{project_name}}': {
        'source_filenames': (
            'css/screen.css',
            'css/humanity/jquery-ui-1.10.0.custom.min.css',
            'django_tables2/themes/paleblue/css/screen.css',
            'uni_form/uni-form.css',
            'css/{{project_name}}.uni-form.css',
            'css/pygments.css',
            ),
        'output_filename': 'css/{{project_name}}.css',
        'extra_context': {
            'media' : 'screen, projection',
            },
        },
}

PIPELINE_JS = {
    '{{project_name}}': {
        'source_filenames': (
            'js/jquery-ui-1.10.0.custom.min.js',
            'uni_form/uni-form.jquery.js',
            'dajaxice/dajaxice.core.js',
                 # Note: this needs to track the output of
                 # dajaxice_js_import template tag
                 # if that ever changes...
            'dajax/jquery.dajax.core.js',
            # Put project specific js file here
            'js/{{project_name}}.js',
            ),
        'output_filename': 'js/{{project_name}}.js',
        },
}

PIPELINE_DISABLE_WRAPPER = True
