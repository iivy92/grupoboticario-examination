from http import HTTPStatus

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from src.schemas.item import Item, CreatedItem
from src.schemas.user import UserCreated
from src.services.users import UserService
from src.services.items import ItemService

router_item_v1 = APIRouter(
    prefix="/v1/item", 
    tags=["Items"]
)


@router_item_v1.post(
    "/create", status_code=HTTPStatus.CREATED.value, response_model=CreatedItem
)
async def create_item(item: Item, user: UserCreated = Depends(UserService().get_token_header)) -> JSONResponse:
    item_created = await ItemService().create_item(item, user)
    return JSONResponse(item_created.dict(), status_code=HTTPStatus.CREATED.value)
