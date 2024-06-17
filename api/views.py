from django.shortcuts import render
from rest_framework.response import Response
from api.models import Customer, Work
from api.serializers import CustomerSerializer, WorkSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

class CustomerListCreateView(ListCreateAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

class CustomerRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class WorkCreateView(CreateAPIView):

    permission_classes=[permissions.IsAuthenticated]

    authentication_classes=[JWTAuthentication]

    serializer_class=WorkSerializer

    queryset=Work.objects.all()


    def perform_create(self, serializer):

        id=self.kwargs.get("pk")

        instance=Customer.objects.get(id=id)

        serializer.save(customer_object=instance)


