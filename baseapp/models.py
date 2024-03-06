from django.db import models

class VisitorDetails(models.Model):
    visitor_name = models.CharField(max_length=100)
    visitor_location = models.CharField(max_length=255)
    visitor_mobile_number = models.CharField(max_length=10)

    def __str__(self):
        return self.name