# ECOMMERCE 

Created templates folder inside the app folder which is called store

Inside the templates folder is where I will store my html files:
Main.html → Template which all will inherit from
Store.html → Home page/store front with all products
Cart.html → Users shopping cart
Checkout.html → Checkout page
![firstnavbar](/readme-screenshots/templates.png)

Created views to render the html files 
![firstnavbar](/readme-screenshots/views.png)

Created STATIC folder to hold CSS files and images:
![firstnavbar](/readme-screenshots/staticfolder.png)

Now that I have set up the main template and added to the main CSS file, all I need to do is close out this section by finishing up the base styling for my 3 pages with placeholder data before I move on to setting up the database.
![firstnavbar](/readme-screenshots/navbar.png)

## Testing:
I was happy with my first attempt on creating the columns for the products and I used a placeholder picture to test how it would look on the site. I added the view and a "Add to cart" button features.
Here is the result: 
![placeholderscrnshot](/readme-screenshots/placeholderscrn.png)

At one point, my code started bugging. I created the cookie method to create and save products inside a cookie, while making an order as a guest user (Not logged in). The cookie collected the information, but the cart icon was not updating the quantity visually. 

Here is the ''Add to cart button''
![addtocart](/readme-screenshots/addtocart.png)
![cookieadd](/readme-screenshots/cookieadd.png)

Here, the cart icon does not update the quantity that's being added to the cookie.
![nocartupdate](/readme-screenshots/nocartupdate.png)

I tried running the whole project locally with Virtual Studio Code and suddenly, the issue was resolved. The cookie was fulfilling its purpose and the cart was updating the quantity:
![cartupdate](/readme-screenshots/cartupdate.png)


## Models:
1. User- Built in Dango user model. An instance of this model will be created for each customer that registers with our website. This model will give us the ability to later use Djangos default authentication system without having to manually set this up ourselves.
2. Customer - Along with a User model each customer will contain a Customer model that holds a one to one relationship to each user. (OneToOneField).
![usercustomer](/readme-screenshots/customer.png)

3. Product - The product model represents products we have in store.
![product](/readme-screenshots/product.png)

4. Order - The order model will represent a transaction that is placed or pending. The model will hold information such as the transaction ID, data completed and order status. This model will be a child or the customer model but a parent to Order Items.
![order](/readme-screenshots/order.png)

5. OrderItem- An order Item is one item with an order. So for example a shopping cart may consist of many items but is all part of one order. Therefore the OrderItem model will be a child of the PRODUCT model AND the ORDER Model.
![orderitem](/readme-screenshots/orderitem.png)

6. ShippingAddress- Not every order will need shipping information. For orders containing physical products that need to be shipping we will need to create an instance of the shipping model to know where to send the order. Shipping will simply be a child of the order model when necessary.
![shipping](/readme-screenshots/shippingaddress.png)


## Create products:
I created a few example projects from the admin panel:
![adminregister](/readme-screenshots/adminregister.png)
![createproducts](/readme-screenshots/createproducts.png)


## Errors
Cart does not exist error.

![cart-error](/readme-screenshots/cart-error.png)

One thing all first time visitors will see if we do not fix this is an error since they will have no cookie cart if this is their first time viewing our website.
I managed to fix this by using a try/except statement and create an empty cart to work with if one does not exist.
![cart-error-fix](/readme-screenshots/cart-error-fix.png)