from django.http import HttpResponse


def courses_page(request):
    if request.user.is_authenticated:
        return HttpResponse('This is the Courses page')
    return HttpResponse("You have no permissions to view this page")
