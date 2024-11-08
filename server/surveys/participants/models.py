from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Occupation(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Participant(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.RESTRICT)
    occupation = models.ForeignKey(Occupation, on_delete=models.RESTRICT)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
  