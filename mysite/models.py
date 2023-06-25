from django.db import models
from django.utils import timezone

# Create your models here.
class Author(models.Model):
    # f_name = first name, l_name = last name
    id = models.AutoField(primary_key=True)
    f_name = models.CharField(max_length=256, null=False)
    l_name = models.CharField(max_length=256, null=False)
    date_of_birth = models.DateField(default=timezone.now().date())
    nationality = models.CharField(max_length=256, null=True)

    class Meta:
        ordering = ['l_name', 'f_name']


class Publisher(models.Model):
    """
        columns:
            - id (primary key)
            - publisher name -> pub_name
            - country 
            - city 
            - estd -> established date
    """
    id = models.AutoField(primary_key=True)
    pub_name = models.CharField(max_length=256, null=False)
    country  = models.CharField(max_length=256, null=False)
    city = models.CharField(max_length=256, null=True)
    estd = models.DateField(default=timezone.now().date(), null=True)


class Books(models.Model):
    id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=256, null=False)
    author_name = models.ForeignKey(Author, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13, unique=True)
    pub_year = models.IntegerField(null=True)
    pub_name = models.ForeignKey(Publisher, on_delete=models.CASCADE)




