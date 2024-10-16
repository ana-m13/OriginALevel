from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg, Count

# Here are the databases tables (called models by Django) 
# which will be converted to sql when it communicates with the database

# This table will be connected to the user. 
# Each user will be having a profile. 
# Django already created the users table
class OriginALevel_ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=15, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    teacher_code = models.CharField(max_length=6, blank=True, null=True)
    priviledges = models.IntegerField(blank=True, null=True)


# This is the question post. The answer post will get attached to the question post.
class OriginALevel_PostModel(models.Model):
    # constraint to user
    user_id = models.ForeignKey(User,related_name="user", on_delete=models.CASCADE)
    # # constraint to replays
    title = models.TextField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    tags = models.TextField(blank=True, null=True)
    tag_code = models.CharField(max_length=5, blank=True, null=True)
    tag_title = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False, blank=True, null=True)
    post_type = models.TextField(blank=True, null=True)

    @property 
    def get_rating_avg(self):
        average =  OriginALevel_RatingModel.objects.filter(post=self).aggregate(rating__avg=Avg('rating'))['rating__avg']
        if average:
            return average
        else:
            return float(0.0)

    @property
    def get_rating_count(self):
        return OriginALevel_RatingModel.objects.filter(post=self).aggregate(rating__count=Count('rating'))['rating__count']


# Answers post. Will be connected with the Post table through an ID
class OriginALevel_ReplyModel(models.Model):
    # constraint to user
    replied_by = models.ForeignKey(User, on_delete=models.CASCADE)
    # constraint to posts
    # every reply is accessed from PostModel
    post = models.ForeignKey(OriginALevel_PostModel,related_name='replies', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    body = models.TextField(blank=True, null=True)
    likes_count = models.IntegerField(blank=True, null=True)


# Will be linked with the User. 
class OriginALevel_SettingsModel(models.Model):
    # constraint to user
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    notify_on_reply = models.BooleanField(default=True, blank=True, null=True)



class OriginALevel_RatingModel(models.Model):
    # constraint to post
    post = models.ForeignKey(OriginALevel_PostModel, related_name='rating', on_delete=models.CASCADE)
    # constraint to user
    rated_by = models.ForeignKey(User, on_delete=models.CASCADE)
    # rating value
    rating = models.IntegerField(blank=True, null=True, default=0)


    def __str__(self):
        return f"{self.post} - {self.rated_by}: {self.rating}"