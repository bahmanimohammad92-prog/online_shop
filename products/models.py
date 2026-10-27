from django.db import models

class Category(models.Model):
    title = models.CharField(
        max_length=255, 
        verbose_name="عنوان"
        )
    
    slug = models.SlugField(
        unique=True, 
        verbose_name="شناسه دسته بندی"
        )

    class Meta:
        verbose_name_plural = "دسته بندی ها"

    def __str__(self):
        return self.title
    

class Product(models.Model):

    category = models.ForeignKey(
        Category, on_delete=models.PROTECT,
        related_name="products",
        verbose_name="دسته‌بندی"
        )
    
    name = models.CharField(
        max_length=255, 
        verbose_name="نام محصول"
        )
    
    price = models.PositiveBigIntegerField(
        verbose_name="قیمت محصول"
        )
    
    stock = models.PositiveIntegerField(
        verbose_name="تعداد موجود در انبار",
        default=0
        )
    
    discount_price = models.PositiveBigIntegerField(
        null=True,
        blank=True, 
        verbose_name="قیمت با تخفیف"
        )
    
    slug = models.SlugField(
        unique=True, 
        verbose_name="شناسه محصول"
        )
    
    description = models.TextField(
        verbose_name="توضیحات"
        )
    
    is_active = models.BooleanField(
        default=True, 
        verbose_name="فعال بودن محصول"
        )
    
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="تاریخ ایجاد"
        )


    class Meta:
        verbose_name_plural = "محصولات"

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.ImageField(
        upload_to="products/", 
        verbose_name="تصویر محصول"
        ) 
       
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="محصول"
        )
    
    is_primary = models.BooleanField(
        verbose_name="تصویر اصلی",
        default=False
        )
    
    sort_order = models.PositiveSmallIntegerField(
        verbose_name="ترتیب نمایش تصاویر",
        default=0
        )


    class Meta:
        verbose_name = "عکس محصولات"
        verbose_name_plural = "عکس های محصول"
        ordering = ["sort_order", "id"]

    def __str__(self):
        return f"{self.product.name} - تصویر {self.pk}"
            
    

    