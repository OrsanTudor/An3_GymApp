from django.db import models


class Workout(models.Model):
    title = models.CharField(max_length=200, null=True, blank=False)
    date = models.DateField(editable=True, null=True, blank=False)
    description = models.TextField(null=True, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['date']


class ClasaPrincipala(models.Model):
    listaParticipanti = models.CharField(editable=False, max_length=200, null=True, blank=True)
    counterParticipanti = models.IntegerField(editable=False, null=True, blank=True)
    complete = models.BooleanField(editable=False, default=False)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, null=True, blank=False)
    title = models.CharField(max_length=200, null=True, blank=False)
    oraInceput = models.TimeField(editable=True, null=True, blank=False)
    create = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['workout']
