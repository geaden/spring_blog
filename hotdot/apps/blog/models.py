import datetime
from django.utils import timezone
from django.db import models
from django.utils.translation \
    import ugettext_lazy as _
from django.urls import reverse

# Create your models here.
from ..core.models import TimeStampedModel


class Post(TimeStampedModel):
    """
    Just example of model
    """
    title = models.CharField(_('Title'), max_length=100)
    content = models.TextField(_('Content'))
    pub_date = models.DateTimeField(verbose_name=_('Date published'),
                                    default=timezone.now())
    is_draft = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('blog:detail',
                       args=[self.pk])

    class Meta:
        ordering = ['-pub_date']

    def __unicode__(self):
        return self.title
