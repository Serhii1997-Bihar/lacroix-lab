import uuid
from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='Назва категорії')
    slug = models.SlugField(max_length=50, unique=True, blank=True, verbose_name='URL-слаг')

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            if not base_slug:
                base_slug = "category"

            slug = base_slug
            while Category.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{uuid.uuid4().hex[:6]}"

            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=30, verbose_name='Країна походження')

    class Meta:
        verbose_name = 'Країна'
        verbose_name_plural = 'Країни'

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=30, verbose_name='Назва бренду')

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренди'

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=10, verbose_name='Розмір')

    class Meta:
        verbose_name = 'Розмір'
        verbose_name_plural = 'Розміри'

    def __str__(self):
        return self.name


class Product(models.Model):
    class Gender(models.TextChoices):
        MALE = 'M', 'Чоловіча'
        FEMALE = 'F', 'Жіноча'
        UNISEX = 'U', 'Унісекс'

    name = models.CharField(max_length=255, verbose_name='Назва товару')
    slug = models.SlugField(max_length=255, unique=True, blank=True, verbose_name='URL-слаг')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products', verbose_name='Категорія')
    country = models.ForeignKey(Country, on_delete=models.PROTECT, related_name='products', verbose_name='Країна', blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='products', verbose_name='Бренд')
    image = models.ImageField(upload_to='products/', verbose_name='Фото')
    video = models.FileField(upload_to='products/videos/', verbose_name='Відеоогляд', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ціна')
    about = models.TextField(verbose_name='Інформація', blank=True)
    gender = models.CharField(max_length=1, choices=Gender.choices, default=Gender.UNISEX, verbose_name='Стать')
    sizes = models.ManyToManyField(Size, related_name='products', verbose_name='Розміри', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата оновлення')

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            if not base_slug:
                base_slug = "product"

            slug = base_slug
            while Product.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{uuid.uuid4().hex[:6]}"

            self.slug = slug

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=255, verbose_name="Ім'я")
    position = models.CharField(max_length=100, verbose_name='Посада', blank=True)
    achievement = models.TextField(verbose_name='Досягнення', blank=True)
    experience = models.CharField(max_length=100, verbose_name='Досвід', blank=True)
    image = models.ImageField(upload_to='employees/', verbose_name='Фото')
    bio = models.TextField(verbose_name='Біографія', blank=True)

    class Meta:
        verbose_name = 'Працівник'
        verbose_name_plural = 'Працівники'

    def __str__(self):
        return self.name