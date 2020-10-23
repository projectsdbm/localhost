from django.db import models

# Create your models here.
class DepartmentModel(models.Model):
    dept_name = models.CharField(max_length=100)

    def __str__(self):
        return self.dept_name


class StudentModel(models.Model):
    picture = models.ImageField(upload_to='profile_pics/',null=True,blank=True,default='profile_pics/nodetail.jpg')
    name = models.CharField(max_length=50)
    parent_name = models.CharField(max_length=50)
    parent_phone = models.CharField(max_length=10)
    roll_no = models.CharField(max_length=9,unique=True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=16)
    phone_no = models.CharField(max_length=10,unique=True)
    department = models.ForeignKey(DepartmentModel,on_delete=models.CASCADE)
    Class = models.CharField(max_length=1)
    year = models.IntegerField()
    bus_no = models.CharField(max_length=3)
    address1 = models.CharField(max_length=200)
    city = models.CharField(max_length=20)

    def __str__(self):
        return "@"+self.name+"-"+self.roll_no
