from django.db import models

class ImagePrompt(models.Model):
    prompt = models.TextField()
    prompt_image = models.ImageField(upload_to='images_for_automation/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.prompt[:50]  # First 50 characters

class Registration(models.Model):
    name = models.TextField()
    email = models.EmailField(unique=True)
    password = models.TextField()


class Feedback(models.Model):
    name = models.TextField()
    email = models.EmailField()
    feedback = models.TextField()

class Contact(models.Model):
    name = models.TextField()
    email = models.EmailField()
    message = models.TextField()
