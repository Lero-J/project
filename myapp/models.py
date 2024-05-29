from django.db import models

# Create your models here.


class Courses(models.Model):
    name = models.CharField(max_length=128, null=True)

    description = models.TextField(max_length=255, null=True)

    price = models.IntegerField(default=0)

    students_count = models.IntegerField(default=0)



    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Курсы'
        verbose_name = 'Курс'
