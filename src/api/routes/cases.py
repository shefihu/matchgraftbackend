import fastapi

from fastapi.responses import JSONResponse

from src.config import settings
from src.schemas.case import Case, CasesResponse
from src.utils import retrieve_json_data

router = fastapi.APIRouter(prefix="/cases", tags=["Cases"])

@router.get(
    "",
    name="Cases:RetrieveCases",
    response_model=CasesResponse,
    status_code=fastapi.status.HTTP_200_OK
)
async def retrieve_cases() -> CasesResponse:
    case = retrieve_json_data(file_path=settings.STORAGE_JSON["cases"])
    print(case)
    if not case:
        return CasesResponse(cases=[])
    cases = Case(**case)
    return CasesResponse(cases=[cases])
