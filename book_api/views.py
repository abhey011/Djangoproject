from django.shortcuts import render
from rest_framework.response import Response
from book_api.models import Book
from book_api.serializer import BookSerializer
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books , many = True)
    return Response(serializer.data)
    

@api_view(['POST'])
def book_create(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


@api_view(['GET','PUT','DELETE'])
def book(request,pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = BookSerializer(book) 
        return Response(serializer.data)

    if request.method == 'PUT':
        return Response(book,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    if request.method == 'DELETE':
        Book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)