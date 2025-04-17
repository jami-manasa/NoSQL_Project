from django.db import models

# Create your models here.
from djongo import models

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    
    def __str__(self):
        return self.username

class CommunityPost(models.Model):
    username = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} - {self.timestamp.strftime('%Y-%m-%d %H:%M')}"


class MentorshipPost(models.Model):
    MENTORSHIP_TYPE_CHOICES = [
        ('offer', 'Offering Mentorship'),
        ('request', 'Requesting Mentorship'),
    ]

    username = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()
    MENTORSHIP_TYPE_CHOICES = [
    ('offer', 'Offering Mentorship'),
    ('request', 'Requesting Mentorship'),]

    expertise_area = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} - {self.mentorship_type} - {self.title}"



class MentorshipRequest(models.Model):
    mentor = models.CharField(max_length=100)   # username of mentor
    student = models.CharField(max_length=100)  # username of student requesting
    message = models.TextField(blank=True)
    status = models.CharField(
        max_length=10,
        choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('ignored', 'Ignored')],
        default='pending'
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} → {self.mentor} ({self.status})"
