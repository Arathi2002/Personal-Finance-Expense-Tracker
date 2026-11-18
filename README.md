 HEAD
# Personal Finance and Expense Tracker

## About the Project

Personal Finance and Expense Tracker is a web-based application developed using Python and Django.

The application helps users manage their personal finances by tracking income and expenses. It provides a dashboard where users can view their total income, total expenses, and remaining balance.

## Features

- Add new income transactions.
- Add daily expense transactions.
- Select transaction categories.
- Record transaction dates.
- View total income.
- View total expenses.
- Calculate net balance automatically.
- View transaction history.
- Delete transaction records.

## Technologies Used

- Python
- Django
- SQLite3
- HTML
- CSS

## Project Structure

```text
expense_tracker/
│
├── config/
├── expenses/
│   ├── migrations/
│   ├── templates/
│   │   └── expenses/
│   │       └── dashboard.html
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
│
├── manage.py
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Folder

```bash
cd expense_tracker
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply Database Migrations

```bash
python manage.py migrate
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

### 8. Open in Browser

http://127.0.0.1:8000/

## Balance Calculation

Net Balance = Total Income - Total Expenses

Example:

- Total Income: ₹3000
- Total Expenses: ₹2000.02
- Net Balance: ₹999.98

## Future Enhancements

- Monthly expense reports.
- Budget management.
- Graphical expense analysis.
- Downloadable financial reports.

## Author
Arathi Munigala

=======
# Personal-Finance-Expense-Tracker
A web-based personal finance and expense tracking application built using Python and Django.
b08ef128914ba9691c5b0112883c6dcb3e701c51
