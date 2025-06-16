from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import URL
from .serializers import URLSerializer
from .utils import generate_short_url

class ShortenURL(APIView):
    def post(self, request):
        serializer = URLSerializer(data=request.data)
        if serializer.is_valid():
            short_url = generate_short_url()
            while URL.objects.filter(short_url=short_url).exists():
                short_url = generate_short_url()
            serializer.save(short_url=short_url)
            return Response({'original_url': serializer.data['original_url'], 'short_url': f"http://localhost:8000/shrt/{short_url}"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExpandURL(APIView):
    def get(self, request, short_url):
        url = get_object_or_404(URL, short_url=short_url)
        return Response({'original_url': url.original_url}, status=status.HTTP_200_OK)
