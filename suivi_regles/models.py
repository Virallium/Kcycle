from django.db import models
from django.contrib.auth.models import User


class CycleMenstruel(models.Model):
    user = models.ForeignKey(User, verbose_name="Utilisateur", on_delete=models.CASCADE, related_name='cycles')
    duree_cycle = models.PositiveIntegerField(verbose_name="Durée du cycle (en jours)")
    ovulation_date = models.DateField(verbose_name="Date d'ovulation", null=True, blank=True)
    commentaire = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Cycle {self.id} - {self.user}"


class Menstruation(models.Model):
    cycle = models.ForeignKey(CycleMenstruel, verbose_name="Cycle", on_delete=models.CASCADE, related_name='menstruations')
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)
    duree_periode_regles = models.PositiveIntegerField(null=True, blank=True, min_value=3, max_value=9)
    estimation_prochaine_menstruation = models.DateField(null=True, blank=True)
    symptomes = models.ManyToManyField('Symptome', through='RessentirSymptome', blank=True)

    def __str__(self):
        return f"Menstruation {self.id} - Cycle {self.cycle_id}"


class Symptome(models.Model):
    nom = models.CharField(max_length=100)
    categorie = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nom


class RessentirSymptome(models.Model):
    menstruation = models.ForeignKey(Menstruation, on_delete=models.CASCADE)
    symptome = models.ForeignKey(Symptome, on_delete=models.CASCADE)
    intensite = models.PositiveSmallIntegerField(default=1)
    
    class Meta:
     unique_together = ('menstruation', 'symptome')
     
    def __str__(self):
        return f"RessentirSymptome {self.id} - Menstruation {self.menstruation.id} - Symptome {self.symptome.id}"