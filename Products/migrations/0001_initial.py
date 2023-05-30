# Generated by Django 4.1.7 on 2023-05-22 17:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('review', '0002_alter_reviewmodel_product_slug'),
        ('account', '0004_viewcounter_alter_user_options'),
        ('Category', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(max_length=50)),
                ('color_rgb', models.CharField(max_length=10)),
                ('slug', models.SlugField(unique=True)),
                ('status', models.CharField(choices=[('published', 'PUBLISHED'), ('unpublished', 'UNPUBLISHED')], default='published', max_length=20)),
                ('position', models.IntegerField(unique=True)),
            ],
            options={
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='SexToys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=65, verbose_name='عنوان')),
                ('photo', models.ImageField(upload_to='products_imagecs', verbose_name='تصویر')),
                ('price', models.IntegerField(verbose_name='قیمت')),
                ('off', models.IntegerField(blank=True, default=0, verbose_name='درصد تخفیف')),
                ('brand', models.CharField(blank=True, max_length=30, verbose_name='برند')),
                ('size', models.CharField(max_length=30, verbose_name='سایز')),
                ('about', models.TextField(verbose_name='توضیحات')),
                ('slug', models.SlugField(unique=True, verbose_name='اسلاگ')),
                ('inventory', models.CharField(choices=[('available', 'موجود'), ('unavailable', 'ناموجود')], default='Available', max_length=15, verbose_name='موجود')),
                ('publish', models.CharField(choices=[('published', 'منتشر شده'), ('unpublished', 'پیش نویس'), ('pending', 'درحال بررسی'), ('returned', 'برگشت داده شده')], default='unpublished', max_length=15, verbose_name='وضعیت انتشار')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('real', models.IntegerField(blank=True)),
                ('reason_for_return', models.TextField(blank=True, help_text='اگر قرار است محصول را رد کنید، چند خطی در مورد دلیل آن بنویسید', verbose_name='دلیل قبول نشدن محصول')),
                ('category', models.ManyToManyField(related_name='sexy_toys_related_name', to='Category.category', verbose_name='کتگوری')),
                ('color', models.ManyToManyField(to='Products.color', verbose_name='رنگ')),
                ('hits', models.ManyToManyField(blank=True, related_name='hits_related', to='account.viewcounter')),
                ('publisher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='publisher_Products', to=settings.AUTH_USER_MODEL, verbose_name='اضافه کننده')),
                ('review', models.ManyToManyField(blank=True, related_name='review_related', to='review.reviewmodel')),
            ],
            options={
                'ordering': ('-created',),
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]