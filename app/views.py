from django.shortcuts import render
from django.core.paginator import Paginator
from .models import MyModel

def home(request):
    return render(request, 'home.html')

def show_all_records(request):
    all_records = MyModel.objects.all()
    paginator = Paginator(all_records, 10)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'all_records.html', {'page_obj': page_obj})