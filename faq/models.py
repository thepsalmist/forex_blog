from django.db import models


class ForexFaq(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Faq(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f"Question by {self.name}"