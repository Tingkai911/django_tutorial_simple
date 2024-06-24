from rest_framework import serializers
from .models import BlogPost


# Step 5) Converts Model to JSON
class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', "published_date"]  # The fields that we want to be returned in the API
