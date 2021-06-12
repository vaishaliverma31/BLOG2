from django.db import models
from django.db.models import fields
from .models import Blogmodel
from rest_framework import serializers

class Blogserializer(serializers.ModelSerializer):
    class Meta:
        model=Blogmodel
        fields='__all__'