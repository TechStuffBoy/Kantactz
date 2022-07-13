from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Contact(models.Model):
    class Meta:
        verbose_name_plural = 'Contacts'
        ordering = ('-updated_at', )

    number = models.CharField('Number', max_length=10)
    country_code = models.CharField('Country Code', max_length=4)
    email = models.EmailField(
        "Personal Email",
        blank=False,  # Form will expect some value
        null=False,  # Cant be null in DB
        help_text="Please enter your email.",
        max_length=254,
    )
    email2 = models.EmailField(
        "Business Email",
        blank=True,
        null=True,
        help_text="Please enter your Business email.",
        max_length=254,
    )
    creator = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='contacts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<id={self.pk} | +{self.country_code}-{self.number}>"