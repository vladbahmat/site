from django.db import models

class Feedback(models.Model):
    email=models.EmailField()
    comment=models.CharField(max_length=256)

    def __str__(self):
        return 'Емаил-{0}, Коммент-{1}'.format(self.email,self.comment)
