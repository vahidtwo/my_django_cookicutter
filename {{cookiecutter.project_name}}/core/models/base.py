import jdatetime
from django.core.cache import cache
from django.db import models
from django.forms.utils import to_current_timezone
from django.utils.text import camel_case_to_spaces
from django.utils.translation import gettext_lazy as _

from core.http import get_client_ip


def datetime2jalali(g_date):
    if g_date is None:
        return None

    g_date = to_current_timezone(g_date)
    jdatetime.set_locale("fa_IR")
    return jdatetime.datetime.fromgregorian(datetime=g_date)


class CustomForeignKey(models.ForeignKey):
    """
    Custom ForeginKey
    custom foreginkey for created_by and created_at
    auto set related names
    """

    def contribute_to_class(self, cls, *args, **kwargs):
        super().contribute_to_class(cls, *args, **kwargs)
        related_name = self.remote_field.related_name
        if not cls._meta.abstract and related_name:
            underscore_name = camel_case_to_spaces(cls.__name__).replace(" ", "_")
            self.remote_field.related_name = related_name.format(underscore_name=underscore_name)


class BaseModel(models.Model):
    """
    Base Model
    methods:
        - jalali_created_at: returns jalali format of created_at attr
    """

    # created_by = CustomForeignKey(
    #     null=True,
    #     to=get_user_model(),
    #     on_delete=models.CASCADE,
    #     editable=False,
    #     related_name="created_{underscore_name}",
    #     verbose_name=_("created by")
    # )
    # updated_by = CustomForeignKey(
    #     null=True,
    #     to=get_user_model(),
    #     on_delete=models.CASCADE,
    #     related_name="updated_{underscore_name}",
    #     verbose_name=_("updated by")
    # )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated at"))
    is_active = models.BooleanField(verbose_name=_("is active"), default=True)

    class Meta:
        abstract = True

    def __str__(self):
        if hasattr(self, "title"):
            return str(self.title)

        return "%s (%s)" % (self._meta.verbose_name, self.id)

    def jalali_created_at(self):
        """
        returns jalali format of created_at attr
        """
        return datetime2jalali(self.created_at)

    jalali_created_at.short_description = _("created_at")

    jalali_created_at = property(jalali_created_at)

    @property
    def seo_object(self):
        if hasattr(self, "seo"):
            return self.seo.last()

    @property
    def formated_jalali_date(self):
        return self.jalali_created_at.strftime("%d %b %Y")


class AnalyticsBaseModel(models.Model):
    """
    Analytics Base Model
    methods:
        - sey_view: plus view to object and cache ip and object_id with action in memcache for 10 minutes
        - set_like: plus like to object and cache ip and object_id with action in memcache for 60 minutes
        - set_dislike: plus dislike in object and cache ip and object_id with action in memcache for 60 minutes
    """

    view_count = models.IntegerField(_("view count"), default=0, blank=True)
    like_count = models.IntegerField(_("like count"), default=0, blank=True)
    dislike_count = models.IntegerField(_("dislike count"), default=0, blank=True)
    play_count = models.IntegerField(
        _("play count"),
        default=0,
        blank=True,
    )

    class Meta:
        abstract = True

    @property
    def _key(self):
        """
        Returns cached key
        """
        return "%s_%s_%s" % (self._meta.app_label, self._meta.model_name, self.id)

    def set_view(self, request, force=False):
        # set view per ip
        ip = get_client_ip(request)
        key = "av_%s_%s" % (self._key, ip)
        if force or not cache.get(key):
            # its force or cache is not set
            self.view_count += 1
            self.save()
            cache.set(key, True, 60 * 10)
            return True

        return False

    def set_play(self, request, force=False):
        # set view per ip
        ip = get_client_ip(request)
        key = "ap_%s_%s" % (self._key, ip)
        if force or not cache.get(key):
            # its force or cache is not set
            self.play_count += 1
            self.save()
            cache.set(key, True, 60 * 10)
            return True

        return False

    def set_like(self, request, force=False):
        # set like per ip
        ip = get_client_ip(request)
        key = "al_%s_%s" % (self._key, ip)
        if force or not cache.get(key):
            # its force or cache is not set
            self.like_count += 1
            self.save()
            cache.set(key, True, 60 * 60)
            return True

        return False

    def set_dislike(self, request, force=False):
        # set dislike per ip
        ip = get_client_ip(request)
        key = "dl_%s_%s" % (self._key, ip)
        if force or not cache.get(key):
            # its force or cache is not set
            self.dislike_count += 1
            self.save()
            cache.set(key, True, 60 * 60)
            return True

        return False
