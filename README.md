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

