from rest_framework import serializers

from .models import Categorie, Consultation, ContenuEducatif

class ContenuEducatifSerializer(serializers.ModelSerializer):
    categorie_nom = serializers.CharField(source='categorie.name', read_only=True)

    class Meta:
        model = ContenuEducatif
        fields = (
            'id', 'title', 'description', 'video', 'photo', 'created_at',
            'updated_at', 'categorie', 'categorie_nom',
        )
        read_only_fields = ('id', 'created_at', 'updated_at', 'categorie_nom')


class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ('id', 'name')
        read_only_fields = ('id',)


class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = ('id', 'user', 'contenu_educ', 'date_consultation', 'progress')
        read_only_fields = ('id', 'user', 'date_consultation')

    def validate_progress(self, progress):
        if not 0 <= progress <= 100:
            raise serializers.ValidationError(
                "La progression doit être comprise entre 0 et 100."
            )
        return progress