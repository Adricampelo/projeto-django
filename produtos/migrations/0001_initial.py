# Generated by Django 5.1.5 on 2025-02-26 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('categoria', models.CharField(max_length=255)),
                ('estoque', models.IntegerField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('codigo', models.CharField(max_length=50)),
                ('validade', models.DateField()),
                ('unidade', models.CharField(blank=True, max_length=50, null=True)),
                ('custo', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('estoque_minimo', models.IntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'db_table': 'produtos_produto',
            },
        ),
    ]
