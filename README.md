<div align="center">
<h1>Django Restart</h1>
</div>

# **Context**
- [**Context**](#context)
  - [**Day 01**](#day-01)
    - [Installation](#installation)
    - [Django Project](#django-project)
    - [Django App](#django-app)

## **Day 01**

### Installation

- Package manager

  ```sh
  pipx install uv
  ```

- Initial project

  ```sh
  uv init
  ```

- Django install

  ```sh
  uv add django
  ```

[⬆️ Go to Context](#context)

### Django Project

- Create project

  ```sh
  django-admin startproject first_project
  ```

- Run the project server

  ```sh
  py manage.py runserver
  ```

[⬆️ Go to Context](#context)

### Django App

- Create app

  ```sh
  py manage.py startapp first_app
  ```

> [!NOTE]
>
> - A project can contain multiple apps

- Register app in [settings.py](./Day%2001/first_project/settings.py)

  ```py
  INSTALLED_APPS = [
      ...
      'first_app',
  ]
  ```

[⬆️ Go to Context](#context)
