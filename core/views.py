from django.shortcuts import render

# Create your views here.

import requests


from .forms import SubmitEmbed
from .serializer import EmbedSerializer


def save_embed(request):

    if request.method == "POST":
        form = SubmitEmbed(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            r = requests.get('http://api.embed.ly/1/oembed?url=' + url)
            json = r.json()
            serializer = EmbedSerializer(data=json)
            if serializer.is_valid():
                embed = serializer.save()
                return render(request, 'embeds.html', {'embed': embed})
    else:
        form = SubmitEmbed()

    return render(request, 'index.html', {'form': form})