from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name

class Film(models.Model):
    title = models.CharField(max_length=255)
    rating = models.FloatField(default=0)
    film_director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True)
    time = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return self.title

class Comments(models.Model):
    nick = models.CharField(max_length=200)
    comm = models.TextField(max_length=1000)
    film = models.ForeignKey(Film, on_delete=models.CASCADE, null=True)

    def str(self):
        return self.nick

