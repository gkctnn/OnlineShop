from django.db import models
from django.db.models.signals import pre_save
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True,blank=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=30)
    sale_price = models.DecimalField(max_digits=100,decimal_places=2,blank=True, null=True)
    def __unicode__(self): #def __str__(self):
        return self.title

	#
	#
	# active = models.BooleanField(default=True)
	# categories = models.ManyToManyField('Category', blank=True)
	# default = models.ForeignKey('Category', related_name='default_category', null=True, blank=True)
    #
	# objects = ProductManager()

	# class Meta:
	# 	ordering = ["-title"]



	# def get_absolute_url(self):
	# 	return reverse("product_detail", kwargs={"pk": self.pk})
    #
	# def get_image_url(self):
	# 	img = self.productimage_set.first()
	# 	if img:
	# 		return img.image.url
	# 	return img #None
