from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

def get_user(self):
    return self.username + " :" + self.first_name + " " + self.last_name
User.add_to_class("__str__", get_user)

class Category(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=45, primary_key=True)
    description = models.TextField(default="")
    def __str__(self):
        return self.name

class Group(models.Model):
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    description = models.TextField(null=True)
    image = models.ImageField(blank=True, null=True)
    def __str__(self):
        titleGroup = "{} : " + self.name
        return titleGroup.format(self.id)

class GroupBelongCategory(models.Model):
    objects = models.Manager()
    groupId = models.ForeignKey(Group, on_delete=models.CASCADE)
    categoryName = models.ForeignKey(Category, on_delete=models.CASCADE)

class Account(models.Model):
    objects = models.Manager()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.BooleanField(default=False, verbose_name='isMale')
    dateOfBirth = models.DateField(null=True, blank=True)
    hobby = models.TextField(default='', blank=True, null=True)
    avatar = models.ImageField(blank=True, null=True)
    coverPhoto = models.ImageField(blank=True, null=True)
    def __str__(self):
        title = self.user.__str__() + ' :{}'
        return title.format(self.dateOfBirth)

class AccountApplyGroup(models.Model):
    objects = models.Manager()
    userName = models.ForeignKey(User, on_delete=models.CASCADE)
    groupId = models.ForeignKey(Group, on_delete=models.CASCADE)
    timeApply = models.DateField(auto_now_add=True)

class Post(models.Model):
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    content = models.TextField(default='')
    image = models.ImageField(null=True)
    userName = models.ForeignKey(Account, on_delete=models.CASCADE)
    groupId = models.ForeignKey(Group, on_delete=models.CASCADE)
    timePost = models.DateField(auto_now_add=True)
    
class AccountReportPost(models.Model):
    objects = models.Manager()
    userName = models.ForeignKey(Account, on_delete=models.CASCADE)
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)
    content= models.TextField(default='')
    timeReport = models.DateField(auto_now_add=True)

class Comment(models.Model):
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    content = models.TextField(default='')
    username = models.ForeignKey(Account, on_delete=models.CASCADE)
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)
    timeComment = models.DateField(auto_now_add=True)

class accountReportComment(models.Model):
    objects = models.Manager()
    userName = models.ForeignKey(Account, on_delete=models.CASCADE)
    commentId = models.ForeignKey(Comment, on_delete=models.CASCADE)
    content = models.TextField(default='')
    timeReport = models.DateField(auto_now_add=True)

class GroupHasAccount(models.Model):
    objects = models.Manager()
    groupId = models.ForeignKey(Group, on_delete=models.CASCADE)
    userName = models.ForeignKey(User, on_delete=models.CASCADE)
    isAdmin = models.BooleanField(default=False);