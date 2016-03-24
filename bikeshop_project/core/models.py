from django.db import models
from django.utils import timezone


class Membership(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    renewed_at = models.DateTimeField(default=timezone.now)
    member = models.OneToOneField(
        'registration.Member',
        on_delete=models.CASCADE,
        related_name='membership'
    )
    safe_space = models.BooleanField(default=False)
    community = models.BooleanField(default=False)
    space = models.BooleanField(default=False)
    give_back = models.BooleanField(default=False)
    # this should be a form field that requires the new member to type out there full name
    acknowledgement = models.BooleanField(default=False)


class Payment(models.Model):
    membership = models.ForeignKey(
        'Membership',
        on_delete=models.CASCADE,
    )
    payment_choices = (
        ('CASH', 'cash'),
        ('CHEQUE', 'cheque'),
        ('VOLUNTEERING', 'volunteering'),
        ('STRIPE', 'stripe'),
        ('PAYPAL', 'paypal')
    )
    type = models.CharField(max_length=12, choices=payment_choices)
    created_at = models.DateTimeField(auto_now_add=True)


class Visit(models.Model):
    visit_choices = (
        ('VOLUNTEER', 'volunteer'),
        ('WORK', 'work on bike'),
        ('WORKSHOP', 'workshop')
    )
    member = models.ForeignKey(
        'registration.Member',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    purpose = models.CharField(max_length=50, choices=visit_choices)