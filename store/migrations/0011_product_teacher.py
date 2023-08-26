# Generated by Django 4.1.5 on 2023-08-24 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0008_alter_teacher_city'),
        ('store', '0010_remove_product_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher'),
        ),
    ]
