# Generated by Django 3.2.13 on 2023-11-21 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='about_us_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('comments', models.TextField()),
                ('gasStationAddr', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Gas_Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_name', models.CharField(max_length=200)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('regular_gas_price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('premium_gas_price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('diesel_price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GasStation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=255)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('services_offered', models.TextField()),
                ('amenities', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='GasStationListing',
            fields=[
                ('listing_id', models.AutoField(primary_key=True, serialize=False)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='station_tracker.gasstation')),
            ],
        ),
        migrations.CreateModel(
            name='GasStationOwner',
            fields=[
                ('owner_id', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('owner_name', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('business_address', models.CharField(max_length=255)),
                ('emergency_contact', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GasStationReview',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=100)),
                ('rating', models.IntegerField(default=0)),
                ('review_text', models.TextField()),
                ('gas_station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='station_tracker.gasstationlisting')),
            ],
        ),
        migrations.AddField(
            model_name='gasstationlisting',
            name='station_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='station_tracker.gasstationowner'),
        ),
        migrations.AddField(
            model_name='gasstation',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='station_tracker.gasstationowner'),
        ),
        migrations.CreateModel(
            name='CustomerInquiry',
            fields=[
                ('inquiry_id', models.AutoField(primary_key=True, serialize=False)),
                ('sender_name', models.CharField(max_length=100)),
                ('sender_email', models.EmailField(max_length=254)),
                ('message_text', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Resolved', 'Resolved'), ('Closed', 'Closed')], default='Pending', max_length=10)),
                ('gas_station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='station_tracker.gasstationlisting')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
