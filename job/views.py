from django.shortcuts import render, get_object_or_404
from job.models import Job, Person, Skill, Category, Works, Advices, Experience, Codes


def index(request):
    lee = Person.objects.get(id=1)
    skills = Skill.objects
    categories = Category.objects
    works = Works.objects
    advices = Advices.objects
    experiences = Experience.objects
    codes = Codes.objects
    return render(request, 'index.html', {'person': lee,
                                          'skills': skills,
                                          'categories': categories,
                                          'works': works,
                                          'advices': advices,
                                          'experiences': experiences,
                                          'codes': codes})


def home(request):
    jobs = Job.objects
    return render(request, 'home.html', {'jobs': jobs})


def detail(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    return render(request, 'detail.html', {'job': job_detail})
