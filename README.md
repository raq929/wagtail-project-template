# Wagtail Project Template

> A template for a Wagtail project with basic apps and a Webpack setup.

## Table of Contents
* [Requirements](#requirements)
* [Create a new repo](#create-a-new-repo)
* [Development](#development)
   * [Quick start](#quick-start)
   * [Adding requirements](#adding-requirements)
   * [Database configuration](#database-configuration)
   * [Managment commands](#management-commands)

## Requirements
* Python 3
* `virtualenv` or [`virtualenvwrapper`](https://virtualenvwrapper.readthedocs.io/en/latest/install.html)

## Create a new repo from this template.

1.  Clone this repo
1.  Create a new virtualenv for your project and run `pip install django`
1.  Create a new project from the template by running `django-admin startproject <project_name> --template=wagtail-project-template`
1.  `cd` into your new project directory and run `git init` to initialize a git repository. Make an initial commit.
1.  Open your new project in a text editor and replace all instances of `project_name` with your project name.
1.  Change this README to be relevant to your project.
1.  Create a database using the instructions below.

## Development

### Quick start
1.  [Create a virtualenv](https://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html#mkvirtualenv) for this project (using python3)
1.  `pip install -r dev-requirements.txt`
1.  In a new window `npm install` then `npm start`
1.  Start postgresql
1.  `createdb <project_name>`
1.  `DATABASE_URL=postgres:///iai ./manage.py migrate`
1.  `DATABASE_URL=postgres:///iai ./manage.py createdevdata`
1.  `DATABASE_URL=postgres:///iai ./manage.py runserver`

### Requirements
Use [`pipenv`](https://docs.pipenv.org/) to manage requirements.

1.  `pipenv install --three` # Creates a virtualenv with python3 and installs normal dependencies
1.  `pipenv install --dev` # Installs dev dependencies
1.  `pipenv install <package>` # Installs the package and automatically updates `Pipfile` and `Pipfile.lock`.

### Database configuration

The first time you run, you'll need to run migrations and create a superuser:

```bash
    python manage.py migrate           # Create/sync the database.
    python manage.py createsuperuser   # Create an initial user.
```

``base.py`` will use sqlite3 by default.
You can use postgres with the ``DATABASE_URL`` environment variable.

```bash
    createdb project_name
    DATABASE_URL=postgres:///project_name python manage.py migrate
```

The format for `DATABASE_URL` urls is
`<type_of_database>://<database_user>:<database_password>@<server>:<port>/<database_name>`
If no database is specified, the default is a SQLite database.

You can now run the server: `DATABASE_URL=postgres:///project_name ./manage.py runserver`

### Management commands
<dl>
  <dt>createdevdata [--delete]</dt>
  <dd>
    This command creates a basic Wagtail site and a superuser. It calls all other management commands related to development data. The delete flag deletes all data before creating new data.
  </dd>
  <dt>createhomepage [--delete]</dt>
  <dd>
    This command creates a homepage and Wagtail Site if they do not already exist. If called with the delete flag, deletes all pages except the root and creates a homepage. You will need to restart the server after running this command, as the Wagtail site number will change.
  </dd>
  <dt>createblogposts <number_of_posts></dt>
  <dd>
    This command creates a blog index page (if it does not already exist) and the specified number of blog posts.
  </dd>
</dl>

## [LICENSE](LICENSE.md)
