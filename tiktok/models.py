from django.db import models

class TikTokProfile(models.Model):
    username = models.CharField(max_length=100)
    video_types = models.CharField(max_length=255, help_text="e.g., funny, gaming, beauty, etc.")
    followers_count = models.PositiveIntegerField()
    gets_engagement = models.CharField(help_text="Yes or No")
    
    PREFERRED_PAYMENT_CHOICES = [
        ('bank', 'Bank Transfer'),
        ('gopay', 'GoPay'),
        ('ovo', 'OVO'),
        ('dana', 'DANA'),
        ('linkaja', 'LinkAja'),
    ]
    preferred_payment_method = models.CharField(max_length=10, choices=PREFERRED_PAYMENT_CHOICES)
    preferred_currency = models.CharField(max_length=10)

    # Bank details
    bank_account_name = models.CharField(max_length=255)
    bank_name = models.CharField(max_length=255)
    bank_account_number = models.CharField(max_length=50)
    bank_branch = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    
    taxpayer_id = models.CharField(max_length=20, blank=True, null=True, verbose_name="NPWP (Taxpayer ID)")

    def __str__(self):
        return self.username
