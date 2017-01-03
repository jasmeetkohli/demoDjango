from django.shortcuts import render

# Create your views here.


def Index(request):
	return render(request,'Demo_app/index.html')

def firstPage(request):
	file="excel.xlsx"
	return render(request,'Demo_app/firstPage.html',locals())