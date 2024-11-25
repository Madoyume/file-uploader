from django.db import models

class File(models.Model):
    name = models.CharField(max_length=100)
    file = models.BinaryField(editable=True)
    insdate = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name