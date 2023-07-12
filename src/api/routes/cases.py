import fastapi


from src.config import settings
from src.schemas.case import Case, CasesResponse
from src.utils import retrieve_json_data
from storage.dummy.cases import case_list

router = fastapi.APIRouter(prefix="/cases", tags=["Cases"])


@router.get(
    "",
    name="Cases:RetrieveCases",
    response_model=CasesResponse,
    status_code=fastapi.status.HTTP_200_OK,
)
async def retrieve_cases() -> CasesResponse:
    # case = retrieve_json_data(file_path=settings.STORAGE_JSON["cases"])
    cases = [Case(**case) for case in case_list]
    return CasesResponse(cases=cases)
