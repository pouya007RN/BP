from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()


class Content(models.Model):
    title = models.CharField(max_length=64)
    text = models.TextField()
    
    def __str__(self) -> str:
        return self.title
    
    @property
    def content_rates(self):
        return self.rates.all()
    
    @property
    def content_rates_count(self):
        return self.content_rates.count()
    
    @property
    def content_rates_avg(self):
        return self.content_rates.aggregate(avg_rate=models.Avg('rate'))['avg_rate'] or 0
    
    
class ContentRate(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='rates')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rates')
    rate = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    
    class Meta:
        unique_together = ('content', 'user',)
    
    @classmethod
    def submit(cls, content, rate, user):
        content_rate, _ = cls.objects.get_or_create(content=content, user=user)
        content_rate.rate = rate
        content_rate.save()
        return content_rate
