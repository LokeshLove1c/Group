from django.db import models

# Create your models here.
class History(models.Model):
    creation_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50)
    last_updated_by = models.CharField(max_length=50)
    last_updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
class Users(History):
    uid = models.AutoField(primary_key=True)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email_id = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=50)


    def __str__(self):
       return self.name

class Group(History):
    gid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(default="")


    def __str__(self):
        return self.name

class ExpenceEntry(History):
    exp_id = models.AutoField(primary_key=True)
    gid = models.ForeignKey(Group, on_delete=models.CASCADE)
    uid = models.ForeignKey(Users, on_delete=models.CASCADE)
    amount = models.IntegerField()
    name = models.CharField(max_length=50)
    tag = models.CharField(max_length=50)
    description = models.TextField(default="")


    def __srt__(self):
        return self.name

# class ExpenceEntryShare(models.Model):
#     exp_id = models.AutoField(primary_key = True)
#     uid = models.ForeignKey(Users, on_delete=models.CASCADE)
#     created_by = models.CharField(max_length=50)
#     created_on = models.DateTimeField(auto_now=False)
#     updated_by = models.CharField(max_length=50)
#     updated_on = models.DateTimeField(auto_now=False)


class UserGroup(models.Model):
    id = models.AutoField(primary_key=True)
    gid = models.ForeignKey(Group, on_delete=models.CASCADE)
    uid = models.ForeignKey(Users, on_delete=models.CASCADE)

class UserExpenceEntry(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.ForeignKey(Users, on_delete=models.CASCADE)
    gid = models.ForeignKey(Group, on_delete=models.CASCADE)

    