from django.urls import path
from . import views


# Step 7.2) Create a route to the view
urlpatterns = [
    # The trailing slash is important
    path('blogposts/', views.BlogPostListCreate.as_view(), name='blogpost-view-create'),
    path("blogposts/<int:pk>/", views.BlogPostRetrieveUpdateDestroy.as_view(), name="update"),
    path('blogposts/query/', views.BlogPostList.as_view(), name='query'),
]
