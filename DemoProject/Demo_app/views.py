from django.shortcuts import render
from django.views.generic import View

from models import Customer

class Index(View):

	def get(self,request):
		return render(request,'Demo_app/index.html')

	def post(self,request):
		name = request.POST['name']
		mail = request.POST['mail']
		c = Customer(name=name,email=mail)
		c.save()
		file="excel.xlsx"
		return render(request,'Demo_app/firstPage.html',locals())


