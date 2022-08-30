from .models import Listing
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from listings.serializers import ListingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

class ListApiView(APIView):
    #permission_classes=[IsAuthenticated]

    create_serializer = ListingSerializer

    listings = Listing.objects.all()

    def get(self, id=False):

        if id:

            listing = self.listings.filter(id=id)
            
            if listing.exists():

                serializer = self.create_serializer(listing.first())

                print(serializer.data)

                return Response(serializer.data, status=status.HTTP_200_OK)

            else:

                return Response({"Error": "Page not found"}, status=status.HTTP_404_NOT_FOUND)
        else:

            serializer = self.create_serializer(self.listings.all(), many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        serializer = self.create_serializer(data = request.data)
        
        if serializer.is_valid(): 
            
                serializer.save()

                return Response(serializer.data, status=status.HTTP_200_OK)
        else:

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
#@permission_classes([IsAuthenticated])
def update_listing(request, id):
    listing = Listing.objects.get(id=id)
    
    serializer = ListingSerializer(instance=listing, data=request.data)

    if serializer.is_valid():

        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    else:

        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
#@permission_classes([IsAuthenticated])
def delete_listing(request, id):

    listing = Listing.objects.get(id=id)

    listing.delete()

    return Response(status=status.HTTP_202_ACCEPTED)