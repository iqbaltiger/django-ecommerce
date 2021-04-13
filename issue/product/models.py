from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

yes_or_no = (
       (1,'Yes'),
       (0,'No')

    )


class Category(models.Model):

    cat_name = models.CharField(max_length=50,blank=True,null=True,unique=True)
    parent_cat = models.ForeignKey("self",on_delete = models.SET_NULL,related_name='child_category_list',blank=True,null=True)

    category_image = models.ImageField(upload_to='images/',default="dummy-profile-pic-male1.webp", null=True)
    category_favicon_icon = models.ImageField(upload_to='images/',default="dummy-profile-pic-male1.webp", null=True)   
    status = models.BooleanField(default=True)  # published or not 
                                                                                                                                   
    def __str__(self):
        return self.cat_name


#Brand Info

class Brand(models.Model):

    brand_name = models.CharField(max_length=50,blank=False,null=True,unique=True)
    brand_image = models.ImageField(upload_to='images/',default="dummy-profile-pic-male1.webp", null=True)
    website = models.CharField(max_length=50,blank=False,null=True,unique=True)
    status = models.BooleanField(default=True)  # published or not 
                                                                                                                                   
    def __str__(self):
        return self.brand_name

#Product Variant
    
class Variant(models.Model):

    variant_name = models.CharField(max_length=50,blank=False,null=True,unique=True)
    variant_status = models.BooleanField(default=True)

    def __str__(self):
        return self.variant_name


#Product Unit
class Unit(models.Model):

    unit_name = models.CharField(max_length=50,blank=False,null=True,unique=True)
    unit_short_name = models.CharField(max_length=30,blank=False,null=True,unique=True)

    def __str__(self):
        return self.unit_name        

#Product Currency
class Currency(models.Model):

    

    left_or_right = (
       (0,'Left'),
       (1,'Right')

    )    

    currency_name = models.CharField(max_length=50,blank=False,null=True,unique=True)
    currency_icon = models.CharField(max_length=50,blank=False,null=True,unique=True)

    currency_position = models.IntegerField(choices=left_or_right,default='1')

    convertion_rate = models.FloatField(null=False)    
    default_status = models.IntegerField(choices=yes_or_no,default='1')

    def __str__(self):
        return self.currency_name
    
#Supplier

class Supplier(models.Model):


    supplier_name = models.CharField(max_length=50,blank=False,null=True)
    supplier_address = models.TextField(null=True,blank=True)
    supplier_mobile = models.CharField(max_length=50,blank=False,null=True,unique=True)
    supplier_email = models.EmailField(unique=True)
    supplier_details = models.TextField(null=True,blank=True)
    supplier_website = models.CharField(max_length=50,blank=False,null=True)
    status = models.BooleanField(default=True)  # published or not 

    def __str__(self):
        return self.supplier_name
    
class Product(models.Model):

    product_name = models.CharField(max_length=50,null=True)
    category = models.ForeignKey(Category,on_delete = models.PROTECT,related_name='product_category',null=True)
    product_details = RichTextField(null=True,blank=True)
    invoice_details = RichTextField(null=True,blank=True)
    unit = models.ForeignKey(Unit,on_delete = models.PROTECT,related_name='product_unit_measurement',null=True)
    offer = models.IntegerField(choices=yes_or_no,default='1')
    best_sale = models.IntegerField(choices=yes_or_no,default='1')
    review = RichTextField(null=True,blank=True)
    specification = RichTextField(null=True,blank=True)
    description = RichTextField(null=True,blank=True)
    brand = models.ForeignKey(Brand,on_delete=models.PROTECT,related_name='product_brand',null=True)
    tag = models.CharField(max_length=30,blank=True,null=True)
    offer_price = models.FloatField(max_length=10,null=True,blank=True)
    default_image = models.ImageField(upload_to='images/',default="dummy-profile-pic-male1.webp", null=True)
    image = models.ImageField(upload_to='images/',default="dummy-profile-pic-male1.webp", null=True)
    sell_price = models.FloatField(max_length=10,null=True)
    supplier_price = models.FloatField(max_length=10,null=True)
    product_model = models.CharField(max_length=30,blank=True,null=True) 
    supplier = models.ForeignKey(Supplier,on_delete=models.PROTECT,null=True,related_name="supplier_info")
    variant = models.ForeignKey(Variant,on_delete=models.PROTECT,related_name='product_variant',blank=True,null=True)
    video_link  = models.CharField(max_length=30,blank=True,null=True) 

    def __str__(self):
        return self.product_name
     