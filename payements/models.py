from django.db import models
from django.contrib.auth.models import User

class Abonnement(models.Model):
    TYPE_CHOICES = (
        ('FREEMIUM', 'Freemium'),
        ('PREMIUM', 'Premium'),
        ('BUSINESS', 'Business'),
    )
    formule_abonnement = models.CharField(verbose_name='type_abonnement', max_length=20, choices=TYPE_CHOICES)
    date_debut = models.DateField(auto_now_add=True)
    date_fin = models.DateField(null=True, blank=True)
    actif = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='abonnements')

    def __str__(self):
        return f"Abonnement {self.id} - {self.formule_abonnement} - {self.date_debut} → {self.date_fin}"


class Payement(models.Model):
    STATUT_CHOICES = (
        ('Reussi', 'Reussi'),
        ('En attente', 'En attente'),
        ('Echoue', 'Echoue'),
    )
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    moyen_payement = models.CharField(verbose_name='moyen_payement', max_length=50)
    date_paye = models.DateField(null=True, blank=True)
    payement_statut = models.CharField(verbose_name="payement statut", max_length=20, choices=STATUT_CHOICES)
    abonnement = models.ForeignKey(Abonnement, on_delete=models.PROTECT, related_name='payements')

    def __str__(self):
        return f"Payement {self.id} - {self.montant} - {self.date_paye}"