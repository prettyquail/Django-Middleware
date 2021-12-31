from django.shortcuts import render, HttpResponse

# Create your views here.

# my_middleware is created for this func-based view
# After calling FunctionMiddlewareView , my_middleware will be called automatically
# outputs in terminal
def FunctionMiddlewareView(request):
    print("I m View")
    return HttpResponse("This is Home Page for Function-Based Middleware")


def ClassMiddlewareView(request):
    print("I m View")
    return HttpResponse("This is Home Page for Class-Based Middleware")


def MiddlewareExceptionHookView(request):
    print("I m an Exception View")
    a=10/0
    return HttpResponse("This is Home Page for Middleware Hooks")


from django.template.response import TemplateResponse
def MiddlewareTemplateHookView(request):
    print("I am process_template_response Middleware hook")
    context = {'name': 'Manisha'}
    return TemplateResponse(request, 'index.html', context)
