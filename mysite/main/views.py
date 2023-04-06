from django.shortcuts import render, redirect
from .models import Shoes
# Create your views here.
def index(request):
    if request.method == 'POST':
        new_price = request.POST.get('change_price')
        item_id = request.POST.get('id')
        item_id_price = request.POST.get('id_price')
        item_id_image = request.POST.get('id_image')
        change_image = request.FILES.get('change_image')
        if new_price and item_id_price:
            try:
                my_item = Shoes.objects.get(id=int(item_id_price))
                my_item.price = int(new_price)
                my_item.save()
            except:
                return redirect('index')
        elif item_id:
            try:
                my_item = Shoes.objects.get(id=int(item_id))
                my_item.delete()
            except:
                return redirect('index')
        elif item_id_image and change_image:
            try:
                my_item = Shoes.objects.get(id=int(item_id_image))
                my_item.img = f'media\images\{change_image}'
                my_item.save()
            except:
                return redirect('index')
    shoes_list = Shoes.objects.all()
    return render(request, 'main/index.html', context={
        'shoes_list':shoes_list
    })