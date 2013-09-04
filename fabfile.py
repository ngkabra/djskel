from fabric.api import env
env.virtualenv = '~/.v/d14int'
env.backups_dir = '~/Backups/websites'

from dutils.fabfile import *

APPMAP.update({
    '{{project_name}}': [WFApp('{{project_name}}', host='web95')],
    '{{project_name}}t':  [WFApp('{{project_name}}t', host='web95')], #  unused
    'all': ['{{project_name}}', '{{project_name}}t'],
})

env.apps = list(appmap('localhost'))    # default apps=localhost

@cmd_category('Pre-defined App Groups')
def {{project_name}}():
    '''{{project_name}} only'''
    apps('{{project_name}}')


@cmd_category('Pre-defined App Groups')
def {{project_name}}t():
    '''{{project_name}}t only'''
    {{project_name}}t()

def compass():
    compass_(dir='site_media')


def jsgen():
    jsgen_(has_dajax=True, dir='site_media/js')
