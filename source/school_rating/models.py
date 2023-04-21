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
                               related_name='ratings', verbose_name='School Rating')
    rating = models.ForeignKey('school_rating.Rating', on_delete=models.CASCADE,
                               related_name='schools', verbose_name='School Rating')
    score = models.IntegerField(null=True, blank=True, verbose_name='Score')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')

    def __str__(self):
        return f'{self.pk}. {self.school_id}, {self.rating_id}, {self.date_created}'

    class Meta:
        db_table = 'school_rating'
        verbose_name = 'School Rating'
        verbose_name_plural = 'School Ratings'


class Comment(models.Model):
    text = models.TextField(max_length=500, null=True, blank=True, verbose_name='Text')
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE, verbose_name='User')
    school = models.ForeignKey('school_rating.School', on_delete=models.CASCADE, related_name='comments', verbose_name='School')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')

    def __str__(self):
        return f'{self.pk}. {self.user_id}, {self.school_id}, {self.text}'

    class Meta:
        db_table = 'comment'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class CommentLike(models.Model):
    user = models.ForeignKey(User, related_name='comment_likes', on_delete=models.CASCADE, verbose_name='User')
    comment = models.ForeignKey('school_rating.Comment', related_name="comment_likes", on_delete=models.CASCADE, verbose_name='comment')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')

    def __str__(self):
        return f'{self.pk}. {self.user}, {self.comment}'

    class Meta:
        db_table = 'like'
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'
        unique_together = ['user', 'comment']

