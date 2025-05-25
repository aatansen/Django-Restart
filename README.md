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
    - [`**kwargs` in `urls` \& `views`](#kwargs-in-urls--views)

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

### `**kwargs` in `urls` & `views`

- Create a function in [views.py](./Day%2002/first_app/views.py)

  ```py
  def contact(request,**kwargs):
      status=kwargs.get('status')
      return HttpResponse(f"contact page {status}")
  ```

- Add `url` path in [urls.py](./Day%2002/first_app/urls.py)

  ```py
  urlpatterns = [
      ...
      path('contact/',views.contact,{'status':'ok'},name='contact'),
  ]
  ```

- Adding another path based on same view with different `**kwargs`

  ```py
  urlpatterns = [
      ...
      path('contact-v2/',views.contact,{'status':'not ok'},name='contact'),
  ]
  ```

> [!NOTE]
>
> - The third argument in the `path()` function, `{'status': 'ok'}`, is passed to the view as `**kwargs`
> - In this case, when someone visits `/contact/`, Django will call `contact(request, status='ok')`
> - This is useful for passing static values to a view without needing to include them in the URL
> - `contact-v2/` this URL pattern passes `{'status': 'not ok'}` as `**kwargs` to the contact view. It allows reusing the same view (contact) but change the behavior based on static data

[⬆️ Go to Context](#context)
