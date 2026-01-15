import time
import logging

logger = logging.getLogger(__name__)

class RequestLogMiddleware:
    """Muestra el tiempo de ejecución de cada request."""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()
        response = self.get_response(request)
        elapsed = time.time() - start
        logger.info(f"{request.method} {request.path} ({elapsed:.2f}s)")
        return response
