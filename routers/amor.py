from fastapi import APIRouter

amor_router = APIRouter()

@amor_router.get('/')
def message():
    return {'amor':'te amo mucho mucho. Sos la mejor del mundo entero'}