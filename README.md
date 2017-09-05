# Wagtail Project Template

> A template for a Wagtail project with basic apps and a Webpack setup.

## Install

1.  To start a project using this template, run
    ```bash
    django-admin startproject name --template=https://github.com/littleweaver/wagtail-project-template.git
    ```

1.  Double check that all instances of `project_name` were replaced with your project name. You may need to do this manually for `package.json` and `.gitignore`

1.  Change this README to be relevant to your project.

1.  Run `./manage.py migrate` and `.manage.py runserver` and you're up and running!

## Usage

### Requirements
When compliling requirements using `pip compile`, it's important to compile requirements before compiling dev-requirements, as dev-requirements depends on the requirements file. Follow the steps below when adding requirements.

1.  Add package name to `requirements.in`
1.  `pip-compile --output-file requirements.txt requirements.in`
1.  `pip-compile --output-file dev-requirements.txt dev-requirements.in`

### Database configuration

Set the database url as the `DATABASE_URL` enviromnent variable.

The format for `DATABASE_URL` urls is
`<type_of_database>://<database_user>:<database_password>@<server>:<port>/<database_name>`
The default is a SQLite database.

## [LICENSE](LICENSE.md)
