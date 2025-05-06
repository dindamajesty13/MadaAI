from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from myapi.chat.views import chat_generate
from myapi.product.views import get_products, create_product, product_detail
from myapi.user.views import get_user_data

urlpatterns = [
    path('products/', get_products, name='get_products'),
    path('products/create/', create_product, name='create_product'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("user/", get_user_data, name="get_user_data"),
    path('chat/generate/', chat_generate, name='chat_generate'),
]
