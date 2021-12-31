def my_middleware(get_response):
    print("One time Initialization")

    def my_function(request):
        print("This is before view")
        response = get_response(request)
        print("This is after view")
        return response

    return my_function


class MyMiddleware:
    # Initialization will be done only one time
    def __init__(self, get_response):
        self.get_response = get_response
        print("One time Initialization")

    # The below method will run each time when we call our view function
    def __call__(self, request):
        print("This is before view")
        response = self.get_response(request)
        print("This is after view")
        return response


# Note:
# If multiple middleware are there, then each middleware will first get initialized
# Then the code which is written before view is called will get executed
# At last that code will be executed which is written after the view call.

from django.shortcuts import HttpResponse

# *************MIDDLEWARE HOOKS*******************8

class MyProcessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        response = self.get_response(request)
        return response

    # The below function will dominate over HttpResponse of Django Views
    def process_view(request, *args, **kwargs):
        print("This is process view of middleware")

        #if return None ,then view fcuntion will called
        return HttpResponse("This is process view-before view")


class MyExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        response = self.get_response(request)
        return response

    # The below function will run ,when exception occurred inside the view function
    def process_exception(self, request, exception):
        msg = exception
        return HttpResponse(msg)


class MyTemplateResponseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        response = self.get_response(request)
        return response

    # The below function will run ,when exception occurred inside the view function
    def process_template_response(self, request, response):
        print("Process Template Response From Middleware")

        # If we want to change context data of view
        # This will run after activating middleware
        response.context_data['name'] = 'Mani'
        return response

