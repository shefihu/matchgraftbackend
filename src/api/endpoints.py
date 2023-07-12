import fastapi

from src.api.routes.inference import router as inference_router
from src.api.routes.cases import router as cases_router

router = fastapi.APIRouter()

router.include_router(router=inference_router)
router.include_router(router=cases_router)
