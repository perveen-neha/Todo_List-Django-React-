from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers

# from rest_framework.decorators import api_view
from rest_framework.decorators import api_view

from rest_framework.response import Response

from .serializers import TaskSerialzer

from .models import Task

# Create your views here.
@api_view(['GET'])
def apiOverviewss(request):
    api_urls = {
        'List':'/task-List/',
        'Detail View':'/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def TaskList(request):
    task=Task.objects.all()
    serializer = TaskSerialzer(task, many='True')
    return Response(serializer.data)


@api_view(['GET'])
def TaskDetail(request,pk):
    task=Task.objects.all(id=pk)
    serializer = TaskSerialzer(task, many='False')
    return Response(serializer.data)



@api_view(['POST'])
def TaskCreate(request):
    
    serializer = TaskSerialzer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def TaskUpdate(request,pk):
    task=Task.objects.get(id=pk)
    serializer = TaskSerialzer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def TaskDelete(request,pk):
    task=Task.objects.get(id=pk)
    task.delete()

    return Response()

    