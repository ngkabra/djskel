This is not ready for production yet.

This is a template for a django project.

To use:

    git clone git@github.com:ngkabra/djskel.git
    django-admin.py startproject {{project_name}} --template=djskel

Then go to {{project_name}}/project_settings and configure
all the files in there and the sub-directories.

Update {dev,prod,test}/_passwords.py appropriately.
Backup the _passwords.py files.
Soft-link appropriate directory to "local"

Then:

    cd <{{project_name}}>/
    pip install -r requirements.txt
    git init
    git add manage.py requirements.txt myproj
    cd <{{project_name}}>/{{project_name}}/
    git submodule add git@github.com:ngkabra/dutils.git
    git submodule add git@github.com:ngkabra/dbase.git

After that

-    create database {{project_name}}, user {{project_name}}
-    edit the port number in manage.py
-    python manage.py syncdb

Further customizations:

- for each new app, manage.py schemamigration <appname> --auto
    - followed by fab migrate
- For dbtemplates, uncomment in settings.py, and in dev/misc.py
- for debug toolbar, uncomment in dev/misc.py
- for django redirects, uncomment in settings.py and in installed_apps
