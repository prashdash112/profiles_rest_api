from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from profiles_api import serializers, models
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

class HelloApiView(APIView):
    """Test API views"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format="None"):
        """Returns a list of API views feature"""
        an_apiview = [
            "Uses HTTP methods as function( get, post,patch,put,delete)",
            "Is similar to a traditional django view",
            "Gives you the most control over your application logic",
            "Is mapped manually to URLs"
        ]
        return Response({'message':'Hello', 'an_api_view':an_apiview})
    
    def post(self, request):
        """Create a Hello message with the posted name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({"message:",message})
        else: 
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST
                            )
        
    def put(self,requests, pk=None):
        """handle updating an object"""
        return Response({'method':'PUT'})
    
    def patch(self, requests, pk=None):
        """handles partial update"""
        return Response({'method':'PATCH'})
    
    def delete(self, requests, pk=None): 
        """Delete objects in DB"""
        return Response({'method':'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test API Viewsets"""
    
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a Hello message"""

        a_viewset = [
            'uses actions (list, create, retrieve, update, delete, partial update )'
        ]

        return Response({"message":"hello", "a_viewset":a_viewset})
    
    def create(self, request): 
        """Create an new name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({"message:",message})
        else: 
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST
                            ) 

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'HTTP_method':'GET'})
    
    def update(self, request, pk=None): 
        """Updates an existing object"""
        return Response({"HTTP_method":"PUT"})

    def partial_update(self, request, pk=None): 
        """Partial updates the object"""
        return Response({"HTTP_Method":"PATCH"})
    
    def destroy(self, request, pk=None): 
        """Handle removing an object"""
        return Response({"HTTP_Method":"DELETE"})
    
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')
    
class UserLoginApiView(ObtainAuthToken):
    """Handle creating User authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES 
    