from django.db import models
from django.contrib.auth.models import User
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
        pass

    thread = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name='senders', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='receivers', on_delete=models.CASCADE)
    content = models.TextField(max_length=2000)
    status = models.CharField(max_length=1, default='S', choices=STATUS, blank=False)
    box = models.CharField(max_length=1, default='I', choices=BOX, blank=False)
    send_time = models.DateTimeField(auto_now_add=True)
    receive_time = models.DateTimeField(blank=True, null=True)
    archive_time = models.DateTimeField(blank=True, null=True)
    delete_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "{}: {}->{}".format(self.id, self.sender, self.receiver)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('messagebox:message.list')
