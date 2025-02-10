from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from movies.models import Movie
from .utils import calculate_cart_total
from .models import Movie  # Make sure to import the Movie model


def index(request):
    cart_total = 0
    movies_in_cart = []
    cart = request.session.get('cart', {})
    movie_ids = list(cart.keys())  # Get all the movie IDs in the cart

    if movie_ids:  # Checks if movie_ids list is not empty
        movies_in_cart = Movie.objects.filter(id__in=movie_ids)  # Fetch the movies by their IDs
        cart_total = calculate_cart_total(cart, movies_in_cart)  # Calculate the total price

    # Prepare the data to be passed to the template
    template_data = {
        'title': 'Cart',  # Page title
        'movies_in_cart': movies_in_cart,  # List of movies in the cart
        'cart_total': cart_total,  # Total price of the cart
    }

    # Render the template with the data
    return render(request, 'cart/index.html', template_data)


def add(request, id):
    get_object_or_404(Movie, id=id)
    cart = request.session.get('cart', {})
    cart[id] = request.POST['quantity']
    request.session['cart'] = cart
    return redirect('home.index')

def add_to_cart(request, id):
    get_object_or_404(Movie, id=id)
    cart = request.session.get('cart', {})
    cart[id] = request.POST['quantity']
    request.session['cart'] = cart
    return redirect('cart.index')
