from rest_framework.views import APIView
from rest_framework.response import Response 


class HelloApiView(APIView):
    """Test API views"""

    def get(self, request, format="None"):
        """Returns a list of API views feature"""
        an_apiview = [
            "Uses HTTP methods as function( get, post,patch,put,delete)",
            "Is similar to a traditional django view",
            "Gives you the most control over your application logic",
            "Is mapped manually to URLs"
        ]
        return Response({'message':'Hello', 'an_api_view':an_apiview})