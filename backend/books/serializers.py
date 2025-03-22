from rest_framework import serializers
from .models import Book, SwapRequest

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'description', 'credit', 'price', 'image', 'owner']
        extra_kwargs = {
            'owner': {'read_only': True},
            'image': {'required': True}
        }

class SwapRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = SwapRequest
        fields = '__all__'
        read_only_fields = ('requester', 'created_at')