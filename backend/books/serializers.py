from rest_framework import serializers
from .models import Book, SwapRequest

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = ('owner', 'created_at')

class SwapRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = SwapRequest
        fields = '__all__'
        read_only_fields = ('requester', 'created_at')