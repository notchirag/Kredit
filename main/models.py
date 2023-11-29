from django.db import models
from datetime import date

class Entries(models.Model):
    name = models.CharField(max_length=50)
    father = models.CharField(max_length=50)
    borrow_date = models.DateField(default=date.today)
    due_date = models.DateField()
    contact_one = models.CharField(max_length=15)
    contact_two = models.CharField(max_length=15, blank=True, null=True)
    principal = models.PositiveIntegerField()
    interest = models.DecimalField(max_digits=4, decimal_places=2)
    address = models.CharField(max_length=100)
    guarantor = models.CharField(max_length=50)
    contact_guar = models.CharField(max_length=15)
    entry_time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    identity = models.FileField(upload_to="identities")

    def __str__(self):
        return(self.name)
    

PAYMENT_TYPE = [
    ("GP", "GPay"),
    ("PH", "Phone Pay"),
    ("PA", "Paytm"),
    ("CA", "Cash"),
    ("BT", "Bank Transfer"),
]

class Installment(models.Model):
    entry = models.ForeignKey(Entries, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    amount = models.PositiveIntegerField()
    date = models.DateField(default=date.today)
    pay_type = models.CharField(max_length=50, choices=PAYMENT_TYPE)

    def __str__(self):
        return(f'{self.entry.name} ({self.entry.id}) - {self.date}')

