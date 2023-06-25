from django.db import models
from django.utils import timezone

# Create your models here.
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    f_name = models.CharField(max_length=256, null=False)
    l_name = models.CharField(max_length=256, null=False)
    date_of_birth = models.DateField(null=True)
    nationality = models.CharField(max_length=256, null=True)

    class Meta:
        ordering = ['l_name', 'f_name']


class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    pub_name = models.CharField(max_length=256, null=False)
    country  = models.CharField(max_length=256, null=False)
    city = models.CharField(max_length=256, null=True)
    estd = models.IntegerField(null=True)


class Books(models.Model):
    id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=256, null=False)
    author_name = models.ForeignKey(Author, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13, unique=True)
    pub_year = models.IntegerField(null=True)
    pub_name = models.ForeignKey(Publisher, on_delete=models.CASCADE)




