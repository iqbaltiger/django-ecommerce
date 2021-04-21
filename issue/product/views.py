from django.shortcuts import render, redirect
from .forms import categoryForm, supplierForm

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Category, Brand, Variant, Unit, Currency, Supplier, Product, Cart, User
from django.views.generic.base import TemplateView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.template.loader import render_to_string
from django.db.models import F


# Create your views here.


# Save Category Info
def saveCategory(request):
    form = categoryForm(request.POST or None, request.FILES)

    if request.method == 'POST':

        print("All Files", request.FILES)

        print("All Data", request.POST)

        if form.is_valid():
            form.save()

            return redirect('/product/categorylist/')

    return render(request, 'category.html', {'form': form})


# Edit category info based on requested id
def editCategory(request, pk):
    print("PK", pk)

    editedCategory = Category.objects.get(pk=pk)

    print(editedCategory)

    print("Post Data", request.POST)

    form = categoryForm(request.POST or None, instance=editedCategory)

    if request.method == "POST":
        form = categoryForm(request.POST or None, request.FILES, instance=editedCategory)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submission successful')

            return redirect('/product/categorylist/')
    return render(request, 'editCategory.html', {'form': form})


# Delete category

def deleteCategory(request, pk):
    deletedCategory = Category.objects.get(pk=pk)
    if deletedCategory:
        deletedCategory.delete()
        return redirect('/product/categorylist/')
    return redirect('/product/categorylist/')


def category_list(request):
    catList = Category.objects.all().order_by('-id')
    return render(request, 'catlist.html', {"catlist": catList})


###########Brand###################################
class BrandEntry(SuccessMessageMixin, CreateView):
    model = Brand
    template_name = 'product/brand_entry.html'
    fields = '__all__'
    success_url = "/product/brandlist/"
    success_message = "%(brand_name)s has been created successfully"


class BrandList(SuccessMessageMixin, ListView):
    model = Brand
    template_name = 'product/brand_list.html'
    context_object_name = 'brandlist'


class BrandUpdate(SuccessMessageMixin, UpdateView):
    model = Brand
    template_name = 'product/brand_update.html'
    fields = '__all__'
    success_url = "/product/brandlist/"
    success_message = "<b>%(brand_name)s</b> has been updated successfully"


class BrandDelete(SuccessMessageMixin, DeleteView):
    model = Brand
    success_url = "/product/brandlist/"
    success_message = "%(brand_name)s has been deleted successfully"


class Dashboard(TemplateView):
    template_name = 'product/main.html'


###Variant####

class VariantEntry(SuccessMessageMixin, CreateView):
    model = Variant
    template_name = 'product/variant_entry.html'
    fields = '__all__'
    success_url = "/product/variantlist/"
    success_message = "%(variant_name)s has been added successfully"


class VariantList(SuccessMessageMixin, ListView):
    model = Variant
    template_name = 'product/variant_list.html'
    context_object_name = 'variantlist'


class VariantUpdate(SuccessMessageMixin, UpdateView):
    model = Variant
    template_name = 'product/variant_update.html'
    fields = '__all__'
    success_url = "/product/variantlist/"
    success_message = "<b>%(variant_name)s</b> has been updated successfully"


class VariantDelete(SuccessMessageMixin, DeleteView):
    model = Variant
    success_url = "/product/variantlist/"
    success_message = "%(variant_name)s has been deleted successfully"


###Unit####


class UnitEntry(SuccessMessageMixin, CreateView):
    model = Unit
    template_name = 'product/unit_entry.html'
    fields = '__all__'
    success_url = "/product/unitlist/"
    success_message = "%(unit_name)s has been added successfully"


class UnitList(SuccessMessageMixin, ListView):
    model = Unit
    template_name = 'product/unit_list.html'
    context_object_name = 'unitlist'


class UnitUpdate(SuccessMessageMixin, UpdateView):
    model = Unit
    template_name = 'product/unit_update.html'
    fields = '__all__'
    success_url = "/product/unitlist/"
    success_message = "<b>%(unit_name)s</b> has been updated successfully"


class UnitDelete(SuccessMessageMixin, DeleteView):
    model = Unit
    success_url = "/product/unitlist/"
    success_message = "%(unit_name)s has been deleted successfully"


###Currency####


class CurrencyEntry(SuccessMessageMixin, CreateView):
    model = Currency
    template_name = 'product/currency_entry.html'
    fields = '__all__'
    success_url = "/product/currencylist/"
    success_message = "%(currency_name)s has been added successfully"


class CurrencyList(SuccessMessageMixin, ListView):
    model = Currency
    template_name = 'product/currency_list.html'
    context_object_name = 'currencylist'


class CurrencyUpdate(SuccessMessageMixin, UpdateView):
    model = Currency
    template_name = 'product/currency_update.html'
    fields = '__all__'
    success_url = "/product/currencylist/"
    success_message = "<b>%(currency_name)s</b> has been updated successfully"


class CurrencyDelete(SuccessMessageMixin, DeleteView):
    model = Currency
    success_url = "/product/currencylist/"
    success_message = "%(currency_name)s has been deleted successfully"


# Supplier


###Currency####

class SupplierEntry(SuccessMessageMixin, CreateView):
    model = Supplier
    form_class = supplierForm
    template_name = 'product/supplier/supplier_entry.html'
    # fields = '__all__'
    success_url = "/product/supplierlist/"
    success_message = "%(supplier_name)s has been added successfully"


class SupplierList(SuccessMessageMixin, ListView):
    model = Supplier
    template_name = 'product/supplier/supplier_list.html'
    context_object_name = 'supplierlist'


class SupplierUpdate(SuccessMessageMixin, UpdateView):
    model = Supplier
    template_name = 'product/supplier/supplier_update.html'
    fields = '__all__'
    success_url = "/product/supplierlist/"
    success_message = "<b>%(supplier_name)s</b> has been updated successfully"


class SupplierDelete(SuccessMessageMixin, DeleteView):
    model = Supplier
    template_name = 'product/supplier/supplier_confirm_delete.html'
    success_url = "/product/supplierlist/"
    success_message = "%(supplier_name)s has been deleted successfully"


# Product


class ProductEntry(SuccessMessageMixin, CreateView):
    template_name = 'product/product_entry.html'
    model = Product
    fields = '__all__'
    success_url = "/product/supplierlist/"
    success_message = "<b>%(product_name)s</b> has been updated successfully"


class ProductList(SuccessMessageMixin, ListView):
    model = Product
    template_name = 'product/product_list.html'
    context_object_name = 'productlist'


class ProductUpdate(SuccessMessageMixin, UpdateView):
    model = Product
    template_name = 'product/product_update.html'
    fields = '__all__'
    success_url = "/product/productlist/"
    success_message = "<b>%(product_name)s</b> has been updated successfully"


class ProductDelete(SuccessMessageMixin, DeleteView):
    model = Product
    template_name = 'product/product_confirm_delete.html'
    success_url = "/product/productlist/"
    success_message = "%(product_name)s has been deleted successfully"


class ProductDetails(SuccessMessageMixin, DetailView):
    model = Product
    template_name = 'product/product_front_store.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products_in_cart'] = Cart.objects.count()
        context['cartlist'] = Cart.objects.all()

        return context


class CategoryDetails(SuccessMessageMixin, ListView):
    model = Product
    paginate_by = 2
    template_name = 'product/temp_category.html'

    # context_object_name = 'allProducts'

    # def get_queryset(self):
    #     #category = get_object_or_404(Category, pk=self)
    #     queryresult = Product.objects.filter(category=self)
    #     return queryresult

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs['pk']
        # print(id, [o.category.id for o in Product.objects.all()], Category.objects.get(id=id), Product.objects.filter(category__id=id).all())
        category = get_object_or_404(Category, pk=id)
        context['categoryinfo'] = get_object_or_404(Category, pk=id)
        # context['product_list'] = Product.objects.filter(category__id=id).all()
        all_Product = Product.objects.filter(category=category).all()

        brand_dict = {}

        for i in all_Product:
            brand_dict[i.brand.id] = i.brand.brand_name

        context['brandlist'] = brand_dict
        context['categories'] = Category.objects.all()
        context['allProducts'] = category.product_category.all()
        # print(context['allProducts'])

        return context


def load_category_based_product(request):
    brands = request.GET.getlist('brand[]')
    categoryId = request.GET.get('catId', None)
    # print("brandId:",brandId)
    # brand = get_object_or_404(Brand, pk=brandId)
    category = get_object_or_404(Category, pk=categoryId)
    print("############Issue Here##############")
    if brands:

        allbrand_based_product = Product.objects.filter(
            brand__id__in=brands).filter(category=category).distinct()
    else:
        allbrand_based_product = Product.objects.filter(category=category).distinct()

    # model_to_dict(brand)
    t = render_to_string('product/ajax/product-list.html',
                         {'data': allbrand_based_product})

    return JsonResponse({'data': t})

    # Sorting based product


def load_sorting_based_product(request):
    sort_value = request.GET.get('sort_order_value', None)
    categoryId = request.GET.get('catId', None)
    print("Sort Value:", sort_value)
    # brand = get_object_or_404(Brand, pk=brandId)
    category = get_object_or_404(Category, pk=categoryId)
    print("############Sort Here##############")
    if sort_value == 'newest':

        allbrand_based_product = Product.objects.filter(
            category=category).order_by('-id').distinct()
    elif sort_value == 'priceHighLow':
        allbrand_based_product = Product.objects.filter(
            category=category).order_by('-offer_price').distinct()

    elif sort_value == 'priceLowHigh':
        allbrand_based_product = Product.objects.filter(
            category=category).order_by('offer_price').distinct()

    elif sort_value == 'a_to_z':
        allbrand_based_product = Product.objects.filter(
            category=category).order_by('product_name').distinct()

    elif sort_value == 'z_to_a':
        allbrand_based_product = Product.objects.filter(
            category=category).order_by('-product_name').distinct()
    else:
        allbrand_based_product = Product.objects.filter(
            category=category).distinct()

    # allbrand_based_product = Product.objects.filter(
    #     category=category).order_by('-offer_price').distinct()

    # model_to_dict(brand)
    t = render_to_string('product/ajax/product-list.html',
                         {'data': allbrand_based_product})

    return JsonResponse({'data': t})


class CartDetails(SuccessMessageMixin, ListView):
    model = Cart
    template_name = 'product/cart.html'


def addToCart(request):
    _product = request.GET.get('product_id', None)

    pquantity = request.GET.get('product_quantity', None)

    print(_product, pquantity)

    # product = Product.objects.get(pk=_product)
    product = Product.objects.get(pk=_product)

    # same_product = get_object_or_404(Cart, id=_product)
    same_product = Cart.objects.filter(product=product).first()

    print(same_product)
    print("_product", same_product)
    if same_product:
        sumc = int(same_product.quantity)
        pquantity = int(pquantity) + sumc

        same_product.delete()

    else:

        pquantity = pquantity
        # print("Else Quantity", pquantity)

    cart = Cart(product=product, quantity=pquantity)
    print(cart)
    cart.save()

    return JsonResponse({'data': 'saved successfully!'})


class CartList(SuccessMessageMixin, ListView):
    model = Cart
    template_name = 'product/cart.html'
    context_object_name = 'cartlist'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)


class Checkout(SuccessMessageMixin, CreateView):
    model = User
    fields = '__all__'
    template_name = 'product/checkout.html'

