Django Product Database

📌 Overview

This is a simple Django project for managing products.
It demonstrates Django models, admin, queries, media files, and templates.


---

🚀 Features

Product model with fields:

name, price, available, category, stock, rating

released_on, added_at, updated_at

image (upload product picture)


Admin panel to add, edit, and search products.

QuerySet examples for filtering, ordering, and searching.

Media support for uploading and displaying images.

Template (HTML) to display products in a grid with name, price, category, and image.



---

⚙ Installation

1. Clone the repo:

git clone https://github.com/yourusername/django_product_database.git
cd django_product_database


2. Create and activate virtual environment:

python -m venv venv
venv\Scripts\activate   # On Windows


3. Install dependencies:

pip install -r requirements.txt


4. Run migrations:

python manage.py makemigrations
python manage.py migrate


5. Create a superuser:

python manage.py createsuperuser


6. Run the server:

python manage.py runserver




---

🌐 Usage

Go to http://127.0.0.1:8000/admin/ → manage products.

Go to http://127.0.0.1:8000/app3/ → view products list with images.



---

📷 Example

Products page will show:

Product image (or placeholder)

Name, price, category, stock, and rating
