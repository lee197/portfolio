from django.db import models


class Codes(models.Model):
    code_image = models.ImageField(upload_to='images/', default='images/0.jpg')
    code_name = models.CharField(max_length=50, default='fudi')
    code_description = models.CharField(max_length=500, default='fudi')
    code_url = models.CharField(max_length=500, default='fudi')

    def __str__(self):
        return self.code_name


class Experience(models.Model):
    ex_image = models.ImageField(upload_to='images/', default='images/0.jpg')
    company_name = models.CharField(max_length=50, default='fudi')
    ex_description = models.CharField(max_length=500, default='fudi')
    date = models.DateField()
    position = models.CharField(max_length=5, default='left')

    def __str__(self):
        return self.company_name


class Advices(models.Model):
    name = models.CharField(max_length=50, default='fudi')
    description = models.CharField(max_length=500, default='fudi')
    rank = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Works(models.Model):
    name = models.CharField(max_length=50, default='fudi')
    work_image = models.ImageField(upload_to='images/', default='images/0.jpg')
    type = models.CharField(max_length=50, default='iOS')

    def __str__(self):
        return self.name


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
    main_image = models.ImageField(upload_to='images/', default='images/0.jpg')
    personal_image = models.ImageField(upload_to='images/', default='images/0.jpg')
    candidate_name = models.CharField(max_length=20, default='Lee')
    short_summary = models.CharField(max_length=200, default='Im a software engineer')
    summary = models.CharField(max_length=1000, default='Im a software engineer')

    def __str__(self):
        return self.candidate_name


# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)

    def __str__(self):
        return self.summary
