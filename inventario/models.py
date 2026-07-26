from django.db import models


class Categoria(models.Model):
    """Categoría para agrupar artículos (Herramientas, Insumos, Repuestos, etc.)."""
    nombre = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=256, blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.nombre


class Articulo(models.Model):
    """Artículo del inventario de StockControl."""
    nombre = models.CharField(max_length=150)
    codigo = models.CharField("Código de barra", max_length=50)
    descripcion = models.CharField(max_length=256, blank=True)
    stock = models.IntegerField(default=0)
    ubicacion = models.CharField("Ubicación / Bodega", max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"

    def __str__(self):
        return self.nombre
