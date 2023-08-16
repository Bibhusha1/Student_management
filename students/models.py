from django.db import models

class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    SEMESTER_CHOICES = [
        ('1', '1st Semester'),
        ('2', '2nd Semester'),
        ('3', '3rd Semester'),
        ('4', '4th Semester'),
        ('5', '5th Semester'),
        ('6', '6th Semester'),
        ('7', '7th Semester'),
        ('8', '8th Semester'),
    ]

    GRADE_CHOICES = [
        ('BIM', 'Bachelor of Information Management'),
        ('BBM', 'Bachelor of Business Management'),
        ('BBA', 'Bachelor of Business Administration'),
        ('BCA', 'Bachelor of Computer Applications'),
        ('CSIT', 'Bachelor of Computer Science and Information Technology'),
        # Add more choices as needed
    ]

    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    dob = models.DateField()
    grade = models.CharField(max_length=4, choices=GRADE_CHOICES)
    semester = models.CharField(max_length=1, choices=SEMESTER_CHOICES)
    emailid = models.EmailField()
    phone = models.BigIntegerField()
    address = models.CharField(max_length=100)

  


    def __str__(self):
        return self.name
