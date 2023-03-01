# Generated by Django 4.1.5 on 2023-03-01 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0002_membershippurchase_shortlistedcandidates_and_more'),
        ('superuser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_paid', models.FloatField(max_length=10)),
                ('payment_id', models.CharField(max_length=100, null=True)),
                ('payment_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('membership', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='recruiter.subscriptionplan')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='recruiter.company')),
            ],
        ),
    ]
