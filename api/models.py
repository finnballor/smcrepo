from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=200, null= False, blank = False )
    description = models.CharField(max_length= 200, null=True, blank = True )

    def __str__(self) -> str:
        return self.name



# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=200, null= False, blank = False )
    subject_code = models.CharField(max_length= 200, null=True, blank = True )

    def __str__(self) -> str:
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length= 200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=25,)
    image = models.ImageField(upload_to = 'teacher/images/' )


    def __str__(self) -> str:
        return self.name
