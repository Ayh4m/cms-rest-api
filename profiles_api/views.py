from rest_framework.views import APIView
from rest_framework.response import Response


class APIViewFeatures(APIView):
    """APIView Features"""

    def get(self, request, format=None):
        """Return a list of APIView features"""
        features = [
            "Uses HTTP methods as function (get, post, patch, put, delete)",
            "Is similar to traditional django view",
            "Give you the most control over your application logic",
            "Is mapped manually to URLs"
        ]
        return Response({'message': 'APIView features', 'features': features})
