from datetime import datetime
from random import random

import fastapi

from fastapi.exceptions import HTTPException

from src.config import settings
from src.schemas.case import Case
from src.schemas.person import Patient, Donor
from src.schemas.inference import (
    MatchingInference,
    InferenceResult,
    SaveInferenceResponse,
    InferenceResultPayload,
)
from src.utils import store_json_data, format_datetime_to_iso
from storage.dummy.cases import case_list

router = fastapi.APIRouter(prefix="/case", tags=["Case"])


@router.post(
    "/inference",
    name="Inference:MatchPatientDonors",
    response_model=InferenceResult,
    status_code=fastapi.status.HTTP_201_CREATED,
)
async def match_patient_donors(
    patient_details: Patient = fastapi.Body(..., embed=True),
    donors_details: list[Donor] = fastapi.Body(..., embed=True),
) -> InferenceResult:
    result = list()
    try:
        store_json_data(
            file_path=settings.STORAGE_JSON["patients"],
            json_content=patient_details.model_dump(),
        )
        store_json_data(
            file_path=settings.STORAGE_JSON["donors"],
            json_content=[donor.model_dump() for donor in donors_details],
        )
        for donor in donors_details:
            matching_inference = MatchingInference(
                donor_pseudonym=donor.model_dump()["general"]["pseudonym"],
                grade2_plus=random(),
                grade3_plus=random(),
            )
            result.append(matching_inference)
    except Exception as err:
        raise HTTPException(status_code=fastapi.status.HTTP_400_BAD_REQUEST, detail=err)
    return InferenceResult(
        patient_pseudonym=patient_details.model_dump()["general"]["pseudonym"],
        result=result,
    )


@router.post(
    "/result",
    name="Inference:SaveResult",
    response_model=SaveInferenceResponse,
    status_code=fastapi.status.HTTP_201_CREATED,
)
async def save_result(
    inference_result_payload: InferenceResultPayload = fastapi.Body(..., embed=True),
) -> SaveInferenceResponse:
    try:
        case = Case(
            case_id=inference_result_payload.model_dump()["case_id"],
            patient_pseudonym=inference_result_payload.model_dump()[
                "patient_pseudonym"
            ],
            total_donors=len(inference_result_payload.model_dump()["result"]),
            created_at=format_datetime_to_iso(date_time=datetime.now()),
        )
        store_json_data(
            file_path=settings.STORAGE_JSON["cases"], json_content=case.model_dump()
        )
        case_list.append(case.model_dump())
        return SaveInferenceResponse(is_saved=True if case else False)
    except Exception as err:
        raise HTTPException(status_code=fastapi.status.HTTP_400_BAD_REQUEST, detail=err)
