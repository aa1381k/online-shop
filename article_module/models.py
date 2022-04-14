from django.db import models

# Create your models here.
from account_module.models import User


class articlecategorymodel(models.Model):
    parrent = models.ForeignKey('articlecategorymodel',null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    url_title = models.CharField(max_length=200,unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'article category'


class articlemodel(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(db_index=True,allow_unicode=True)
    image = models.ImageField(upload_to='images/article')
    short_description = models.TextField()
    text  = models.TextField()
    is_active = models.BooleanField(default=True)
    selected_category = models.ManyToManyField(articlecategorymodel)
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True,editable=False)
    create_date = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.title

    def get_jalali_create_time(self):
        return self.create_date.strftime("%H:%M")



class articlecomments(models.Model):
    article = models.ForeignKey(articlemodel, on_delete=models.CASCADE)
    parent = models.ForeignKey('articlecomments',on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True, editable=False)
    text = models.TextField()

    def __str__(self):
        return str(self.user)