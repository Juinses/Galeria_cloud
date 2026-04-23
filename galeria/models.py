from django.db import models

class GaleriaFotos(models.Model):
    # 'idgaleria' con AutoField es el equivalente a PK (Primary Key) y AI (Auto Increment)
    idgaleria = models.AutoField(primary_key=True, db_column='idgaleria')
    
    # 'foto' corresponde a VARCHAR(45)
    foto = models.CharField(max_length=45)
    
    # 'estado' corresponde a VARCHAR(45)
    estado = models.CharField(max_length=45)

    class Meta:
        # Esto asegura que Django busque la tabla llamada 'Galeria_fotos'
        db_table = 'Galeria_fotos'
        # Esto evita que Django agregue una 's' al final del nombre de la tabla
        managed = True 

    def __str__(self):
        return f"{self.foto} - {self.estado}"