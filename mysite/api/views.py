from django.shortcuts import render
from rest_framework import generics, status  # Import generic view for CRUD
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import BlogPost
from .serializers import BlogPostSerializer

# Create your views here.


# Step 6) Create view that use the Model and the Serializer
# - Generic view that create a new blog post and get all the blog post that exist
class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()  # Give all the instances of the blogpost
    serializer_class = BlogPostSerializer  # The serializer that we want to use

    # Overwrite the view - add a delet route to the API view
    def delete(self, request, *args, **kwargs):
        BlogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()  # Give all the instances of the blogpost
    serializer_class = BlogPostSerializer  # The serializer that we want to use
    lookup_field = "pk"  # Primary Key - the ID of the blog post


class BlogPostList(APIView):
    def get(self, request):
        # Get the title from the query parameters (if none, default to empty string)
        title = request.query_params.get('title', "")

        if title:
            # Filter the queryset based on the title
            blog_posts = BlogPost.objects.filter(title__icontains=title)
        else:
            # If no title is provided, return all blog posts
            blog_posts = BlogPost.objects.all()

        serializer = BlogPostSerializer(blog_posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)