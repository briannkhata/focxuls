from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name


class Advocate(models.Model):
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    username = models.CharField(max_length=200)
    bio = models.TextField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.username

class Usertype(models.Model):
    usertype_id = models.BigAutoField(primary_key=True)
    usertype_name = models.CharField(max_length=200)
    deleted = models.IntegerField(default=0)
    def __str__(self):
        return self.usertype_name
    
class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    usertype_id = models.ForeignKey(Usertype, on_delete=models.SET_NULL, null=True)
    deleted = models.IntegerField(default=0)
    def __str__(self):
        return self.Name

class Folder(models.Model):
    folder_id = models.BigAutoField(primary_key=True)
    folder_name = models.CharField(max_length=200)
    deleted = models.IntegerField(default=0)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.folder_name

class Plan(models.Model):
    plan_id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200)
    cost = models.BigIntegerField()
    duration = models.CharField(max_length=200)
    deleted = models.IntegerField(default=0)
    def __str__(self):
        return self.title

class Subscription(models.Model):
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.title


class File(models.Model):
    file_id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    path = models.TextField(max_length=250, null=True, blank=True)
    deleted = models.IntegerField(default=0)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    folder_id = models.ForeignKey(Folder, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
