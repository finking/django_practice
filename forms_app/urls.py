from django.urls import path
from .views import contact_send

# path('form/', include('forms_app.urls')),
urlpatterns = [
    # path('user/<str:username>/', UserDiscussionListView.as_view(), name='discussion-list'),
    # path('new/', DiscussionCreateView.as_view(), name='discussion-create'),
    # path('detail/<int:pk>/<slug:slug>', DiscussionDetailView.as_view(), name='discussion-detail'),
    # path('create/', discussion_created, name='create')
    path('contact/', contact_send, name='contact'),

]