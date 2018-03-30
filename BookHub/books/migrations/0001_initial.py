# Generated by Django 2.0.3 on 2018-03-30 15:16

from django.db import migrations, models
import django.db.models.deletion
import isbn_field.fields
import isbn_field.validators
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='catalogue number')),
                ('title', models.CharField(db_index=True, max_length=100)),
                ('description', models.TextField()),
                ('publication_date', models.DateField()),
                ('image_url', models.URLField()),
                ('cover', models.CharField(choices=[('hardcover', 'Hardcover'), ('paperback', 'Paperback')], default='paperback', max_length=9)),
                ('language', models.CharField(choices=[('PL', 'Polish'), ('EN', 'English')], default='PL', max_length=2)),
                ('isbn', isbn_field.fields.ISBNField(db_index=True, max_length=28, validators=[isbn_field.validators.ISBNValidator], verbose_name='ISBN')),
                ('authors', models.ManyToManyField(to='books.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('website', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Publisher'),
        ),
    ]
