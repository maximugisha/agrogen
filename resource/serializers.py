from rest_framework import serializers
from .models import Post, Attachment


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ['id', 'file']
        read_only_fields = ['id',]

class PostSerializer(serializers.ModelSerializer):
    attachments = serializers.ListField(
        child=serializers.FileField(), required=False, write_only=True
    )
    categories = serializers.ListField(child=serializers.IntegerField(), required=False)

    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        categories_data = validated_data.pop('categories', [])
        attachments_data = validated_data.pop('attachments', [])
        post = Post.objects.create(**validated_data)
        
        if categories_data:
            post.categories.set(categories_data)  # Use .set() to assign categories

        for attachment_file in attachments_data:
            attachment = Attachment.objects.create(file=attachment_file)
            post.attachments.add(attachment)

        return post
    
    def to_representation(self, instance):
        """Custom representation to return related fields properly."""
        representation = super().to_representation(instance)

        # Replace the write-only attachments field with a proper serialized output
        representation['attachments'] = AttachmentSerializer(instance.attachments.all(), many=True).data

        # Replace categories with their actual data
        representation['categories'] = [category.pk for category in instance.categories.all()]

        return representation
