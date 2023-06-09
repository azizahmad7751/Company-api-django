from django.db import models

# Create your models here.

# creating company Model.

class Company(models.Model):
	company_id= models.AutoField(primary_key=True)
	name=models.CharField(max_length=50)
	location=models.CharField(max_length=50)
	about=models.TextField()
	type=models.CharField(max_length=100, choices=
		(('IT','IT'),
			('Non IT','Non IT'),
			('Mobile Phones','Mobile Phones')
			)) 
	added_date=models.DateTimeField(auto_now=True)
	active=models.BooleanField(default=True)


#Creating Employee class model.

class Employee(models.Model):
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=50)
	address = models.CharField(max_length=200)
	phone = models.CharField(max_length=10)
	about = models.CharField(max_length=50, choices=(
		('Manager','manager'),
		('Software Engineer','sd'),	
		('Prject Leader','pl')		
		))

    #Making foreignKey from company class primary key (id). 
    #Actually this is for the purpose to find which eployee has a relation with which company  
	#Creating one to many relation
	Company=models.ForeignKey(Company, on_delete=models.CASCADE)