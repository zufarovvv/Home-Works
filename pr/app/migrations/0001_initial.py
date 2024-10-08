# Generated by Django 4.2.16 on 2024-09-11 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='IceCream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Parrent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.child')),
                ('ice_cream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.icecream')),
            ],
        ),
        migrations.AddField(
            model_name='child',
            name='ice_cream',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.icecream'),
        ),
    ]
