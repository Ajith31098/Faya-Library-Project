from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'description', 'book_pages', 'author')

    def validate_title(self, value):
        if Book.objects.filter(title=value).exists():
            raise serializers.ValidationError('this title exist')
        return value
