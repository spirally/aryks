from django.db import models
from django.db.models import Q
from django.db.models.query import QuerySet
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


__all__ = (
    'IsDeletedManager',
    'IsDeletedRestoredManager',
    'IsDeletedModel',
    'IsDeletedRestoredModel'
)


class IsDeletedQuerySet(QuerySet):
    def delete(self):
        self.update(deleted=timezone.now())


class IsDeletedRestoredQuerySet(IsDeletedQuerySet):
    def restore(self):
        self.update(deleted=None)


class IsDeletedManager(models.Manager):
    def _get_query_set(self):
        return IsDeletedQuerySet(self.model, using=self._db)

    def get_queryset(self):
        return self._get_query_set().filter(deleted=None)

    def get_all(self):
        return self._get_query_set()

    def deleted(self):
        return self._get_query_set().filter(~Q(deleted=None))


class IsChildDeletedManager(models.Manager):
    def _get_query_set(self):
        return IsDeletedQuerySet(self.model, using=self._db)

    def get_queryset(self):
        return self._get_query_set().filter(deleted=None, child_deleted=None)

    def get_all(self):
        return self._get_query_set()

    def deleted(self):
        return self._get_query_set().filter(~Q(deleted=None) | ~Q(child_deleted=None))


class IsDeletedRestoredManager(IsDeletedManager):
    def _get_query_set(self):
        return IsDeletedRestoredQuerySet(self.model, using=self._db)


class IsDeletedModel(models.Model):

    deleted = models.DateTimeField(null=True, editable=False, verbose_name=_('Удалено'))

    objects = IsDeletedManager()

    class Meta:
        abstract = True

    def delete(self, using=None):
        self.deleted = timezone.now()

        self.save(using=using)


class IsDeletedRestoredModel(IsDeletedModel):
    objects = IsDeletedRestoredManager()

    class Meta:
        abstract = True

    def restore(self, using=None):
        self.deleted = None

        self.save(using=using)


class ExcludeTypeManager(models.Manager):

    def get_queryset(self):
        qs = super(ExcludeTypeManager, self).get_queryset()
        extra = {}
        for sub in self.model.__subclasses__():
            if hasattr(sub, "exclude_from_base_queryset"):
                extra["%s__isnull" % sub.__name__.lower()] = False
        if extra:
            qs = qs.exclude(**extra)
        return qs

    def get_all(self):
        return super(ExcludeTypeManager, self).get_queryset()


class ExcludeTypeIsDeletedManager(ExcludeTypeManager, IsDeletedManager):
    pass


def exclude_from_base_queryset(model):
    model.exclude_from_base_queryset = True
    return model
