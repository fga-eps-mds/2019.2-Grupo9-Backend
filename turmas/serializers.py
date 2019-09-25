from .models import Turma
from rest_framework import serializers

class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = ['id_turma', 'nome_turma', 'ano_turma', 'periodo_turma']
