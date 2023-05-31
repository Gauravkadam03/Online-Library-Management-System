from django.db import models

# Create your models here.

class book(models.Model):
    B_name=models.CharField(max_length=60)
    A_name=models.CharField(max_length=25)
    Date=models.CharField(max_length=25)
    B_category=models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.B_name 

class issue_book(models.Model):
    s_id = models.IntegerField()
    b_name = models.CharField(max_length=25)
    s_name = models.CharField(max_length=25)

class i_b_data(models.Model):
    s_id = models.IntegerField()
    s_name = models.CharField(max_length=25)
    b_name = models.CharField(max_length=25)
    Date=models.CharField(max_length=25)