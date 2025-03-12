# dummy data

from rest_framework.decorators import api_view
from rest_framework.response import Response

books_data = [
    {
        'id': 1,
        'title': 'Sample Book 1',
        'author': 'Author 1',
        'credit': 5
    },
    {
        'id': 2,
        'title': 'Sample Book 2',
        'author': 'Author 2',
        'credit': 7
    }
]

@api_view(['GET'])
def book_list(request):
    return Response(books_data)