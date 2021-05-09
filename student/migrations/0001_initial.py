# Generated by Django 2.1.7 on 2021-04-07 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('LearningManagementSytem', '__first__'),
        ('instructor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instructor.Courses')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LearningManagementSytem.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Opted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dated', models.DateTimeField(auto_now=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LearningManagementSytem.UserProfile')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LearningManagementSytem.Category')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instructor.Courses')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(default='', max_length=100, unique=True)),
                ('order_date', models.DateTimeField(auto_now=True)),
                ('total_amt', models.DecimalField(decimal_places=2, max_digits=30)),
                ('paid_by', models.CharField(default='Debit', max_length=20)),
                ('placed_by', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='LearningManagementSytem.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='opted',
            name='order',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='student.Orders'),
        ),
        migrations.AddField(
            model_name='opted',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LearningManagementSytem.SubCategory'),
        ),
        migrations.AlterUniqueTogether(
            name='cart',
            unique_together={('course', 'user')},
        ),
    ]
