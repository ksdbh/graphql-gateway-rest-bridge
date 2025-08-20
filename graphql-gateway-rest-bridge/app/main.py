from fastapi import FastAPI, Request
from strawberry.fastapi import GraphQLRouter
from .schema import schema
from .observability import CorrelationIdMiddleware
app = FastAPI(title="GraphQL Gateway")
app.include_router(GraphQLRouter(schema), prefix="/graphql")
app.add_api_route("/health", lambda: {"status": "ok"}, methods=["GET"])
app.add_middleware(CorrelationIdMiddleware)
@app.middleware("http")
async def add_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers.setdefault("X-Content-Type-Options", "nosniff")
    response.headers.setdefault("X-Frame-Options", "DENY")
    return response
