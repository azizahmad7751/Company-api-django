from django.http import HttpResponse, JsonResponse

def home_page(request):
	print("home page requested!!!");

	books= [

		'ALi',
		'Ahmad',
		'Khan'
	]

	return JsonResponse(books, safe=False)