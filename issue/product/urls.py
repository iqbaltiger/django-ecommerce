from django.urls import path

from .import views

from django.conf import settings
from django.conf.urls.static import static

from .views import *
from django.views.generic.base import TemplateView


urlpatterns = [
    path('categorylist/', views.category_list, name='category_list'),
    path('category/', views.saveCategory, name='category'),
    path("editcategory/<int:pk>", views.editCategory, name="editcategory"),
    path("deletecategory/<int:pk>", views.deleteCategory, name="deletecategory"),
    ###Brand###
    path('brand/', BrandEntry.as_view(), name="brand"),
    path('brandlist/', BrandList.as_view(), name="brandlist"),
    path('brandupdate/<int:pk>', BrandUpdate.as_view(), name="brandupdate"),
    path('branddelete/<int:pk>', BrandDelete.as_view(), name="Branddelete"),
    path('dashboard/', Dashboard.as_view(), name="dashboard"),

    # variant

    path('variant/', VariantEntry.as_view(), name="variant"),
    path('variantlist/', VariantList.as_view(), name="variantlist"),
    path('variantupdate/<int:pk>', VariantUpdate.as_view(), name="variantupdate"),
    path('variantdelete/<int:pk>', VariantDelete.as_view(), name="variantdelete"),

    # unit
    path('unit/', UnitEntry.as_view(), name="unit"),
    path('unitlist/', UnitList.as_view(), name="unitlist"),
    path('unitupdate/<int:pk>', UnitUpdate.as_view(), name="unitupdate"),
    path('unitdelete/<int:pk>', UnitDelete.as_view(), name="unitdelete"),


    # currency
    path('currency/', CurrencyEntry.as_view(), name="currency"),
    path('currencylist/', CurrencyList.as_view(), name="currencylist"),
    path('currencyupdate/<int:pk>',
         CurrencyUpdate.as_view(), name="currencyupdate"),
    path('currencydelete/<int:pk>',
         CurrencyDelete.as_view(), name="currencydelete"),

    # Supplier
    path('supplier/', SupplierEntry.as_view(), name="supplier"),
    path('supplierlist/', SupplierList.as_view(), name="supplierlist"),
    path('supplierupdate/<int:pk>',
         SupplierUpdate.as_view(), name="supplierupdate"),
    path('supplierdelete/<int:pk>',
         SupplierDelete.as_view(), name="supplierdelete"),

    # product

    path('product/', ProductEntry.as_view(), name="productentry"),
    path('productlist/', ProductList.as_view(), name="productlist"),
    path('productupdate/<int:pk>',
         ProductUpdate.as_view(), name="productupdate"),
    path('productdelete/<int:pk>',
         ProductDelete.as_view(), name="productdelete"),

    #category frontend
    path('productdetails/<int:pk>',ProductDetails.as_view(),name="productdetails"),
    path('categorydetails/<int:pk>',CategoryDetails.as_view(),name="categorydetails"),
    path('brandbasedproduct/', views.load_category_based_product,name="brandbasedproduct"),
    path('sortingproduct/', views.load_sorting_based_product,
         name="sortingproduct"),
    
    #Cart

    path('cartdetails/<int:pk>',
         CartDetails.as_view(), name="cartdetails"),

    path('addToCart/', views.addToCart, name="addToCart"),
    path('cart/',CartList.as_view(),name="cartlist"),

    #Checkout


    path('checkout/',Checkout.as_view(),name="checkout")
         
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
