from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='userprofile/img/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} | {self.last_name}'

class Doctor(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=100)
    license_number = models.PositiveIntegerField()
    years_of_experience = models.PositiveIntegerField()
    education = models.CharField(max_length=100)
    hospital = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user.user}'


class MedicalRecord(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='MedicalRecord')
    record_type = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    doctor = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.user}'


class Appointment(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    reason = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.user.user}'

class Medication(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dosage = models.PositiveIntegerField()
    schedule = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.user.user}'

class FitnessProgram(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f'{self.user.user}'

class Notification(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.user}'

