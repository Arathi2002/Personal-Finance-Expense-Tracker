from django.db import models

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('INCOME', 'Income'),
        ('EXPENSE', 'Expense'),
    ]

    CATEGORY_CHOICES = [
        ('FOOD', 'Food & Dining'),
        ('TRAVEL', 'Transport & Travel'),
        ('BILLS', 'Utilities & Bills'),
        ('SALARY', 'Salary/Stipend'),
        ('OTHER', 'Other'),
    ]

    title = models.CharField(max_length=120)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES, default='EXPENSE')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='OTHER')
    date = models.DateField()

    def __str__(self):
        return f"{self.title} - {self.amount} ({self.transaction_type})"
