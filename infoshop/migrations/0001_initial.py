# Generated by Django 2.2 on 2019-04-21 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True, verbose_name='Удалено')),
                ('name', models.CharField(db_index=True, max_length=250, verbose_name='Имя')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('owner_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='infoshop.Owner')),
                ('alias', models.SlugField(max_length=300)),
                ('published', models.BooleanField(db_index=True, default=False, verbose_name='Опубликовано')),
                ('seo_keywords', models.CharField(max_length=512, null=True, verbose_name='SEO ключевые слова')),
                ('seo_description', models.TextField(null=True, verbose_name='SEO описание')),
                ('content', models.TextField(null=True, verbose_name='Контент')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
            ],
            options={
                'abstract': False,
            },
            bases=('infoshop.owner', models.Model),
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.SlugField(max_length=300)),
                ('published', models.BooleanField(db_index=True, default=False, verbose_name='Опубликовано')),
                ('seo_keywords', models.CharField(max_length=512, null=True, verbose_name='SEO ключевые слова')),
                ('seo_description', models.TextField(null=True, verbose_name='SEO описание')),
                ('content', models.TextField(null=True, verbose_name='Контент')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('deleted', models.DateTimeField(editable=False, null=True, verbose_name='Удалено')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Имя')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='infoshop.ProductCategory')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.SlugField(max_length=300)),
                ('published', models.BooleanField(db_index=True, default=False, verbose_name='Опубликовано')),
                ('seo_keywords', models.CharField(max_length=512, null=True, verbose_name='SEO ключевые слова')),
                ('seo_description', models.TextField(null=True, verbose_name='SEO описание')),
                ('content', models.TextField(null=True, verbose_name='Контент')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('deleted', models.DateTimeField(editable=False, null=True, verbose_name='Удалено')),
                ('name', models.CharField(db_index=True, max_length=250, verbose_name='Название')),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d/', verbose_name='Изображение товара')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('price_new', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Новая цена')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='infoshop.ProductCategory', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['name'],
                'index_together': {('id', 'alias')},
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('owner_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='infoshop.Owner')),
                ('alias', models.SlugField(max_length=300)),
                ('published', models.BooleanField(db_index=True, default=False, verbose_name='Опубликовано')),
                ('seo_keywords', models.CharField(max_length=512, null=True, verbose_name='SEO ключевые слова')),
                ('seo_description', models.TextField(null=True, verbose_name='SEO описание')),
                ('content', models.TextField(null=True, verbose_name='Контент')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='infoshop.School', verbose_name='Школа')),
            ],
            options={
                'abstract': False,
            },
            bases=('infoshop.owner', models.Model),
        ),
    ]
