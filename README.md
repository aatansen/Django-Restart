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
  - [**Day 03**](#day-03)
    - [Template in Django](#template-in-django)
      - [Send context data in template](#send-context-data-in-template)
    - [Django Template Language](#django-template-language)
      - [Variables](#variables)
      - [Filters](#filters)
      - [Date and Time](#date-and-time)

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

## **Day 03**

### Template in Django

- Create [templates](./Day%2003/first_app/templates/) in app directory where a same name sub-directory of app name [first_app](./Day%2003/first_app/templates/first_app/) need to be created. Here we will create [index.html](./Day%2003/first_app/templates/first_app/index.html)

  ```tree
  📦first_app
  ┣ 📂templates
  ┃ ┗ 📂first_app
  ┃   ┗ 📜index.html
  ```

- Create a function in [views.py](./Day%2003/first_app/views.py)

  ```py
  from django.shortcuts import render

  # Create your views here.
  def first_app(request):
      return render(request,'first_app/index.html')
  ```

- Configure app's [urls.py](./Day%2003/first_app/urls.py) with project [urls.py](./Day%2003/first_project/urls.py)

[⬆️ Go to Context](#context)

#### Send context data in template

- Create a dictionary in [views.py](./Day%2003/first_app/views.py)

  ```py
  def first_app(request):
      dynamic_data={
          'dt':'hello',
      }
      return render(request,'first_app/index.html',context=dynamic_data)
  ```

- Show the data in template's [index.html](./Day%2003/first_app/templates/first_app/index.html)

  ```jinja
  <h1>Dynamic data: {{dt}}</h1>
  ```

[⬆️ Go to Context](#context)

### Django Template Language

- Full docs can be found in official [Django Template Language](https://docs.djangoproject.com/en/stable/ref/templates/language/)

#### Variables

  ```jinja
  <h1>Dynamic data: {{dt}}</h1>
  ```

- Here `{{dt}}` is called variable

[⬆️ Go to Context](#context)

#### Filters

- Uppercase

  ```jinja
  <h1>Uppercase: {{dt|upper}}</h1>
  ```

- Lowercase

  ```jinja
  <h1>Lowercase: {{dt|lower}}</h1>
  ```

- Truncate Words

  ```jinja
  <h1>Truncate Words: {{description|truncatewords:2}}</h1>
  ```

- Truncate Characters

  ```jinja
  <h1>Truncate Characters: {{description|truncatechars:2}}</h1>
  ```

- Multi-Filter

  ```jinja
  <h1>Multi-Filter: {{description|upper|truncatewords:2}}</h1>
  ```

- Capital First

  ```jinja
  <h1>Capital first: {{dt|capfirst}}</h1>
  ```

- Default value

  ```jinja
  <h1>User: {{user_data|default:"anonymous"}}</h1>
  ```

- Length

  ```jinja
  <h1>Length: {{dt|length}}</h1>
  ```

- Slice

  ```jinja
  <h1>Slice: {{dt|slice:'2:3'}}</h1>
  ```

[⬆️ Go to Context](#context)

#### Date and Time

- Send date time in context of [views.py](./Day%2003/first_app/views.py)

  ```py
  from django.shortcuts import render
  from datetime import datetime

  # Create your views here.
  def first_app(request):
      date_time = datetime.now()

      dynamic_data={
          ...
          'date_time': date_time,
      }
      return render(request,'first_app/index.html',context=dynamic_data)
  ```

- Show in template (default view)

  ```jinja
  <h1>Date time: {{date_time}}</h1>
  ```

  - `June 1, 2025, 1:53 p.m.`

- Show only date

  ```jinja
  <h1>Date time: {{date_time|date}}</h1>
  ```

  - `June 1, 2025`

- Day Date Month Year (`D d M Y`)

  ```jinja
  <h1>Day Date Month Year: {{date_time|date:'D d M Y'}}</h1>
  ```

  - `Sun 01 Jun 2025`

- Time only

  ```jinja
  <h1>Time only: {{date_time|time}}</h1>
  ```

  - `2:06 p.m.`

- 24-hour time format

  ```jinja
  <h1>24-hour time format: {{date_time|time:'H:i'}}</h1>
  ```

  - `14:07`

- Short date format

  ```jinja
  <h1>Short date format: {{date_time|date:'SHORT_DATE_FORMAT'}}</h1>
  ```

  - `06/01/2025`

- More Format Constants

  | Format Constant         | Default (en)  | Meaning                   |
  | ----------------------- | ------------- | ------------------------- |
  | `DATE_FORMAT`           | `'N j, Y'`    | `June 1, 2025`            |
  | `SHORT_DATE_FORMAT`     | `'m/d/Y'`     | `06/01/2025`              |
  | `DATETIME_FORMAT`       | `'N j, Y, P'` | `June 1, 2025, 2:30 p.m.` |
  | `SHORT_DATETIME_FORMAT` | `'m/d/Y P'`   | `06/01/2025 2:30 p.m.`    |

- [Date Time Official Built-in template tags and filters](https://docs.djangoproject.com/en/stable/ref/templates/builtins/#date)

[⬆️ Go to Context](#context)
