from http import HTTPStatus

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from src.schemas.item import Item, CreateItem
from src.services.users import UserService

router_item_v1 = APIRouter(
    prefix="/v1/item", 
    tags=["Items"], 
    dependencies=[Depends(UserService().get_token_header)]
)


@router_item_v1.post(
    "/create", status_code=HTTPStatus.CREATED.value, response_model=CreateItem
)
async def create_item(item: Item) -> JSONResponse:
    user_created = await UserService().signup(item)
    return JSONResponse(user_created.dict(), status_code=HTTPStatus.CREATED.value)
