from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Message(models.Model):
    STATUS = (
        ('S', _('Sent')),
        ('R', _('Received')),
    )
    BOX = (
        ('I', _('InBox')),
        ('A', _('ArchiveBox')),
        ('D', _('DeleteBox')),
    )

    class Meta:
        permissions = [
            ['view_message', 'Can view message', ]
        ]
        # unique_together = ((),)

    thread = models.ForeignKey('self', blank=True, null=True)
    sender = models.ForeignKey(User, related_name='senders')
    receiver = models.ForeignKey(User, related_name='receivers')
    content = models.TextField(max_length=2000)
    status = models.CharField(max_length=1, default='S', choices=STATUS, blank=False)
    box = models.CharField(max_length=1, default='I', choices=BOX, blank=False)
    send_time = models.DateTimeField(default=timezone.now)
    receive_time = models.DateTimeField(blank=True, null=True)
    archive_time = models.DateTimeField(blank=True, null=True)
    delete_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "{}: {}->{}".format(self.id, self.sender, self.receiver)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('messagebox:message.list')