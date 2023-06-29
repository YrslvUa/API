# Django Restaurant Management System
This is a Django-based restaurant management system that allows you to manage employees, restaurants, menus, menu items, and votes.

##Installation:
1 Clone the repository: git clone <repository_url>
2 Install the required dependencies using pip: 
```bash
pip install -r requirements.txt
3 Apply the database migrations: python manage.py migrate
4 Start the development server: python manage.py runserver
5 Access the application at http://localhost:8000 in your web browser.

##Features
##Employee
The Employee model represents a user of the system.
Employees can be created with an email and password.
Superusers can be created with additional staff and superuser privileges.
The following fields are available for an employee:
username: A unique username for the employee.
first_name: The first name of the employee.
last_name: The last name of the employee.
email: The email address of the employee (used for authentication).
telephone: The telephone number of the employee.
is_active: Indicates whether the employee account is active.
is_staff: Indicates whether the employee has staff privileges.
created: The date and time when the employee was created.
updated: The date and time when the employee was last updated.
##Restaurant
The Restaurant model represents a restaurant in the system.
Each restaurant has an owner who is an Employee instance.
The following fields are available for a restaurant:
name: The name of the restaurant.
address: The address of the restaurant.
contact_info: Contact information for the restaurant.
created: The date and time when the restaurant was created.
updated: The date and time when the restaurant was last updated.
##Menu
The Menu model represents a menu in a restaurant.
Each menu belongs to a Restaurant instance and contains multiple MenuItem instances.
The following fields are available for a menu:
name: The name of the menu.
restaurant: The restaurant to which the menu belongs.
items: The menu items included in the menu.
is_published: Indicates whether the menu is published.
created: The date and time when the menu was created.
updated: The date and time when the menu was last updated.
date: The date when the menu was created.
##MenuItem
The MenuItem model represents an item in a menu.
Each menu item can have an optional image associated with it.
The following fields are available for a menu item:
name: The name of the menu item.
description: The description of the menu item.
price: The price of the menu item.
product_img: An image representing the menu item.
created: The date and time when the menu item was created.
updated: The date and time when the menu item was last updated.
##Vote
The Vote model represents a vote by an Employee for a Menu.
Each vote includes the employee, menu, date, and rating.
The following fields are available for a vote:
menu: The menu for which the vote is cast.
employee: The employee who cast the vote.
date: The date when the vote was cast.
