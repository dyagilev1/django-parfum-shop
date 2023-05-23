from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Brand, Review, Contact
from django.contrib import messages
from .forms import ContactForm, ReviewForm
from cart.forms import CartAddProductForm
from .forms import ContactForm, ReviewForm



def product_list(request, category_slug=None):

    brand = Brand.objects.all()
    brandID = request.GET.get('brand') 

    category = None
    categories = Category.objects.all()
    
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    if brandID:
        products = Product.objects.filter(brand = brandID)
    else:
        Product.objects.all()

    return render (request, 'shop/product/list.html', context={
        'category': category,
        'categories': categories,
        'products': products,
        'brand': brand,

    })

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', context={
        'product': product,
        'cart_product_form': cart_product_form,
    })

def search_product(request):

    brand = Brand.objects.all()
    brandID = request.GET.get('brand') 

    category = None
    categories = Category.objects.all()

    if brandID:
        products = Product.objects.filter(brand = brandID)
    else:
        Product.objects.all() 
        
    query = request.GET.get("Q")
    products = Product.objects.filter(name__icontains=query)


    

    return render(request, 'shop/product/search.html', context={'products': products,
                                                                'query': query,
                                                                'category': category,
                                                                'categories': categories,
                                                                'brand': brand,                                                            
                                                                })


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST or None)
        errors = None
        if form.is_valid():
            Contact.objects.create(
                first_name = form.cleaned_data.get('first_name'),
                last_name = form.cleaned_data.get('last_name'),
                email = form.cleaned_data.get('email'),
                message = form.cleaned_data.get('message')
                )
            messages.warning(request,"Запит на зворотний зв'язок надіслано. Очікуйте...")
            return render(request,"shop/product/contact.html")
        if form.errors:
            errors = form.errors

        context = {'form':form, 'errors':errors}
        return render(request,"shop/product/contact.html", context )
    else:
        form = ContactForm()

    return render(request, "shop/product/contact.html", {'form':form})


def review(request):
    reviews = Review.objects.all()
    review_form = ReviewForm()

    if request.method == "POST":
        form = ReviewForm(request.POST or None)
        errors = None
        if form.is_valid():
            Review.objects.create(
                first_name = form.cleaned_data.get('first_name'),
                last_name = form.cleaned_data.get('last_name'),
                email = form.cleaned_data.get('email'),
                review_text = form.cleaned_data.get('review_text')
                )
            messages.warning(request,"Відгук додано успішно!")
            return render(request,"shop/product/review.html", context={'reviews':reviews})
        if form.errors:
            errors = form.errors

        context = {'form':form, 'errors':errors, 'reviews':reviews}
        return render(request,"shop/product/review.html", context )
    else:
        form = ReviewForm()

    return render(request, "shop/product/review.html", {'form':form, 'reviews':reviews})
