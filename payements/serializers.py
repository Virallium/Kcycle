from rest_framework import serializers

from .models import Abonnement, Payement


class AbonnementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abonnement
        fields = (
            'id',
            'formule_abonnement',
            'date_debut',
            'date_fin',
            'actif',
            'user',
        )
        read_only_fields = fields


class PayementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payement
        fields = (
            'id',
            'montant',
            'moyen_payement',
            'date_paye',
            'payement_statut',
            'abonnement',
        )
        read_only_fields = fields