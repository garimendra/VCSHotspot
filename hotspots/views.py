# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from hotspots.models import TreeNode
from hotspots.utils.connect import *
from django.http import HttpResponse, JsonResponse
import json


# def index(request):
# 	connectToPerforce()
# 	dirs, files = expand("//Lacerte/MainDev/CSharp_Extensions/")
# 	context = {
# 		'directories' : dirs,
# 		'files' : files
# 	}

# 	return render(request, 'hotspots/index.html', context);



def fetchChildren(request) :
	
	connectToPerforce()
	
	curDir = request.GET.get('curDir')
	
	score = 0

	if curDir[len(curDir)-1] != '/' :
		score = getScore(curDir)
		result = { 'score': score}
	else :
		dirs, files = expand(curDir)
		result = {'dirs' : dirs, 'files' : files }
	
	return JsonResponse(result)



























# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'treeNodes': reverse('treeNode-list', request=request, format=format)
#     })


# #mixins generic view classes

# @permission_classes((permissions.AllowAny,))

# class TreeNodeList(generics.ListCreateAPIView):
#     queryset = TreeNode.objects.all()
#     serializer_class = TreeNodeSerializer

# @permission_classes((permissions.AllowAny,))

# class TreeNodeDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = TreeNode.objects.all()
#     serializer_class = TreeNodeSerializer





















































# class TreeNodeList(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         treeNodes = TreeNode.objects.all()
#         serializer = TreeNodeSerializer(treeNodes, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = TreeNodeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# class TreeNodeList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = TreeNode.objects.all()
#     serializer_class = TreeNodeSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)



# class TreeNodeDetail(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, pk):
#         try:
#             return TreeNode.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         treeNode = self.get_object(pk)
#         serializer = TreeNodeSerializer(snippet)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         treeNode = self.get_object(pk)
#         serializer = TreeNodeSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         treeNode = self.get_object(pk)
#         treeNode.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class TreeNodeDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = TreeNode.objects.all()
#     serializer_class = TreeNodeSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# @api_view(['GET', 'POST'])

# def treeNode_list(request, format = None):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         treeNodes = TreeNode.objects.all()
#         serializer = TreeNodeSerializer(treeNodes, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = TreeNodeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes((permissions.AllowAny,))

# def treeNode_detail(request, pk, format = None):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         treeNode = TreeNode.objects.get(pk=pk)
#     except TreeNode.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = TreeNodeSerializer(treeNode)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = TreeNodeSerializer(treeNode, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         treeNode.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

