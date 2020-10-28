
# Checkout
A Personal finance web app where users can track and visualize their payments and expenses.
[Link](https://checkout-finance.herokuapp.com/)

## Apps
  - ###  Checkout
  -  ### Dashboard
  - ### Payment
  - ### Wishlist
 
### Checkout
  - views\.py
      - Handles login/logout/register.
      - Handles creating/updating/deleting items.
      - Displays items and categories in homepage.
      - Handles searching items.
  - models.py
      - User
      - Item
      - Category
  - forms.py
    - ModelForm for item.
  - utils.py
    Helper functions.
    - Paginate items.
     - Get a category's name.
     - Display error page.

## Dashboard
  Visualizes user data.
  - views.py
    - Gathers the data.
    - Displays the visualization page.
  - utils.py
    - Uses Matplotlib to draw a bar chart.
    - Uses io library to create and save images to memory.
 
 ## Payment
   - views.py
     - Adds/deletes payments.
     - Displays payments page. 
   - models.py
     - Model for payments.
   - forms.py
     - ModelForm for payment.

## Wishlist
  - views.py
    - Adds/deletes wishlist items.
    - Displays wishlist page.
  -  models.py
    - Model for wishlist item.
  - forms.py
    - ModelForm for wishlist item.

## Static files
  - Javascript files for creating/updating/deleting Items/Payments       /Wishlist Items without reloading the page.
  - CSS files for styling pages and elements.

## Procfile
  - For deploying the app on Heroku.
