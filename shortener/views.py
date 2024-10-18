from django.shortcuts import render, redirect, get_object_or_404
import string
import random
from .forms import URLForm
from .models import MyURL
from django.http import HttpResponseRedirect


# Create your views here.
def generateshortcut_url():
    length = 6
    characters = string.ascii_letters + string.digits
    # Generate a list of characters and then join them into a single string
    short_url = ''.join(random.choices(characters, k=length))
    return short_url


def home(request):
    form = URLForm()
    short_url = None
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['original_url']
            short_url = generateshortcut_url()
            # Save the URL
            url_instance = MyURL(original_url=original_url, short_url=short_url)
            url_instance.save()
            return render(request, 'shortener/home.html', {
                'form': form,
                'short_url': short_url
            })
    
    # For GET requests or when form is invalid, render the form again
    return render(request, 'shortener/home.html', {'form': form, 'short_url': short_url})
    
def redirect_site(request, shorturl):
    url_instance = get_object_or_404(MyURL, short_url=shorturl)
    return HttpResponseRedirect(url_instance.original_url)
