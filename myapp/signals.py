from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
import logging
from django.contrib.auth import get_user_model

logger = logging.getLogger(__name__)

@receiver(pre_save, sender=get_user_model())
def user_pre_save(sender, instance, **kwargs):
    instance.username = instance.username.lower()


@receiver(post_save, sender=get_user_model())
def log_user_saved(sender, instance, created, **kwargs):
    if created:
        logger.info(f"New user created: {instance.username}")
    else:
        logger.info(f"Profile updated for user: {instance.username}")


@receiver(post_delete, sender=get_user_model())
def log_user_deleted(sender, instance, **kwargs):
    logger.warning(f'A user deleted: {instance.username}')

