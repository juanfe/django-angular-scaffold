django-angular-scaffold
=======================

[![PyPI version](https://badge.fury.io/py/django-angular-scaffold.svg)](http://badge.fury.io/py/django-angular-scaffold)

set of django commands to scaffold a django-angular project

> Work in Progress

###scaffold

```
./manage.py scaffold
```

Builds a assets folder structure in the following structure:

```
/assets
    + - app
    |   + - config
    |   + - controllers
    |   + - directives
    |   + - services
    |   + - views
    |   + - app.js
    + - lib
        + - fonts
        + - scripts
        + - styles
            + - site
            |   + - _global.scss
            |   + - _mixins.scss
            |   + - _variables.scss
            + - vendor
            + styles.scss
```

It will prompt for an application name, this will add start the angular app off.

It also automatically setups the styles.scss to import the pre stubbed out globals, mixins, and variables files.

The rest of the folders are stubbed out with a `.gitkeep` file to allow the directory structure to be added to git.


###startview

```
./manage.py startview <viewname>
```

creates new view, creates new styles and adds it to the import
