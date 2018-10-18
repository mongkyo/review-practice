from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        if self.name:
            return self.name
        return 'name null'


class Entry(models.Model):
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
    )
    headline = models.CharField(max_length=225)
    pub_date = models.DateField(blank=True, null=True)
    authors = models.ManyToManyField(Author, blank=True)
    n_comments = models.IntegerField(default=0)
    n_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.headline
