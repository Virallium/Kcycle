from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Partenaires(models.Model):
    types_choices=(
        ('ONG','ONG'),
        ('ASBL','ASBL')
    )
    Nom_structure=models.CharField(max_length=100, verbose_name='Nom de la structure')
    type_structure=models.CharField(max_length=100, verbose_name='type de structure', choices=types_choices)
    email = models.EmailField(max_length=200, verbose_name="Email du partenaire")
    contact = models.CharField(max_length=20, verbose_name="Contact partenaire")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Partenaire {self.id} - {self.Nom_structure} - {self.type_structure} "
    
class Programme(models.Model):
    nom=models.CharField(max_length=100, verbose_name="nom programme")
    description = models.TextField()
    
    def __str__(self):
        return f"Programme {self.id} - {self.nom}"
   
class Sponsorisation(models.Model):    
    date_debut = models.DateField(default=timezone.localdate)
    date_fin= models.DateField(auto_now=False, auto_now_add=False)
    partenaire=models.ForeignKey(Partenaires, on_delete=models.CASCADE)
    programme=models.ForeignKey(Programme,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Sponsorisation - {self.id} - {self.partenaire} -{self.programme}"
