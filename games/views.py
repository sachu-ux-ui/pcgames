from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

def index(request):
    p = products.objects.all()[:6]  # limit 6
    return render(request, 'index.html', {'products': p})
def add_products(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        category = request.POST.get('category')
        image = request.FILES.get('image')
        products.objects.create(name=name,Price=price,Quantity=quantity,Category=category,Description=description,Image=image)
        messages.success(request, 'registration successfull')
        return redirect ('home')
    return render(request, 'products.html')    

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
        else:
            User.objects.create(name=name, email=email, password=password, address=address, phone=phone)
            messages.success(request, 'registration successfull')
            return redirect ('index')
    return render(request, 'register.html')
def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email, password=password)

            # ✅ STORE SESSION (THIS WAS MISSING)
            request.session['email'] = user.email

            return render(request, 'index.html', {'user': user})

        except User.DoesNotExist:
            return render(request, 'login.html', {
                'error': 'Invalid email or password'
            })

    return render(request, 'login.html')

def profile(request):
    email = request.session.get('email')

    if email is not None:
        try:
            user = User.objects.get(email=email)
            return render(request, 'profile.html', {'user':user})
        except User.DoesNotExist:
            messages.error(request, "User not found.")
            Category = request.POST.get('category')
        return redirect('login')
    else:
        messages.warning(request, "You need to log in to access your profile.")
        return redirect('login') 

def editprofile(request):
    email = request.session.get('email') 
    user = User.objects.get(email=email)  
    if request.method == 'POST':
        # Get the form data
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        location = request.POST.get('location')
        user.name = name
        user.phone = phone
        user.address = location
        user.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')  
    return render(request, 'profile.html', {'user': user})

def userlist(request):
    user=User.objects.all()
    return render(request,'userlist.html',{'user':user})
def deleteuser(request,id):
    data=User.objects.filter(id=id)
    data.delete()
    return redirect('userlist')
def product_list(request):
    p = products.objects.all()
    return render(request, 'productlist.html', {'p': p})



    
def edit_product(request, id):
    product = get_object_or_404(products, id=id)

    if request.method == "POST":
        product.name = request.POST.get('name')
        product.Description = request.POST.get('Description')
        product.Price = int(request.POST.get('Price') or 0)
        product.Quantity = int(request.POST.get('Quantity') or 0)
        product.Category = request.POST.get('Category')

        if request.FILES.get('Image'):
            product.Image = request.FILES.get('Image')

        product.save()

        print("UPDATED SUCCESSFULLY ✅")  # DEBUG

        return redirect('product_list')

    return render(request, 'edit_productlist.html', {'product': product})

    return render(request, 'edit_productlist.html', {'product': product})
def delete_product(request,id):
    data=products.objects.filter(id=id)
    data.delete()
    return redirect('product_list')    
def userproductlist(request):
    p = products.objects.all()
    return render(request, 'userproductlist.html', {'p': p})
def add_to_cart(request, id):
    email = request.session.get('email')

    if not email:
        return render(request, 'cartlist.html', {
            'error': 'Please login first'
        })

    user = get_object_or_404(User, email=email)
    product = get_object_or_404(products, id=id)

    quantity = int(request.POST.get('quantity', 1))

    cart_item, created = Cart.objects.get_or_create(
        user=user,
        product=product
    )

    if not created:
        cart_item.quantity += quantity
    else:
        cart_item.quantity = quantity

    cart_item.save()

    return redirect('cart_list')  # 👉 go to cart page
def delete_cart(request, id):
    if request.method == "POST":
        cart_item = get_object_or_404(Cart, id=id) 
        cart_item.delete() 
        return redirect('cart') 
    return render(request, 'cart.html')     
def add_to_wishlist(request, id):
    product = get_object_or_404(products, id=id)
    email = request.session.get('email')

    if email:
        user = get_object_or_404(User, email=email)

        wishlist.objects.get_or_create(
            user=user,
            product=product,
        )

        return redirect('viewwishlist')

    else:
        return JsonResponse(
            {'error': 'User not logged in'},
            status=400
        )   

def cart_list(request):
    email=request.session.get('email')
    user = get_object_or_404(User, email=email)
    cart_items = Cart.objects.filter(user=user)
    return render(request, 'cartlist.html', {'cart_items': cart_items})
def viewwishlist(request): 
     email = request.session.get('email') 
     if email: 
        user = get_object_or_404( User,email=email) 
        wishlist_items = wishlist.objects.filter(user=user)
     
        return render(request, 'wishlist.html', {'wishlist_items': wishlist_items}) 
     else: 
        return render(request, 'wishlist.html', {'AUTHENTICATION FAILED': 'User email not found in session. Please login first.'})    