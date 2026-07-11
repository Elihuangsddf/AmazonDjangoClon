from django.db import models

class Oferta(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    descuento = models.DecimalField(max_digits=5, decimal_places=2, help_text="Porcentaje de descuento")
    precio_oferta = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    imagen = models.ImageField(upload_to='ofertas/images', blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Oferta"
        verbose_name_plural = "Ofertas"

    def __str__(self):
        return self.titulo

    @property
    def nombre(self):
        return self.titulo
