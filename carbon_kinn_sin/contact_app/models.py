from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta

User = get_user_model()

class ContactMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    name = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"

class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='reports/', blank=True, null=True)  # Add image field
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report by {self.user.email} at {self.created_at}"

    def clean(self):
        one_hour_ago = timezone.now() - timedelta(hours=1)
        if Report.objects.filter(user=self.user, created_at__gte=one_hour_ago).exists():
            raise ValidationError("You can only submit one report every hour.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
