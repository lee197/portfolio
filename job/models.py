from django.db import models


class Codes(models.Model):
    code_image = models.ImageField(upload_to='images/', default='images/0.jpg')
    code_name = models.CharField(max_length=50, default='fudi')
    code_description = models.CharField(max_length=500, default='fudi')
    code_url = models.CharField(max_length=500, default='fudi')

    def __str__(self):
        return self.code_name


class Advices(models.Model):
    name = models.CharField(max_length=50, default='fudi')
    description = models.CharField(max_length=500, default='fudi')
    rank = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Works(models.Model):
    work_name = models.CharField(max_length=50, default='work sample')
    work_image = models.ImageField(upload_to='images/', default='images/0.jpg')
    work_type = models.CharField(max_length=50, default='iOS')
    work_url = models.CharField(max_length=500, default='https://medium.com/@lee5187415')

    def __str__(self):
        return self.work_name


class Category(models.Model):
    category_name = models.CharField(max_length=20, default='language')

    def __str__(self):
        return self.category_name


class Skill(models.Model):
    category = models.CharField(max_length=20, default='language')
    skill_name = models.CharField(max_length=20, default='swift')
    percentage = models.CharField(max_length=20, default='80')

    def __str__(self):
        return self.skill_name


class Person(models.Model):
    main_image = models.ImageField(upload_to='img/', default='img/0.jpg')
    personal_image = models.ImageField(upload_to='img/', default='img/0.jpg')
    candidate_name = models.CharField(max_length=20, default='Lee')
    short_summary = models.CharField(max_length=200, default='Im a software engineer')
    summary = models.TextField(max_length=1000, default='Im a software engineer')

    def __str__(self):
        return self.candidate_name


# Create your models here.
class Project(models.Model):
    project_image = models.ImageField(upload_to='img/', default='img/0.jpg')
    main_image = models.ImageField(upload_to='img/', default='img/0.jpg')
    title = models.CharField(max_length=50, default="Lee's project")
    subtitle = models.CharField(max_length=50, default="Lee's project")
    video_link = models.CharField(max_length=50, default='Lee')
    image_video = models.ImageField(upload_to='img/', default='img/0.jpg')
    store_link = models.CharField(max_length=100, default='Lee')
    is_screen = models.BooleanField(default=True)

    summary = models.TextField(max_length=1000)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    title = models.CharField(max_length=50, default='Lee')
    small_image = models.ImageField(upload_to='img/', default='img/0.jpg')
    big_image = models.ImageField(upload_to='img/', default='img/0.jpg')
    summary = models.TextField(max_length=500, default='Lee')
    project = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
