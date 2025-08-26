from django.db import models


class Product(models.Model):
    # Choices خاصة بالتصنيفات
    class Category(models.TextChoices):
        ELECTRONICS = 'ELEC', 'Electronics'
        FASHION     = 'FASH', 'Fashion'
        HOME        = 'HOME', 'Home'
        OTHER       = 'OTHR', 'Other'

    name = models.CharField(
        max_length=100,
        verbose_name='Product Name',
        help_text='Enter a clear product name'
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.0,  # لازم default علشان الـ migrate ينجح
        help_text='Price in your local currency'
    )

    available = models.BooleanField(default=True)  # الحقل القديم عندك

    # حقول جديدة للـ Lab 4
    category = models.CharField(
        max_length=4,
        choices=Category.choices,
        default=Category.OTHER
    )

    stock = models.IntegerField(
        default=0,
        help_text='Units in inventory'
    )

    released_on = models.DateField(
        blank=True,
        null=True
    )

    added_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    image = models.ImageField(
        upload_to='products/',
        blank=True,
        null=True
    )

    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]
    rating = models.IntegerField(
        choices=RATING_CHOICES,
        default=5
    )

    def _str_(self):
        return f"{self.name} ({self.get_category_display()})"

    class Meta:
        ordering = ['name']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'