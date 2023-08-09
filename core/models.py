from django.db import models
from stdimage.models import StdImageField

#SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify


class Base(models.Model):
    creation = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        abstract = True
        
        
class Product(Base):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    stock = models.IntegerField()
    image = StdImageField(upload_to='products', variations={'thumb': (124, 124)})
    slug = models.SlugField(max_length=100, blank=True, editable=False)
    
    def __str__(self) -> str:
        return self.name
    

def product_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.name)
    
    
signals.pre_save.connect(product_pre_save, sender=Product)