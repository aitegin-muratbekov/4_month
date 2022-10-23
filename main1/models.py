from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name

class Film(models.Model):
    title = models.CharField(max_length=255)
    rating = models.FloatField(default=0)
    film_director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, related_name='director')
    time = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return self.title