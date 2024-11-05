import uuid
from django.conf import settings
from django.db import models


class Community(models.Model):
    """
    Model that represents a community
    """
    id = models.CharField(default=uuid.uuid4, primary_key=True)
    community_owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                                        on_delete=models.CASCADE,
                                        help_text="Owner of the community")
    name = models.CharField(max_length=50,
                            null=False,
                            blank=False,
                            help_text="Community name")
    description = models.TextField(max_length=250,
                                   null=False,
                                   blank=False,
                                   help_text="Community description")
    community_members = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                               related_name="members")
    created_at = models.DateTimeField(auto_now_add=True,
                                      editable=False,
                                      help_text="Date the community was create")

    class Meta:
        """
        Meta class for overriding default model behaviours
        """
        verbose_name = 'COMMUNITY'
        verbose_name_plural = 'COMMUNITIES'

    def __str__(self) -> str:
        return self.name
