# pip install django
# django-admin startproject http_respo
# cd proj name
# python manage.py startapp AppName  xxxxxx For creation of application
# open settings.py installed apps then copy AppName into INSTALLED_APPS
# create template folder in AppName directory
# go to setting.py under template list add

# import os
# 'DIRS': [os.path.join(BASE_DIR, 'templates')],

# create html file inside templates folder i.e f1.html
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title><h1>My template view </h1></title>
# </head>
# <body>
# <h2> This is a template file</h2>
# </body>
# </html>


# #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# go to views.py
# from django.views.generic.base import TemplateView
#
#
# # Create your views here.
#
# class HomePages(TemplateView):
#     template_name = 'f1.html'

# #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# go to setting.py
# import os
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [os.path.join(BASE_DIR, 'templates')],


# #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# go to urls.py from app directory
# add path in app.urls.py
# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('', views.HomePages.as_view())
# ]


# #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# link app.urls to base.url

# from django.contrib import admin
# from django.urls import path, include
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('tempapp.urls'))
# ]


# #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# #To remove migration error
# python manage.py makemigrations
# python manage.py migrate
