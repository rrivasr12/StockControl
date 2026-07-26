import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Categoria",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nombre", models.CharField(max_length=150)),
                ("descripcion", models.CharField(blank=True, max_length=256)),
                ("creado", models.DateTimeField(auto_now_add=True)),
                ("actualizado", models.DateTimeField(auto_now=True)),
            ],
            options={"verbose_name": "Categoría", "verbose_name_plural": "Categorías"},
        ),
        migrations.CreateModel(
            name="Articulo",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nombre", models.CharField(max_length=150)),
                ("codigo", models.CharField(max_length=50, verbose_name="Código de barra")),
                ("descripcion", models.CharField(blank=True, max_length=256)),
                ("stock", models.IntegerField(default=0)),
                ("ubicacion", models.CharField(max_length=100, verbose_name="Ubicación / Bodega")),
                ("categoria", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="inventario.categoria")),
		("creado", models.DateTimeField(auto_now_add=True)),
		("actualizado", models.DateTimeField(auto_now=True)),
            ],
            options={"verbose_name": "Artículo", "verbose_name_plural": "Artículos"},
        ),
    ]
