from datetime import date
from http import HTTPStatus

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from src.schemas.item import CreatedItem, Item, Items
from src.schemas.user import UserCreated
from src.services.items import ItemService
from src.services.users import UserService

router_item_v1 = APIRouter(prefix="/v1/items", tags=["Items"])


@router_item_v1.post(
    "/create", status_code=HTTPStatus.CREATED.value, response_model=CreatedItem
)
async def create_item(
    item: Item, user: UserCreated = Depends(UserService().get_token_header)
) -> JSONResponse:
    item_created = await ItemService().create_item(item, user)
    return JSONResponse(item_created.dict(), status_code=HTTPStatus.CREATED.value)


@router_item_v1.get("/search", status_code=HTTPStatus.OK.value, response_model=Items)
async def get_items(
    date: date | None = None,
    user: UserCreated = Depends(UserService().get_token_header),
) -> JSONResponse:
    item_created = await ItemService().get_items(user, date)
    return JSONResponse(item_created.dict(), status_code=HTTPStatus.OK.value)
