from django.urls import path

from .views import RegisterView, AdsGeneralView, CreateAdView, CreateCommentView, ListCommentsView, \
    UpdateAdView, DeleteAdView, RetrieveAdView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('ads/list/', AdsGeneralView.as_view(), name='ads'),
    path('ads/<int:ad_id>/', RetrieveAdView.as_view(), name='retrieve_add'),
    path('ads/create/', CreateAdView.as_view(), name='create_ad'),
    path('ads/<int:ad_id>/update/', UpdateAdView.as_view(), name='update_ad'),
    path('ads/<int:ad_id>/delete/', DeleteAdView.as_view(), name='delete_ad'),
    path('ads/<int:ad_id>/comments/list/', ListCommentsView.as_view(), name='list_ad_comments'),
    path('ads/<int:ad_id>/comments/create/', CreateCommentView.as_view(), name='create_comment'),
    
]