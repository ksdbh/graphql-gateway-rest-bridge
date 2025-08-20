import strawberry
from typing import Optional, List
from . import rest_clients
@strawberry.type
class User:
    id: int
    name: str
@strawberry.type
class Post:
    id: int
    title: str
    body: str
    userId: int
    @strawberry.field
    async def author(self) -> Optional[User]:
        data = await rest_clients.get_user(self.userId)
        return User(id=data["id"], name=data["name"])
@strawberry.type
class Query:
    @strawberry.field
    async def health(self) -> str:
        return "ok"
    @strawberry.field
    async def post(self, id: int) -> Optional[Post]:
        data = await rest_clients.get_post(id)
        return Post(**data)
    @strawberry.field
    async def posts(self, limit: int = 5) -> List[Post]:
        items = await rest_clients.list_posts(limit)
        return [Post(**it) for it in items]
schema = strawberry.Schema(query=Query)
