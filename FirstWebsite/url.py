from django.conf.urls import include, url
from django.contrib import admin
from FirstWebsite import views
admin.autodiscover()

urlpatterns = [
    url(r'^hello/', views.hello, name='home'),
    url(r'^$', views.article, name='articleId'),
    url(r'^merchant/$',views.merchant, name = 'merchant_display'),
    url(r'^merchant/(?P<user_id>[0-9]+)/$',views.merchant_info, name='merchant_info'),
    url(r'^merchantlist/$',views.Merchantlist.as_view(), name='merchant_api'),
    url(r'^merchantlist/(?P<mer_id>[0-9]+)/$',views.Merchantlist_1.as_view(), name='merchant_api_1'),
    url(r'^deallist/$', views.Deallist.as_view(), name='deal_api')
    ]