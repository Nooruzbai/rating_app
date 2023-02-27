from django.contrib.auth import get_user_model
from django.db import models

from rating import settings

User = get_user_model()

# Create your models here.
CHOICES = [('unknown', 'Unknown'), ('public', 'Public'), ('private', 'Private')]


class School(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Name')
    description = models.TextField(max_length=400, null=True, blank=True, verbose_name='Description')
    type = models.TextField(default=CHOICES[0], choices=CHOICES,
                            null=False, blank=False, verbose_name='Type')
    address = models.JSONField(default=dict)
    setting = models.CharField(max_length=100, null=False, blank=False, verbose_name='Setting')
    webpage = models.URLField(max_length=100, blank=True, null=True, verbose_name="Webpage")

    def __str__(self):
        return f'{self.pk}. {self.name}'

    class Meta:
        db_table = 'school'
        verbose_name = 'School'
        verbose_name_plural = 'Schools'



class Comment(models.Model):
    text = models.TextField(max_length=400, null=True, blank=True, verbose_name='Comment')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='user', on_delete=models.CASCADE, verbose_name='User')
    school = models.ForeignKey("school_rating.School", related_name='comments', on_delete=models.CASCADE, verbose_name='School')

class Rating(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Name')
    date_created = models.DateTimeField(auto_now_add=True, null=False, blank=False, verbose_name='Datetime')



    def __str__(self):
        return f'{self.pk}. {self.name}'

    class Meta:
        db_table = 'rating'
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'


class SchoolRating(models.Model):
    school = models.ForeignKey('school_rating.School', on_delete=models.CASCADE,
                               related_name='school_ratings', verbose_name='School Rating')
    rating = models.ForeignKey('school_rating.Rating', on_delete=models.CASCADE,
                               related_name='rating_schools', verbose_name='School Rating')
    score = models.IntegerField(null=True, blank=True, verbose_name='Score')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')

    def __str__(self):
        return f'{self.pk}. {self.school}, {self.rating}'

    class Meta:
        db_table = 'school_rating'
        verbose_name = 'School Rating'
        verbose_name_plural = 'School Ratings'
