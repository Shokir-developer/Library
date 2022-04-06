from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializer
from my_app.models import Book


@api_view(['GET'])
def bookApi(request):
	books  = Book.objects.all()
	serializer = BookSerializer(books, many=True)

	return Response(serializer.data)




@api_view(['POST'])
def bookAdd(request):
	serializer = BookSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)