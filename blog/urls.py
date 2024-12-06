from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('web-devlopment/', views.webdev_page, name='webdev_page'),
    path('aiml/', views.aiml_page, name='aiml_page'),
    path('data-analytics/', views.data_analytics_page, name='data_analytics_page'),
    path('web-scrapping/', views.web_scrapping_page, name='web_scrapping_page'),
    path('process-automation/', views.process_automation_page, name='process_automation_page'),
]