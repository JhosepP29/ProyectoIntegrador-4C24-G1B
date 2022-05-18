from django.db import models

# Create your models here.

class Administrador(models.Model):
    ADMIN = 'admin'
    CLIENTE = 'cliente'

    ESTADO_OPCIONES = (
        (ADMIN, 'Admin'),
        (CLIENTE, 'Cliente'),
    )

    codigo = models.IntegerField(unique=True)
    usuario = models.CharField(max_length=100, unique=True)
    contraseña = models.CharField(max_length=100)
    correo = models.EmailField('User Email')
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    estado = models.CharField(max_length=10, choices=ESTADO_OPCIONES)

class Cliente(models.Model):
    codigo = models.IntegerField(unique=True)
    usuario = models.CharField(max_length=100, unique=True)
    contraseña = models.CharField(max_length=100)
    correo = models.EmailField('User Email')
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fec_registro = models.DateTimeField('Fecha de Registro')

class Habitacion(models.Model):
    UNO = 1
    DOS = 2

    PISO_OPCIONES = (
        (UNO, 1),
        (DOS, 2),
    )
    codigo = models.IntegerField(unique=True)
    tipo = models.CharField(max_length=100)
    n_habitacion = models.IntegerField(unique=True)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=100)
    n_piso = models.IntegerField(verbose_name='N° Piso', choices=PISO_OPCIONES)

class Pago(models.Model):
    Debito = "Tarjeta de Debito"
    Credito = "Tarjeta de credito"

    TIPO_OPCIONES = (
        (Debito, "Tarjeta de Debito"),
        (Credito, "Tarjeta de Credito"),
    )
    tipo = models.CharField(max_length=100, choices=TIPO_OPCIONES)
    total = models.IntegerField()
    fec_salida = models.DateTimeField('fecha salida')

class Reserva(models.Model):
    fec_entrada = models.DateTimeField('fecha entrada')
    fec_salida = models.DateTimeField('fecha salida')
    cant_personas = models.IntegerField()