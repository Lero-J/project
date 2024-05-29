from django.http import HttpResponse
from django.shortcuts import render

from myapp.models import Courses


# Create your views here.


def index(request):
    courses = Courses.objects.all()
    ctx = {
        'courses': courses
    }
    return render(request, 'myapp/index.html', context=ctx)

def course_info(request, course_id):
    course = Courses.objects.get(pk=course_id)
    return render(request, 'myapp/about.html', {'course': course})

def contact(request):
    return render(request, 'myapp/contact.html', {'contacts': ('+998 71 245-55-95', '+998 71 245-50-90')})