from django.db import models

# Create your models here.

class Ciudad(models.Model):
    codigo = models.PositiveSmallIntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)

class Persona(models.Model):
    dni = models.CharField(max_length=10, primary_key=True)
    primerApellido = models.CharField(max_length=40)
    segundoApellido = models.CharField(max_length=40)
    nombres = models.CharField(max_length=40)
    ciudad = models.ForeignKey(Ciudad, null=False, blank=False, on_delete=models.CASCADE)

    def nombreCiompleto(self):
        txt = "{0} {1}, {2}"
        return txt.format(self.primerApellido, self.segundoApellido, self.nombres)

class Telefono(models.Model):
    persona = models.ForeignKey(Persona, null=False, blank=False, on_delete=models.CASCADE)
    numero = models.CharField(max_length=10)

class Email(models.Model):
    persona = models.ForeignKey(Persona, null=False, blank=False, on_delete=models.CASCADE)
    email = models.CharField(max_length=100)

