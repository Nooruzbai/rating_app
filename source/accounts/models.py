from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, verbose_name='Profile')
    first_name = models.CharField(max_length=50, blank=False, null=False, verbose_name="Firstname")
    last_name = models.CharField(max_length=50, blank=False, null=False, verbose_name="Lastname")
    profile_picture = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    bio = models.TextField(max_length=500, null=True, blank=True)
    email = models.EmailField(blank=False, null=False, verbose_name="Email")

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return f"Profile: {self.user}. {self.id} {self.last_name} {self.first_name}, {self.email} "