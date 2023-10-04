from django.shortcuts import render,redirect,HttpResponse
from app.models import *
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.contrib.auth.models import User


def Master(request):
    return render(request, 'master.html')

def Index(request):
    categoryID = request.GET.get('category')
    brandID = request.GET.get('brand')
    brand = Brand.objects.all()
    category = Category.objects.all()
    if categoryID:
        product = Product.objects.filter(sub_category = categoryID).order_by('-id')
    elif brandID:
        product = Product.objects.filter(brand = brandID).order_by('-id')
    else:
        product = Product.objects.all()

    context = {
        "category":category,
        "product":product,
        "brand":brand,
    }

    return render(request, 'index.html',context)


def Signup(request):
    if request.method == "POST":
        form = UserCreateFrom(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1'],
            )
            login(request,new_user)
            return redirect('index')
    else:
        form = UserCreateFrom()
    context = {
        "form":form
    }
    print('error is this-> ',form.error_messages)
    return render(request, 'registration/signup.html',context) 


@login_required(login_url="/accounts/login/")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")


@login_required(login_url="/accounts/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")

 
@login_required(login_url="/accounts/login/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')


def Contact(request):
    if request.method == 'POST':
        contact = Contact_us(
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            subject = request.POST.get('subject'),
            message = request.POST.get('message'),
        ) 
        contact.save()
    return render(request,'contact-us.html')

def CheckOut(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        cart = request.session.get('cart')
        uid = request.session.get('_auth_user_id')
        user = User.objects.get(pk=uid)
        print(phone, address, pincode, cart,uid,user)
        for i in cart:
            a = cart[i]['price']
            b = cart[i]['quantity']
            total_price = (int(a) * int(b))

            order = Order(
            user = user,
            product = cart[i]['name'],
            quantity = cart[i]['quantity'],
            price = cart[i]['price'],
            image = cart[i]['image'],
            pincode = pincode,
            address = address,
            phone_number = phone,
            total = total_price,
            )

            order.save()
        request.session['cart'] = {}
        return redirect('/')

def Your_Order(request):
    uid = request.session.get('_auth_user_id')
    user = User.objects.get(pk=uid)

    order = Order.objects.filter(user = user)
    context = {
        'order' : order,
    }
    print(order)
    return render(request, 'order.html',context)

def Product_detail(request):
    id = request.GET.get('item')
    product = Product.objects.filter(id = id).first()
    category = Category.objects.all()
    brand = Brand.objects.all()
    print(id) 
    print("------------------------------------product----------------------------")
    # print(product.name)
    context = {
        'product':product,
        'category':category,
        'brand':brand
    }
    return render(request, 'product_detail.html',context)

def Product_page(request):
    category = Category.objects.all()
    brand = Brand.objects.all()
    categoryID = request.GET.get('category')
    brandID = request.GET.get('brand')
    if categoryID:
        product = Product.objects.filter(sub_category = categoryID).order_by('-id')
    elif  brandID:
        product = Brand.objects.filter(brand = brandID).order_by('-id')
    else:
        product = Product.objects.all()

    context = {
        'category':category,
        'brand':brand,
        'product':product,
    }
    return render(request,'product.html',context)

def Search(request):
    query = request.GET['query']
    product = Product.objects.filter(name__icontains = query)
    context = {
        'product' : product
    }
    return render(request, 'search.html',context)
