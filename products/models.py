from django.db import models
from django.db.models.signals import pre_save,post_save
from django.utils.text import slugify
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True,blank=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=30)
    sale_price = models.DecimalField(max_digits=100,decimal_places=2,blank=True, null=True)
    def __unicode__(self): #def __str__(self):
        return self.title

def product_pre_save_reciever(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=slugify(instance.title)
product_pre_save_reciever(product_pre_save_reciever,sender=Product)

# def product_post_save_reciever(sender,instance,*args,**kwargs):
#     if instance.slug != slugify(instance.title):
#         instance.slug=slugify(instance.title)
#         instance.save()
# product_post_save_reciever(product_post_save_reciever,sender=Product)
