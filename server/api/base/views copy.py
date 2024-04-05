from django.shortcuts import render, redirect
from django.http import JsonResponse

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Advocate, Usertype, User, File, Folder, Subscription, Plan
from .serializers import AdvocateSerializer, CompanySerializer, SubscriptionSerializer, FileSerializer, UsertypeSerializer, PlanSerializer, FolderSerializer
from django.db.models import Q


@api_view(['GET'])
def endoints(request):
    data = ['/advocates', 'advocates/:username']
    return Response(data)


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def advocate_list(request):
    # http://127.0.0.1:8000/advocates/?query=bnkhata
    if request.method == 'GET':
        query = request.GET.get('query')
        if query == None:
            query = ''

        advocates = Advocate.objects.filter(
            Q(username__icontains=query) | Q(bio__icontains=query))
        serializer = AdvocateSerializer(advocates, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        advocate = Advocate.objects.create(
            username=request.data['username'],
            bio=request.data['bio'],
        )
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)


# @api_view(['GET', 'POST'])
# def companies_list(request):
#     if request.method == 'GET':
#         companies = Company.objects.all()
#         serializer = CompanySerializer(companies, many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         company = Company.objects.create(
#             name=request.data['name'],
#             bio=request.data['bio'],
#         )
#         serializer = CompanySerializer(company, many=False)
#         return Response(serializer.data)

# @api_view(['GET','PUT','DELETE'])
# def advocate_detail(request, username):

#     advocate = Advocate.objects.get(username=username)
#     if request.method == "GET":
#         serializer = AdvocateSerializer(advocate, many=False)
#         return Response(serializer.data)

#     if request.method == "PUT":
#         advocate.username = request.data['username']
#         advocate.bio = request.data['bio']
#         advocate.save()
#         serializer = AdvocateSerializer(advocate, many=False)
#         return Response(serializer.data)

#     if request.method == "DELETE":
#         advocate.delete()
#         return Response('User Deleted')

class File(APIView):
    def get_object(self, file_id):
        try:
            return File.objects.get(file_id=file_id)
        except File.DoesNotExist:
            raise Response("File does not exist")
        
    def get(self, request, file_id=None):
        if file_id is not None:
            file = self.get_object(file_id)
            serializer = FileSerializer(file, many=False)
            return Response(serializer.data)
        else:
            files = File.objects.all()
            serializer = FileSerializer(files, many=True)
            return Response(serializer.data)

    def put(self, request, file_id):
        file = self.get_objects(file_id)
        file.title = request.data['title']
        file.name = request.data['name']
        file.path = request.data['path']
        file.folder_id = request.data['folder_id']
        file.user_id = request.data['user_id']
        file.save()
        serializer = FileSerializer(file, many=False)
        return Response(serializer.data)

    def delete(self, request, file_id):
        file = self.get_objects(file_id)
        file.deleted = 0
        file.save()
        return Response("File was Removed")


class Subscription(APIView):
    def get_object(self, subscription_id):
        try:
            return Subscription.objects.get(subscription_id=subscription_id)
        except Subscription.DoesNotExist:
            raise Response("subscription does not exist")

    def get(self, request, subscription_id):
        subscription = self.get_objects(subscription_id)
        serializer = SubscriptionSerializer(subscription, many=False)
        return Response(serializer.data)

    def put(self, request, subscription_id):
        subscription = self.get_objects(subscription_id)
        subscription.title = request.data['title']
        subscription.status = request.data['status']
        subscription.start_date = request.data['start_date']
        subscription.end_date = request.data['end_date']
        subscription.user_id = request.data['user_id']
        subscription.save()
        serializer = SubscriptionSerializer(subscription, many=False)
        return Response(serializer.data)

    def delete(self, request, subscription_id):
        subscription = self.get_objects(subscription_id)
        subscription.delete()
        return Response("Subscription was Disabled")


class Folder(APIView):
    def get_object(self, folder_id):
        try:
            return Folder.objects.get(folder_id=folder_id)
        except Folder.DoesNotExist:
            raise Response("folder does not exist")

    def get(self, request, folder_id):
        folder = self.get_objects(folder_id)
        serializer = FolderSerializer(folder, many=False)
        return Response(serializer.data)

    def put(self, request, folder_id):
        folder = self.get_objects(folder_id)
        folder.folder_name = request.data['folder_name']
        folder.user_id = request.data['user_id']
        folder.save()
        serializer = FolderSerializer(folder, many=False)
        return Response(serializer.data)

    def delete(self, request, folder_id):
        folder = self.get_objects(folder_id)
        folder.deleted = 0
        folder.save()
        return Response("Folder was Disabled")


class Usertype(APIView):
    def get_object(self, usertype_id):
        try:
            return Usertype.objects.get(usertype_id=usertype_id)
        except Usertype.DoesNotExist:
            raise Response("Usertype does not exist")

    def get(self, request, usertype_id):
        usertype = self.get_objects(usertype_id)
        serializer = UsertypeSerializer(usertype, many=False)
        return Response(serializer.data)

    def put(self, request, usertype_id):
        usertype = self.get_objects(usertype_id)
        usertype.usertype_name = request.data['usertype_name']
        usertype.save()
        serializer = UsertypeSerializer(usertype, many=False)
        return Response(serializer.data)

    def delete(self, request, usertype_id):
        usertype = self.get_objects(usertype_id)
        usertype.deleted = 0
        usertype.save()
        return Response("Usertype was Disabled")


class Plan(APIView):
    def get_object(self, plan_id):
        try:
            return Plan.objects.get(plan_id=plan_id)
        except Plan.DoesNotExist:
            raise Response("Plan does not exist")

    def get(self, request, plan_id):
        plan = self.get_objects(plan_id)
        serializer = PlanSerializer(plan, many=False)
        return Response(serializer.data)

    def put(self, request, plan_id):
        plan = self.get_objects(plan_id)
        plan.title = request.data['title']
        plan.cost = request.data['cost']
        plan.duration = request.data['duration']
        plan.save()
        serializer = PlanSerializer(plan, many=False)
        return Response(serializer.data)

    def delete(self, request, plan_id):
        plan = self.get_objects(plan_id)
        plan.deleted = 0
        plan.save()
        return Response("Plan was Disabled")


# class AdvocateDetail(APIView):
#     def get_object(self, username):
#         try:
#             return Advocate.objects.get(username=username)
#         except Advocate.DoesNotExist:
#             raise Response("Advocate does not exist")

#     def get(self, request, username):
#         advocate = self.get_objects(username)
#         serializer = AdvocateSerializer(advocate, many=False)
#         return Response(serializer.data)

#     def put(self, request, username):
#         advocate = self.get_objects(username)
#         advocate.username = request.data['username']
#         advocate.bio = request.data['bio']
#         advocate.save()
#         serializer = AdvocateSerializer(advocate, many=False)
#         return Response(serializer.data)

#     def delete(self, request, username):
#         advocate = self.get_objects(username)
#         advocate.delete()
#         return Response("User was Deleted")
