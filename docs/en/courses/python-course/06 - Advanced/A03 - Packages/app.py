# Packages
# Packages are used to organize modules.
# Packages are folders that contain modules.
# Lets take this folder structure as an example:
# 06 - Advanced
# └── A02 - Packages
#     ├── ecommerce
#     │   └── ecommerce.py
#     └── app.py

# In this structure, we have a package called ecommerce.

# To create a package, we have to create a folder with an __init__.py file inside it.
from ecommerce.ecommerce import calculate_shipping, calculate_tax
import ecommerce.ecommerce as e
import ecommerce.ecommerce

from ecommerce.shopping.cart import show_cart
import ecommerce.shopping.cart as s
import ecommerce.shopping.cart

from ecommerce.customer.info import show_customer
import ecommerce.customer.info as c
import ecommerce.customer.info

ecommerce.ecommerce.calculate_shipping()
ecommerce.ecommerce.calculate_tax()

# This is tedious, so we can use the from statement to import the module directly.

calculate_shipping()
calculate_tax()

e.calculate_shipping()
e.calculate_tax()

# Subpackages
# As the project grows, we can create subpackages.
# Lets take this folder structure as an example:
# 06 - Advanced
# └── A02 - Packages
#     ├── ecommerce
#     │   ├── __init__.py
#     │   ├── ecommerce.py
#     │   └── shopping
#     │       ├── __init__.py
#     │       └── cart.py
#     └── app.py

# In this structure, we have a package called ecommerce.
# We also have a subpackage called shopping.
ecommerce.shopping.cart.show_cart()
show_cart()
s.show_cart()


# Intra-package References
# Intra-package references are used to import modules from a package.
# Lets take this folder structure as an example:
# 06 - Advanced
# └── A02 - Packages
#     ├── ecommerce
#     │   ├── __init__.py
#     │   ├── ecommerce.py
#     │   ├── shopping
#     │   │   ├── __init__.py
#     │   │   └── cart.py
#     │   └── customer
#     │       ├── __init__.py
#     │       └── info.py
#     └── app.py

# Lets go to the file info.py and continue the lesson there.

# Welcome back.

# To use the package info, lets import it.
ecommerce.customer.info.show_customer()
show_customer()
c.show_customer()


# Lets see the dir function.
print(dir(ecommerce.customer.info))
print(dir(c))

# but we can also print different things.
print(ecommerce.customer.info.__name__)
print(ecommerce.customer.info.__package__)
print(ecommerce.customer.info.__file__)

print(c.__name__)
print(c.__package__)
print(c.__file__)
