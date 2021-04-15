from django.shortcuts import render,redirect
from .forms import categoryForm,supplierForm

from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Category,Brand,Variant,Unit,Currency,Supplier,Product
from django.views.generic.base import TemplateView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.forms.models import model_to_dict




# Create your views here.



#Save Category Info
def saveCategory(request):

    form = categoryForm(request.POST or None,request.FILES)

    if request.method=='POST':

       print("All Files",request.FILES) 

       print("All Data",request.POST) 

       if form.is_valid():

          form.save()

          return redirect('/product/categorylist/')

    return render(request,'category.html',{'form':form})

#Edit category info based on requested id
def editCategory(request,pk):

    print("PK",pk)

    editedCategory = Category.objects.get(pk=pk)

    print(editedCategory)

    print("Post Data",request.POST)

    form = categoryForm(request.POST or None,instance = editedCategory)

    if request.method=="POST":
       form = categoryForm(request.POST or None,request.FILES,instance = editedCategory)    
       if form.is_valid():

          form.save()
          messages.success(request, 'Form submission successful')

          return redirect('/product/categorylist/') 
    return render(request,'editCategory.html',{'form':form})      



#Delete category

def deleteCategory(request, pk):

    deletedCategory = Category.objects.get(pk=pk)
    if deletedCategory:
       deletedCategory.delete()
       return redirect('/product/categorylist/')
    return redirect('/product/categorylist/')

def category_list(request):

    catList = Category.objects.all().order_by('-id')
    return render(request,'catlist.html',{"catlist":catList})    

###########Brand###################################
class BrandEntry(SuccessMessageMixin,CreateView):

    model = Brand
    template_name = 'product/brand_entry.html'
    fields = '__all__'
    success_url ="/product/brandlist/"
    success_message = "%(brand_name)s has been created successfully"

class BrandList(SuccessMessageMixin,ListView):
    model = Brand
    template_name = 'product/brand_list.html'
    context_object_name = 'brandlist'
    

class BrandUpdate(SuccessMessageMixin,UpdateView):

    model = Brand
    template_name = 'product/brand_update.html'
    fields = '__all__'
    success_url ="/product/brandlist/"
    success_message = "<b>%(brand_name)s</b> has been updated successfully"


class BrandDelete(SuccessMessageMixin,DeleteView):
    model = Brand
    success_url ="/product/brandlist/"
    success_message = "%(brand_name)s has been deleted successfully"


class Dashboard(TemplateView):

    template_name = 'product/main.html'



###Variant####

class VariantEntry(SuccessMessageMixin,CreateView):

    model = Variant
    template_name = 'product/variant_entry.html' 
    fields = '__all__'
    success_url ="/product/variantlist/"
    success_message = "%(variant_name)s has been added successfully"

class VariantList(SuccessMessageMixin,ListView):
    model = Variant
    template_name = 'product/variant_list.html'
    context_object_name = 'variantlist'    
     
class VariantUpdate(SuccessMessageMixin,UpdateView):

    model = Variant
    template_name = 'product/variant_update.html'
    fields = '__all__'
    success_url ="/product/variantlist/"
    success_message = "<b>%(variant_name)s</b> has been updated successfully"


class VariantDelete(SuccessMessageMixin,DeleteView):
    model = Variant
    success_url ="/product/variantlist/"
    success_message = "%(variant_name)s has been deleted successfully"  


###Unit####

class UnitEntry(SuccessMessageMixin,CreateView):

    model = Unit
    template_name = 'product/unit_entry.html' 
    fields = '__all__'
    success_url ="/product/unitlist/"
    success_message = "%(unit_name)s has been added successfully"

class UnitList(SuccessMessageMixin,ListView):
    model = Unit
    template_name = 'product/unit_list.html'
    context_object_name = 'unitlist'    
     
class UnitUpdate(SuccessMessageMixin,UpdateView):

    model = Unit
    template_name = 'product/unit_update.html'
    fields = '__all__'
    success_url ="/product/unitlist/"
    success_message = "<b>%(unit_name)s</b> has been updated successfully"


class UnitDelete(SuccessMessageMixin,DeleteView):
    model = Unit
    success_url ="/product/unitlist/"
    success_message = "%(unit_name)s has been deleted successfully"        


###Currency####

class CurrencyEntry(SuccessMessageMixin,CreateView):

    model = Currency
    template_name = 'product/currency_entry.html' 
    fields = '__all__'
    success_url ="/product/currencylist/"
    success_message = "%(currency_name)s has been added successfully"

class CurrencyList(SuccessMessageMixin,ListView):
    model = Currency
    template_name = 'product/currency_list.html'
    context_object_name = 'currencylist'    
     
class CurrencyUpdate(SuccessMessageMixin,UpdateView):

    model = Currency
    template_name = 'product/currency_update.html'
    fields = '__all__'
    success_url ="/product/currencylist/"
    success_message = "<b>%(currency_name)s</b> has been updated successfully"


class CurrencyDelete(SuccessMessageMixin,DeleteView):
    model = Currency
    success_url ="/product/currencylist/"
    success_message = "%(currency_name)s has been deleted successfully"     


#Supplier

###Currency####

class SupplierEntry(SuccessMessageMixin,CreateView):

    model = Supplier
    form_class = supplierForm
    template_name = 'product/supplier/supplier_entry.html' 
    # fields = '__all__'
    success_url ="/product/supplierlist/"
    success_message = "%(supplier_name)s has been added successfully"

class SupplierList(SuccessMessageMixin,ListView):
    model = Supplier
    template_name = 'product/supplier/supplier_list.html'
    context_object_name = 'supplierlist'    
     
class SupplierUpdate(SuccessMessageMixin,UpdateView):

    model = Supplier
    template_name = 'product/supplier/supplier_update.html'
    fields = '__all__'
    success_url ="/product/supplierlist/"
    success_message = "<b>%(supplier_name)s</b> has been updated successfully"


class SupplierDelete(SuccessMessageMixin,DeleteView):
    model = Supplier
    template_name = 'product/supplier/supplier_confirm_delete.html'
    success_url ="/product/supplierlist/"
    success_message = "%(supplier_name)s has been deleted successfully"  
    
#Product

class ProductEntry(SuccessMessageMixin,CreateView):
    template_name = 'product/product_entry.html' 
    model = Product
    fields = '__all__'
    success_url ="/product/supplierlist/"
    success_message = "<b>%(product_name)s</b> has been updated successfully"

class ProductList(SuccessMessageMixin,ListView):
    model = Product
    template_name = 'product/product_list.html'
    context_object_name = 'productlist'    


class ProductUpdate(SuccessMessageMixin,UpdateView):

    model = Product
    template_name = 'product/product_update.html'
    fields = '__all__'
    success_url ="/product/productlist/"
    success_message = "<b>%(product_name)s</b> has been updated successfully"


class ProductDelete(SuccessMessageMixin,DeleteView):
    model = Product
    template_name = 'product/product_confirm_delete.html'
    success_url ="/product/productlist/"
    success_message = "%(product_name)s has been deleted successfully"  


class ProductDetails(SuccessMessageMixin,DetailView):

    model = Product
    template_name = 'product/product_front_store.html'    


    
class CategoryDetails(SuccessMessageMixin,ListView):
    model = Product
    template_name = 'product/temp_category.html'

    def get_context_data(self,**kwargs):

        context = super().get_context_data(**kwargs)
        id = self.kwargs['pk']
        #print(id, [o.category.id for o in Product.objects.all()], Category.objects.get(id=id), Product.objects.filter(category__id=id).all())
        category = get_object_or_404(Category,pk=id)
        context['categoryinfo'] = get_object_or_404(Category,pk=id)
        # context['product_list'] = Product.objects.filter(category__id=id).all()
        context['brandlist'] = Brand.objects.all()
        context['categories'] = Category.objects.all()
        context['allProducts'] = category.product_category.all()
        print(context['allProducts'])

        return context    


def load_category_based_product(request):
    brandId = request.GET.get('brand', None)
    print("brandId:",brandId)
    brand = get_object_or_404(Brand, pk=brandId)
    
    
    # data = {

    #     "backdata": brandId
    # }  
    return JsonResponse(model_to_dict(brand))


