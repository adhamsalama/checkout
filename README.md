

# Checkout
A Personal finance web app where users can track and visualize their payments and expenses.
Users can create items that they have bought with details like what's the item's name, price, quantity, seller, date, category and comments.
The app stores the items and makes them searchable, and visualizes the data by generating bar charts for specific dates chosen by the user.
The app also stores payments and wishlist items.
[Link](https://checkout-finance.herokuapp.com/)

## Apps
  - ###  Checkout
  - ### Dashboard
  - ### Payment
  - ### Wishlist
 
### Checkout
  - views\.py
      - register function
        - Handles registering for the app. 
      - login_view function
        - Handles logging in the app.
       - logout_view function
         - Handles logging out the app.
        - index function
          - Gets the items the users have stored and displays them in index.html.
       - create_item function
         -  If the request made is GET, shows the user a page for creating new item.
         - If the request made is POST, receives the new item information and adds it to the database.     
      - edit_item function
        - If the request made is GET, returns the HTML form for editing the item.
        - If the request made is POST, updates the item with the new information.
       - delete_item function
         - Receives and item id and deletes it from the database.
       - update_balance function
         - Updates the user balance with the entered quantity.
       - profile function
         - Shows the user's profile page.
       - search function
         - Searches the user's items for the entered query and returns a page with all the results.
       - category function
         - Gets all the items of a certain category and displays a page with the results.
       - change_password function
         - Changes the user's password.
       - error404 function
         - Returns a custom error page.
  - models.py
      -  User model.
      - Item model.
      - Category model.
  - forms.py
    - ModelForm for item.
  - utils.py
    Helper functions.
    - paginate function.
      - Receives a list of items and optionally a page number and a paginated version of the items.
    - get_categories function.
      - Returns all user's categories. 
    - error function.
      - Returns a custom error page with a specific message. 
 - Templates
	  - layout.html
		   - Base for all other templates. 
	  - index.html
		  - Shows the user's latest items.
	  -  error.html
		  - Shows a custom error page.
	  - profile.html
		  - Shows the user's account information.
	  - search.html
		  - Shows the results for a user's search.  
	  - paginator.html
		  - Shows a paginated page of items.  
	  - edit_item_form.html
		  - A form for editing an item, which will be filled with the item's information.  
	  - register.html
		  - A page with a form for registering a user.
	- login.html
		- A page with a form for logging in a user. 
- Static
   - add_item.js
     - Shows the user a form for creating a new item and sends a request to the server to add the item without reloading the page.
   - edit_item.js
     - Shows a form for editing an item and saving it without reloading the page. 
   - delete_item.js
     - Deletes an item and removes it from the page without reloading the page.
   - darkly.css
     - Bootstrap theme.
   - styles.css
     - Custom CSS rules.  
   - logo.png
     - Logo for the project.
## Dashboard
Visualizes user data.
- views.py
	- get_data function
		- Receives a request with a date, collects the items bought on that date, uses plot_barchart function to create two images that visualize the data for the month and the year, and returns the images.
	- index function
		- Uses get_data function to get the data for the current month and year, and displays the data in an HTML page. 
- utils.py
	- plot_barchart function.
		- Gets data as input, generates a bar chart image using Matplotlib and returns that image.
- Templates
	- index.html
		- Shows page with a date input and displays the data for that date.
  
 ## Payment
- views.py
	- index function
		- Gets all user payments, paginates them and displays them in a page.
	- add function
		- Adds a user payment to the database. 
	- delete function
		- Deletes a user payment from the database. 
- models.py
	- Payment model.     
- forms.py
	- ModelForm for payment.
- Templates
	- index.html
		- A page that shows user's payments and a form to add new payments.  
- Static
	- add_payment.js
		- Sends a request to the server to add new payment and adds it to the page without reloading the page. 
	- delete_payment.js
		- Sends a request to the server to delete a payment and removes it from the page without reloading the page.
  
## Wishlist
- views.py
	- index function
		- Gets all wishlist items, paginates them and displays a page that shows the wishlist items.
	- get_form function
		- Returns form for a adding wishlist item. 
	- add_wishlist function
		- Receives data for adding a new wishlist item and adds it, or returns an error if something wrong happened.
	- delete_wishlist function 
		- Receives wishlist item id and deletes that item. 
-  models.py
	- Model for wishlist item.
- forms.py
	- ModelForm for wishlist item.
- Templates
	- index.html
		- A page that shows all wishlist items and a form to add new wishlist items.
	- form.html
		- A form for adding new wishlist items.     
- Static
	-  addwishlist.js
		- Sends a request to the server to add new wishlist item and adds it to the page without reloading the page. 
	- deletewishlist.js
		-  Sends a request to the server to delete wishlist item and removes it from the page without reloading the page.

## Staticfiles
 A directory of collected static files of the project. (Required even if empty for Heroku deployment to work)

## Requirements.txt
- A list of required Python packages to run the project.

## Procfile
  - For deploying the app on Heroku.
