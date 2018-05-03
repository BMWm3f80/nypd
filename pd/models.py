from django.db import models
from django.contrib.auth.models import User, AbstractUser


class Department(models.Model):
    Name = models.CharField(max_length=255)
    Zip_code = models.IntegerField()
    Number_of_weapons = models.IntegerField()
    Number_of_vehicles = models.IntegerField()
    Number_of_workers = models.IntegerField()
    Head = models.CharField(max_length=255)
    Area = models.IntegerField()

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'
    def __str__(self):
        return self.Name




class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    GENDER_OPTION = (
        ('Male', 'Male'),
        ('Female', 'Female')

    )
    gender = models.CharField(max_length=255, choices=GENDER_OPTION)
    date_of_birth = models.DateField()
    age = models.IntegerField()
    phone = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=8, decimal_places=2, default=800.00)
    card_number = models.CharField(max_length=255)
    gun_id = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    rank = models.IntegerField()
    working_hours = models.IntegerField()
    dep = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username




class Vehicle(models.Model):
    BelongsTo = models.ForeignKey(Department, on_delete=models.CASCADE)
    Plate_number = models.CharField(max_length=60)
    Model = models.CharField(max_length=255)
    isInUse = models.BooleanField(default=False)
    Using_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)



class Task(models.Model):
    Title = models.CharField(max_length=255)
    Description = models.TextField()
    isComplete = models.BooleanField(default=False)
    Dudate = models.DateField()
    Executed_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.Title

