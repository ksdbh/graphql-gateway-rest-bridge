import logging, uuid
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger("gql-gateway")
class CorrelationIdMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        corr_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
        response = await call_next(request)
        response.headers["X-Request-ID"] = corr_id
        logger.info("path=%s method=%s status=%s req_id=%s", request.url.path, request.method, response.status_code, corr_id)
        return response
