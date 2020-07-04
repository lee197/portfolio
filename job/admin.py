from django.contrib import admin
from .models import Project, Person, Skill, Category, Works, Advices, Codes, ProjectImage

# Register your models here.
admin.site.register(Project)
admin.site.register(Person)
admin.site.register(Skill)
admin.site.register(Category)
admin.site.register(Works)
admin.site.register(Advices)
admin.site.register(Codes)
admin.site.register(ProjectImage)

