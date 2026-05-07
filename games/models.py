from django.db import models



# Create your models here.
class products(models.Model):
    name =models.CharField(max_length=100)
    Description =models.TextField()
    Price =models.IntegerField()
    Quantity =models.IntegerField()
    Category =models.CharField(max_length=100)
    Image =models.ImageField (upload_to='products/')
    created_at =models.DateTimeField (auto_now_add=True)
    def __str__(self):
        return f"{self.name}"  
class User(models.Model):
    name = models.CharField(max_length=100)
    email=models.EmailField()
    password = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    phone=models.IntegerField()
    def __str__(self):
        return f"{self.name}"  
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(products,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Cart of {self.user.name}"             
class wishlist(models.Model): 
    user=models.ForeignKey(User,on_delete=models.CASCADE) 
    product=models.ForeignKey(products,on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True) 
 
    def __str__(self): 
        return f"wishlist of {self.user.name}"