
## Technologies Used

- Full Stack: Python, Django, HTML, CSS, Bootstrap
- Database: MySQL
- Payment Gateway: Razorpay


## Features

- User Authentication: Secure login and registration for a personalized shopping experience.
- Shopping Cart: Efficient cart management for adding, updating, and removing products.
- Razorpay Integration: Seamless payment transactions through the Razorpay payment gateway.


## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

Install Python 3.7 or above

* <a href="https://python.org/downloads/" target="_blank">Python</a>
 
### Installation

> 👉 **Step 1** - Download the code from the GH repository (using `GIT`):
```bash
git clone https://github.com/prathmeshsoni/Ecommerce.git && cd Ecommerce
```

<br />

> 👉 **Step 2** - Create virtual environment:
```
python -m venv .venv
```

<br />

> 👉 **Step 3** - Activating the environment:

on Windows:
```bash
.venv\Scripts\activate.bat
```
on Mac OS / Linux:
```bash
source .venv\Scripts\activate
```

<br />

> 👉 **Step 4** - Installing dependencies:

```bash
pip install -r requirements.txt
```

<br />

> 👉 **Step 5** - You can now run the development server:

```bash
python manage.py runserver
```

Visit [`http://127.0.0.1:8000`](http://localhost:8000) in your browser. The app should be up & running.

<br />

> 👉 **Step 6** - Go `config.py` Not Necessary:


Go to the `config.py` file on the Ecommerce folder (`/music_club/config.py`) setting all requirements after "=". 

```
# For sending email to users during registration or password recovery
email = ''
password = ''

# For integrating with the Razorpay payment gateway.
razorpay_key_id = ''
razorpay_key_secret = ''
```

<br />

> 👉 **Step 7** - Integrate the Razorpay payment gateway for transactions.

Documentation: <a href="https://razorpay.com/docs/payments/server-integration/python/install/" target="_blank">Razorpay Integration</a>

**IMPORTANT**: Make sure your Razorpay account is running in `TEST Mode` and Use the Test token provided by Razorpay:

<br />

## Default Credentials

- **User Credentials:**
  - URL: http://127.0.0.1:8000/
  - Username: Pravin
  - Password: user@123

- **Admin Credentials:**
    - Django Admin Panel: http://127.0.0.1:8000/admin_side/
  - Username: admin
  - Password: admin@123

## Connect with me at

<p align='center'>
  <a href="#" target="_blank">
    <img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>
</p>

<p align='center'>
  📫 How to reach me: <a href='mailto:yadavpravin4444@gmail.com'>yadavpravin4444@gmail.com</a>
</p>


## All Set :)

<p style="float:left;" align="left">
  <a href="#top">Back To Top</a>
</p>

<p style="text-align:right;" align="right">
  <a href="https://github.com/Pravin06102005/Sport-Accessories-Store/tree/main" target="_blank">Back To Repository</a>
</p>
