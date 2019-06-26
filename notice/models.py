from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
class Notice(models.Model):
    title=models.CharField(max_length=300)
    body=models.TextField()
    file=models.FileField(upload_to='document/',null=True)
    update_date=models.DateTimeField(auto_now=True)
    hit=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:50]

    @property
    def update_counter(self):
        self.hit=self.hit+1
        self.save()

