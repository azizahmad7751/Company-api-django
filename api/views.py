from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company, Employee
from api.serializers import CompanySerializer,EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.

# we will not used function based views. Rest framework provide us modelViewSet class which give us all the methods

class CompanyViewSet(viewsets.ModelViewSet):  
	#access all objects of Company model
	queryset=Company.objects.all()

	#Then convert that model data to json formate
	serializer_class=CompanySerializer
	
	#creating function for to get companies/{companyId}/employees means to get employees of specific company
	#@action is a decorator used to access primary key by detail=True
	@action(detail=True, methods=['get']) 
	def employees(self, request, pk=None):
		try:
	     	#to get primary key of a company
			company=Company.objects.get(pk=pk)
			#print(company)
			#get an employees which has a specific PK
			emps=Employee.objects.filter(Company=company)
			print(emps)
			#convert object to json and then send for request
			emps_serializer=EmployeeSerializer(emps, many=True, context={'request':request})
			return Response(emps_serializer.data)

		except Exception as e:
			print(e);
			return Response({
				'message':'Company might not exist '
				})
			



class EmployeeViewSet(viewsets.ModelViewSet):
	queryset= Employee.objects.all()
	serializer_class=EmployeeSerializer

		