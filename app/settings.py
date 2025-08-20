from pydantic import BaseModel
import os
class Settings(BaseModel):
    app_name: str = "graphql-gateway"
    jwt_secret: str = os.getenv("JWT_SECRET", "change-me")
    rest_base_url: str = "https://jsonplaceholder.typicode.com"
    timeout_seconds: int = 5
settings = Settings()
