from django.http import JsonResponse
import logging
from django.contrib.auth.models import User

logger = logging.getLogger(__name__)


def index(request):
    logger.info("Testing the logger")

    try:
        User.objects.get(pk=1)
    except User.DoesNotExist:
        logger.error("User with Id %s does not exist.", 1)

    return JsonResponse({"msg": "Some context"})
