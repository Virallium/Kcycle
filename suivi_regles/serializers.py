from rest_framework import serializers

from .models import CycleMenstruel, Menstruation, RessentirSymptome, Symptome


class CycleMenstruelSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = CycleMenstruel
        fields = ('id', 'user', 'duree_cycle', 'ovulation_date', 'commentaire')
        read_only_fields = ('id',)


class RessentirSymptomeSerializer(serializers.ModelSerializer):
    symptome_nom = serializers.CharField(source='symptome.nom', read_only=True)

    class Meta:
        model = RessentirSymptome
        fields = ('id', 'menstruation', 'symptome', 'symptome_nom', 'intensite')
        read_only_fields = ('id', 'symptome_nom')

    def validate_menstruation(self, menstruation):
        request = self.context.get('request')
        if request and menstruation.cycle.user_id != request.user.pk:
            raise serializers.ValidationError(
                "Cette menstruation n'appartient pas à votre compte."
            )
        return menstruation


class MenstruationSerializer(serializers.ModelSerializer):
    symptomes = RessentirSymptomeSerializer(
        source='ressentirsymptome_set',
        many=True,
        read_only=True,
    )

    class Meta:
        model = Menstruation
        fields = (
            'id',
            'cycle',
            'date_debut',
            'date_fin',
            'estimation_prochaine_menstruation',
            'symptomes',
        )
        read_only_fields = ('id', 'symptomes')

    def validate_cycle(self, cycle):
        request = self.context.get('request')
        if request and cycle.user_id != request.user.pk:
            raise serializers.ValidationError(
                "Ce cycle n'appartient pas à votre compte."
            )
        return cycle


class SymptomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symptome
        fields = ('id', 'nom', 'categorie')
        read_only_fields = ('id',)