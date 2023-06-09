# Generated by Django 3.2.5 on 2023-05-05 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20230504_1009'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-created'], 'verbose_name': 'Product', 'verbose_name_plural': 'Product'},
        ),
        migrations.AddField(
            model_name='productcategory',
            name='description_en',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='商品分類描述(英)'),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='name_en',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='商品分類名稱(英)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='product_set', to='products.productcategory', verbose_name='Product Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created Date'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Product Description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Modified Date'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Product Name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='Product Price'),
        ),
    ]
