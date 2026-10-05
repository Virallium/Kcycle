from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Categorie(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class ContenuEducatif(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video=models.FileField(upload_to='contenus_educations_videos/', null=True, blank=True)
    photo=models.ImageField(upload_to='contenus_educations_photos/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='contenus_educations')

    def __str__(self):
        return self.title
    
    
class Consultation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='consultations')
    contenu_educ = models.ForeignKey(ContenuEducatif, on_delete=models.CASCADE, related_name='consultations')
    date_consultation = models.DateTimeField(auto_now_add=True)
    progress = models.FloatField(default=0.0)  # Progress percentage (0.0 to 100.0)

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=models.Q(progress__gte=0, progress__lte=100),
                name='consultation_progress_0_100',
            ),
        ]

    def __str__(self):
        return f"Consultation {self.id} - User: {self.user} - Contenu Educ: {self.contenu_educ}"

