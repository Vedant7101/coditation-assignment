# Coditation Assignment

In this assignment REST API is implemeneted using Django framework of python.

## Software Requirements
- Python 
- MySQL

## Required Python Libraries
- Django
- pyodbc
- mysqlclient
- djangorestframework
- django-cors-headers 

## Starting Application

- After starting application you can open home page on http://localhost:8000
- I have kept another html file in root directory in case to test rest api seperate from server

## Rest API Commands

### Category commands

- To get list of all categories (GET): 

  http://127.0.0.1:8000/api/categoryList/
  
- To get information of particular category (GET):

  http://127.0.0.1:8000/api/categoryList/?category=<Category Name\>
  
  For e.g http://127.0.0.1:8000/api/categoryList/?category=Category 1

- To add new category (POST): 

  http://127.0.0.1:8000/api/addCategory/
  
  Paramaters = {
    "category_name": "Category 1.1",
    "parent_category": "Category 1"
  }
  
- To delete particular category (DELETE):

  http://127.0.0.1:8000/api/category/<Category ID\>/
  
  For e.g http://127.0.0.1:8000/api/category/16/  
  
### Product Commands
  
- To get list of all products (GET):
  
  http://127.0.0.1:8000/api/productList/
  
- To get information of particular product (GET):
  
  http://127.0.0.1:8000/api/productList/?product_name=<Product Name\>
  
  For e.g. http://127.0.0.1:8000/api/productList/?product_name=Product 1
  
- To get list of products in particular category (GET):
  
  http://127.0.0.1:8000/api/productList/?category=<Category Name\>
  
  For e.g. http://127.0.0.1:8000/api/productList/?category=Category 1
  
- To add new product (POST):
  
  http://127.0.0.1:8000/api/addProduct/
  
  parameters = {
    "product_name": "Product 1",
    "categories": "Category 1,Category 2",
  	"price": 100
  }
  
- To update existing product (PUT):
  
  http://127.0.0.1:8000/api/product/<Product ID\>/
  
  For e.g http://127.0.0.1:8000/api/product/10/
  
  parameters = {
    "product_name": "Product 6",
    "categories": "Category 1,Category 3",
  	"price": 50
  }
  
- To delete specific product (DELETE):
  
  http://127.0.0.1:8000/api/product/<Product ID\>/
  
  For e.g http://127.0.0.1:8000/api/product/10/
