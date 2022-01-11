
from django.shortcuts import render, get_object_or_404
 
from .models import Flat, FlatImage
 
def flat_view(request):
    flats = Flat.objects.all()
    return render(request, 'nilay/post_list.html', {'flats':flats})

def detail_view(request, id):
    flat = get_object_or_404(Flat, id=id)
    photos = FlatImage.objects.filter(property=flat)
    return render(request, 'nilay/detail.html', {
        'flat':flat,
        'photos':photos
    })