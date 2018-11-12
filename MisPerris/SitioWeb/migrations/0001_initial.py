# Generated by Django 2.1.2 on 2018-10-22 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CorreoElectronico', models.CharField(max_length=100)),
                ('Run', models.CharField(max_length=10)),
                ('Nombre', models.CharField(max_length=50)),
                ('FechaNacimiento', models.DateField()),
                ('Telefono', models.IntegerField()),
                ('region', models.CharField(max_length=50)),
                ('comuna', models.CharField(max_length=50)),
                ('tipoCasa', models.CharField(max_length=50)),
            ],
        ),
    ]
