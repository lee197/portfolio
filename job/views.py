from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from job import email_sender
import json

from job.models import Job, Person, Skill, Category, Works, Advices, Experience, Codes


def index(request):
    lee = Person.objects.get(id=1)
    skills = Skill.objects
    categories = Category.objects
    works = Works.objects
    advices = Advices.objects.order_by("rank")
    experiences = Experience.objects
    codes = Codes.objects
    return render(request, 'index.html', {'person': lee,
                                          'skills': skills,
                                          'categories': categories,
                                          'works': works,
                                          'advices': advices,
                                          'experiences': experiences,
                                          'codes': codes})


@csrf_exempt
def email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        try:
            email_sender.send_email(email)
        except:
            error_message = {'message': "You have error while sending email", 'type': 'Email Error'}
            return HttpResponse(json.dumps(error_message), content_type="application/json")

    data = {'message': "Your email has been sent out", 'type': 'Email Sent'}
    return HttpResponse(json.dumps(data), content_type="application/json")


def home(request):
    jobs = Job.objects
    return render(request, 'home.html', {'jobs': jobs})


def detail(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    return render(request, 'detail.html', {'job': job_detail})
