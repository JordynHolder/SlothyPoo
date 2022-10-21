from django.shortcuts import render
from SiteManager.models import Image, TAG_CHOICES

# Create your views here.


def Gallery(request):
    if request.method == 'POST':
        print(request.POST)
        admin_obj = Image.objects.filter(tags=request.POST.get('tags'))
    else:
        admin_obj = Image.objects.all()
    
    tag_obj = TAG_CHOICES
    return render(request, "Gallery.html", {'admin_obj': admin_obj, 'tag_obj': tag_obj})
