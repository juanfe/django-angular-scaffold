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

Can accept a path. The following are valid viewname arguments

```
./manage startview homepage
./manage startview home-page
./manage startview ticket/new
./manage startview settings/options/test
```
This will create a view file in the appropriate folder, create a mirrored scss file in the site directory, and
import the style into the main styles.scss file.

###generatedocs

```
./manage.py generatedocs
```

Adds a `/docs` folder and copies some basic documentation into it

###createdebugger

```
./manage.py createdebugger
```

Creates a config file for angular that overrides console.log and replaces it with
$log.debug. Then disables $log.debug unless a query string with an encoded password
is included. 

This makes it very easy to debug your application without having to expose the underlying 
to the users. It also allows you to keep your logging statements in your app when going to 
production, as they are turned off and hidden by default. 