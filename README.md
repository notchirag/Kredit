# Kredit

## Overview

This is a web application built with Django and Bootstrap, designed to assist money lenders in managing their records and details efficiently. The application provides a user-friendly interface for money lenders to keep track of their clients, loans, and installments.

## Technologies Used

- **Django:** A high-level Python web framework for rapid development and clean, pragmatic design.
- **Bootstrap:** A popular CSS framework for building responsive and mobile-first web pages.

## Features

- **Client Management:** Easily add, update, and delete client information.
- **Loan Tracking:** Keep detailed records of loans, including loan amount, interest rates, and due dates.
- **Interest Calculation:** Calculate both simple and compound interest for loans.
- **Installment History:** Track all installments related information which includes name, amount, date and mode of payment.
- **User Authentication:** Secure user authentication system to ensure only authorized users can access and manage data.
- **Responsive Design:** Bootstrap framework ensures the application is accessible and functional across various devices.

## Installation

To get up and running, simply do the following and set your admin username and password when prompted.
```bash
git clone https://github.com/notchirag/Kredit.git
cd Kredit
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

```
