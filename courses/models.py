from django.db import models


# class Course(models.Model):
#     name = models.CharField(max_length=100)
#
#
# class CourseExpert(models.Model):
#     name = models.CharField(max_length=50)
#     course = models.ForeignKey()


class Students(models.Model):
    Female = 'F'
    Male = 'M'
    choices = ((Female, 'Female'), (Male, 'Male'))

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=choices, default=Female)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
