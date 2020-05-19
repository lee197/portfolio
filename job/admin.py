from django.contrib import admin
from .models import Job, Person, Skill, Category

# Register your models here.
admin.site.register(Job)
admin.site.register(Person)
admin.site.register(Skill)
admin.site.register(Category)

