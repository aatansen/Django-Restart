<div align="center">
<h1>Django Restart</h1>
</div>

# **Context**
- [**Context**](#context)
  - [**Day 01**](#day-01)
    - [Installation](#installation)
    - [Django Project](#django-project)
    - [Django App](#django-app)
  - [**Day 02**](#day-02)
    - [Functional View](#functional-view)
    - [Configure `urls.py`](#configure-urlspy)

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

## **Day 02**

### Functional View

- Open app's [views.py](./Day%2002/first_app/views.py) and create a function

  ```py
  # core django imports
  ...
  from django.http import HttpResponse

  # Create your views here.
  def my_function(request):
      return HttpResponse("Hello from django")
  ```

[⬆️ Go to Context](#context)

### Configure `urls.py`

- Create [urls.py](./Day%2002/first_app/urls.py) in app directory

  ```py
  # core django imports
  from django.urls import path

  # import from app
  from first_app import views

  urlpatterns = [
      path('',views.my_function,name='')
  ]
  ```

- Now include this in project [urls.py](./Day%2002/first_project/urls.py)

  ```py
  # core django imports
  from django.contrib import admin
  from django.urls import path,include

  urlpatterns = [
      path('admin/', admin.site.urls),
      path('',include('first_app.urls'))
  ]
  ```

[⬆️ Go to Context](#context)
