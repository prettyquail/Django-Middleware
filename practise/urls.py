from django.urls import path
from . import views

urlpatterns = [
    path("function-based/", views.FunctionMiddlewareView, name="firstview"),
    path("class-based/", views.ClassMiddlewareView, name="secondview"),
    path("exception/", views.MiddlewareExceptionHookView, name="thirdview"),
    path("template/", views.MiddlewareTemplateHookView, name="fourthview"),

]
