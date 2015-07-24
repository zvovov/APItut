from django.shortcuts import render

# Create your views here.
from rest_framework import serializers
from .models import SavedEmbeds

class EmbedSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedEmbeds