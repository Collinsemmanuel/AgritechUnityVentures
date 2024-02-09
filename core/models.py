# Create your models here.
# core/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    # Custom user model extending AbstractUser
    ROLES = [
        ('farmer', 'Farmer'),
        ('investor', 'Investor'),
        ('agricultural_expert', 'Agricultural Expert'),
    ]

    role = models.CharField(max_length=20, choices=ROLES)

    #add related_nme avoiding clashes
    groups = models.ManyToManyField(Group, related_name='core_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='core_user_set', blank=True)

    def __str__(self):
        return self.username

class Project(models.Model):
    # Model for agricultural projects
    name = models.CharField(max_length=255)
    description = models.TextField()
    funding_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Loan(models.Model):
    # Model for loans
    LOAN_TYPES = [
        ('smartphone', 'Smartphone Loan'),
        ('laptop', 'Laptop Loan'),
        ('motorbike', 'Motorbike Loan'),
        ('car', 'Car Loan'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    loan_type = models.CharField(max_length=20, choices=LOAN_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.get_loan_type_display()}"

class BlogPost(models.Model):
    # Model for blog posts or news updates
    title = models.CharField(max_length=255)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
