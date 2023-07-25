
# Riverway - E-commerce Website using Django

RiverWay is an ecommerce website that allows users to buy and sell products online. The website has all the basic functionality of an ecommerce website, including a shopping cart, checkout process, account management, and order tracking.


## Features

- User Authentication
- Product Catalog and Search
- Shopping Cart
- PayPal Payment Gateway
- Order Tracking


## Deployment

1. Clone the repository:

```bash
  git clone https://github.com/Aditya-kr-jha/riverWay.git
```
2. Create a virtual environment and activate it.

3. Install dependencies:

```bash
 pip install -r requirements.txt

```
4. Install dependencies:

```bash
 pip install -r requirements.txt

```
5. Set up AWS credentials and create an S3 bucket for static files.

6. Update the database settings in settings.py to connect to your AWS RDS PostgreSQL instance.

7. Apply migrations:

```bash
 python manage.py migrate

```
8. Run the development server:

```bash
 python manage.py runserver

```
 The website should now be accessible at http://localhost:8000/.





## Technologies Used
* Django: Backend framework for handling user authentication and managing data models.
* HTML/CSS: Frontend design for a clean and responsive user interface.
* AWS Elastic Beanstalk: Deployment and scaling of the application.
* AWS S3: Storage for static files, improving performance.
* AWS RDS PostgreSQL: Database management for efficient data storage.
* PayPal: Integration for secure and convenient payment options.
