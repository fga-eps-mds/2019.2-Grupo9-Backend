from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UsuarioAluno, Registration
from .serializers import UsuarioAlunoSerializer, RegistrationSerializer
from rest_framework import status

@api_view(['POST'])
def cadastrar_aluno(request):
	serializer = UsuarioAlunoSerializer(data = request.data)
	if serializer.is_valid():
		registro = Registration.objects.filter(matricula=serializer.data["matricula_aluno"]).first()
		if (registro):
			aluno = UsuarioAlunoSerializer.create(serializer, request.data)
			return Response ({"Usuario cadastrado com sucesso!"})
		else:
			return Response ({"Não foi possível encontrar um aluno com esta matricula na disciplina, tente novamente!"})		
	else:
		return Response({"Dados incorretos! Tente novamente"})

class MultipleRegistrationsViewSet(generics.ListCreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

    def create(self, request, *args, **kwargs):
        data = request.data.get("items") if 'items' in request.data else request.data
        many_data = isinstance(data, list)
        serializer = self.get_serializer(data=data, many=many_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)