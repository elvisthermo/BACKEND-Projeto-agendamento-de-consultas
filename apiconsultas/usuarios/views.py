from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Customer
from .serializers import *

...

@api_view(['GET', 'POST'])
def clientes_list(request):
    """
 List  customers, or create a new customer.
 """
    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        clientes = Clientes.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(usuarios, 10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = ClientesSerializer(data,context={'request': request} ,many=True)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()

        return Response({'data': serializer.data , 'count': paginator.count, 'numpages' : paginator.num_pages, 'nextlink': '/api/clientes/?page=' + str(nextPage), 'prevlink': '/api/clientes/?page=' + str(previousPage)})

    elif request.method == 'POST':
        serializer = ClientesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def clientes_detail(request, pk):
    """
 Retrieve, update or delete a customer by id/pk.
 """
    try:
        clientes = Clientes.objects.get(pk=pk)
    except Clientes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClientesSerializer(clientes,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ClientesSerializer(clientes, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        clientes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)