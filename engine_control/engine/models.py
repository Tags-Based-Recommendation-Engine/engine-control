from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=255)

class Tag(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.CharField(max_length=100)

class User(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

class Item(models.Model):
    item_name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
class Item_tag(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    score = models.IntegerField(default = 0)

class Transactions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    response = models.IntegerField(default = 3)

class UserInterests(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    score = models.IntegerField(default = 0)

class UserCluster(models.Model):
    cluster_name = models.CharField(max_length=255)

class UserClusterTags(models.Model):
    cluster = models.ForeignKey(UserCluster, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    score = models.IntegerField(default = 0)

class User_Cluster(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cluster = models.ForeignKey(UserCluster, on_delete=models.CASCADE)
    corelation = models.IntegerField(default=0)

class UClusterCorelation(models.Model):
    cluster = models.ForeignKey(UserCluster, on_delete=models.CASCADE)
    item_cluster = models.ForeignKey(Category, on_delete=models.CASCADE)
    corelation = models.IntegerField(default=0)

class Recommendations(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    corelation = models.IntegerField(default=0)