from rest_framework import serializers
from hotspots.models import TreeNode

class TreeNodeSerializer(serializers.ModelSerializer) :
	
	class Meta :
		model = TreeNode
		fields = ('id', 'path')

	# id = serializers.IntegerField(read_only=True)
	# path = serializers.CharField(required=True, allow_blank=False, max_length=1000)

	# def create(self, validated_data) :
	# 	return TreeNode.objects.create(**validated_data)

	# def update(self, instance, validated_data) :
	# 	instance.path = validated_data.get('path', instance.path)
	# 	instance.save()
	# 	return instance
