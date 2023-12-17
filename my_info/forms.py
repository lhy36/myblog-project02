# from django.shortcuts import redirect,  get_object_or_404 
# from .forms import CartAddProductForm 
# from .cart import Cart
# from .models import Book

# # add_to_cart 뷰 내에서 폼 사용 예시
# def add_cart(request, book_id):
#     cart = Cart(request)
#     book = get_object_or_404(Book, id=book_id)
#     form = CartAddProductForm(request.POST)  # 사용자로부터 입력된 수량을 받기 위한 폼

#     if form.is_valid():
#         cd = form.cleaned_data
#         cart.add(book=book, quantity=cd['quantity'], update_quantity=cd['update'])

#     return redirect('cart')
