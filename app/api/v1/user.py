from fastapi import APIRouter

router = APIRouter()
@router.get("*/user/*")
async def road_items():
    return[{"user_name": "Amath"}]
