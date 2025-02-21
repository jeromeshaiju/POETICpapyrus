from django.db import models

class AIModel(models.Model):
    name = models.CharField(max_length=100)
    # Add more fields as needed