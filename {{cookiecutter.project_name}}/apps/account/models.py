from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _

from core.models.user import AbstractUser


class User(AbstractUser):
    """User model
    phone number is required and must be unique
    role represent that's for example user is developer or project manager or etc
    skill represents that's which related role-skill user has
    if user phone number has been changed the is_phone_number_approve change to False
    this model has two cached properties for bio and wallet that's related to user instance
    """


    ICON: str = "Person"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")


    @cached_property
    def full_name(self):
        return self.get_full_name()

    full_name.short_description = _("full name")
