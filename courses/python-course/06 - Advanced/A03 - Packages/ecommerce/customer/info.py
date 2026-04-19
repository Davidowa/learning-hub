# To use the package cart here we have to use the intra-package reference.

# Absolute import
# from ecommerce.shopping.cart import show_cart

# Relative import
from ..shopping.cart import show_cart

# The two ... mean that we are navigating two levels up in the folder structure.


def show_customer():
    print("Showing customer")
    show_cart()

# Lets go back to the app.py file.
