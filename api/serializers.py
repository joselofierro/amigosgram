from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.categorias.models import Categoria
from apps.preguntas.models import Pregunta


class PreguntaSerializer(ModelSerializer):
    class Meta:
        model = Pregunta
        fields = ['texto', 'fecha']


class CategoriaSerializer(ModelSerializer):
    preguntas = PreguntaSerializer(many=True)

    class Meta:
        model = Categoria
        fields = ['nombre', 'preguntas']

    def create(self, validated_data):
        preguntas_data = validated_data.pop('preguntas')
        try:
            name_c = validated_data.get('nombre')
            categoria = Categoria.objects.get(nombre=name_c)
            for pregunta in preguntas_data:
                Pregunta.objects.create(categoria=categoria, **pregunta)
        except Categoria.DoesNotExist:
            categoria = Categoria.objects.create(**validated_data)
            for pregunta in preguntas_data:
                Pregunta.objects.create(categoria=categoria, **pregunta)

        return categoria
