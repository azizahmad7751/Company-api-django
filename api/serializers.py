from rest_framework import serializers
from api.models import Company, Employee

# create serializers here to convert models to json

class CompanySerializer(serializers.HyperlinkedModelSerializer):
	company_id = serializers.ReadOnlyField()
	class Meta:
		#Meta class used that we can explain what calss we use...
		model=Company
		# fields used which field of Company model
		#To access all fields we use __all__.
		fields="__all__"


# create employee serializers here to convert models to json
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
	id = serializers.ReadOnlyField()

	class Meta:
		model = Employee
		fields ="__all__"
			