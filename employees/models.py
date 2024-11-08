from django.db import models
from django.utils import timezone


class Department(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "department"
        verbose_name_plural = "departments"

    

class Employee(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=255)
    is_married = models.BooleanField(default=False)
    salary =models.FloatField(default=0.0)
    contract_exp = models.DateTimeField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.first_name} {self.last_name} |{self.s}"
    
    class Meta:
        verbose_name = "employee"
        verbose_name_plural = "employees"
    


class About(models.Model):
    title = models.CharField(max_length=255)
    body =models.TextField()
    
    def __str(self):
        return self.title


    class Meta:
        verbose_name = "about"
        verbose_name_plural = "abouts"
    
class Contact(models.Model):
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.address}|{self.email}|{self.phone}"


    class Meta:
        verbose_name = "contact"
        verbose_name_plural = "contacts"


class Team(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    position = models.CharField(max_length=55)
    about = models.TextField(max_length=255)
    avatar = models.ImageField(upload_to="team")

    def __str__(self):
        return f"{self.first_name} {self.last_name} | {self.position}"
    
    class Meta:
        verbose_name = "team"
        verbose_name_plural = "teams"