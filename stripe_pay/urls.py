from django.urls import path
from stripe_pay.views import get_stripe_session_id, get_item_html
from stripe_pay.apps import StripePayConfig

app_name = StripePayConfig.name

urlpatterns = [
    path('buy/<int:item_id>/', get_stripe_session_id, name='get_stripe_session_id'),
    path('item/<int:item_id>/', get_item_html, name='get_item_html'),
]
