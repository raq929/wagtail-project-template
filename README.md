# Wagtail Project Template

> A template for a Wagtail project with basic apps and a Webpack setup.

## Install

1.  To start a project using this template, run
    ```bash
      django-admin startproject name --template=https://github.com/littleweaver/wagtail-project-template.git
    ```

1.  Rename the project-name folder to your project name.

1.  Search for all instances of `project-name` in the repo and replace them with your project name.

1.  Change this README to be relevant to your project.

1.  Run `./manage.py migrate` and `.manage.py runserver` and you're up and running!

## Usage

### Requirements
When compliling requirements using `pip compile`, it's important to compile requirements before compiling dev-requirements, as dev-requirements depends on the requirements file.
