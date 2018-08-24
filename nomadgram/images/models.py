from django.db import models
from nomadgram.users import models as user_models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.


@python_2_unicode_compatible
class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


@python_2_unicode_compatible
class Image(TimeStampedModel):

    """ Image Model """

    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()
    creator = models.ForeignKey(user_models.User, models.SET_NULL, null=True,)

    def __str__(self):
        return '지역:{} -설명:{}'.format(self.location, self.caption)


@python_2_unicode_compatible
class Comment(TimeStampedModel):

    """ Comment Model """

    message = models.TextField()
    creator = models.ForeignKey(user_models.User, models.SET_NULL, null=True,)
    image = models.ForeignKey(Image, models.SET_NULL, null=True,)


@python_2_unicode_compatible
class Like(TimeStampedModel):

    """ Like Model """

    creator = models.ForeignKey(user_models.User, models.SET_NULL, null=True,)
    image = models.ForeignKey(Image, models.SET_NULL, null=True,)