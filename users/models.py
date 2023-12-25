from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_online = models.BooleanField(default=False)
    following = models.ManyToManyField(User, related_name='following', blank=True)
    friends = models.ManyToManyField(User, related_name='friends', blank=True)
    bio = models.CharField(max_length=50, blank=True)
    date_of_birth = models.CharField(max_length=6, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    image = models.ImageField(default='default_profile.img', upload_to='profile_img')

    def profile_posts(self):
        """
        чтобы установить связь между пользователем и постом,
        напишите связанное имя модели в маленьком регистре,
        а затем используйте _set.
        fields.name_model_relation + _set.metod()
        """
        return self.user.post_set.all()