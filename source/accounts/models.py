from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(get_user_model(),related_name='profile', on_delete=models.CASCADE, verbose_name='Profile')
    profile_picture = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    bio = models.TextField(max_length=500, null=True, blank=True)
    email = models.EmailField(blank=False, null=False, verbose_name="Email")

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return f"Profile: {self.user.username}. {self.id} {self.last_name} {self.first_name}, {self.email} "