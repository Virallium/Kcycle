from rest_framework import serializers

from .models import Programme, Partenaires, Sponsorisation

class ProgrammeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programme
        fields = ('id', 'nom', 'description')
        read_only_fields = fields


class PartenairesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partenaires
        fields = ('id', 'Nom_structure', 'type_structure', 'email', 'contact', 'user')
        read_only_fields = ('id', 'user')


class SponsorisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsorisation
        fields = ('id', 'date_debut', 'date_fin', 'partenaire', 'programme')
        read_only_fields = ('id',)

    def validate_partenaire(self, partenaire):
        request = self.context.get('request')
        if request and partenaire.user_id != request.user.pk:
            raise serializers.ValidationError(
                "Ce partenaire n'appartient pas à votre compte."
            )
        return partenaire
