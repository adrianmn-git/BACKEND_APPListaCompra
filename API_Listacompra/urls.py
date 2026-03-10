from django.contrib import admin
from django.urls import re_path
from ListaCompra import views


urlpatterns = [

    re_path(r'^admin/', admin.site.urls),

    # =========================
    # SHOPPING LISTS
    re_path(r'^lists$', views.GetListsView, name="GetListsView"),
    re_path(r'^list/(?P<list_id>\d+)$', views.GetListView, name="GetListView"),
    re_path(r'^lists/create$', views.CreateListView, name="CreateListView"),
    re_path(r'^lists/(?P<list_id>\d+)/complete$', views.CompleteListView, name="CompleteListView"),
    re_path(r'^lists/(?P<list_id>\d+)/items$', views.GetListItemsView, name="GetListItemsView"),

    # =========================
    # PRODUCTS
    re_path(r'^products$', views.GetProductsView, name="GetProductsView"),
    re_path(r'^products/create$', views.CreateProductView, name="CreateProductView"),

    # =========================
    # SHOPPING LIST ITEMS
    re_path(r'^items/add$', views.AddProductToListView, name="AddProductToListView"),
    re_path(r'^items/(?P<item_id>\d+)/update$', views.UpdateListItemView, name="UpdateListItemView"),
    re_path(r'^items/(?P<item_id>\d+)/delete$', views.DeleteListItemView, name="DeleteListItemView"),
]