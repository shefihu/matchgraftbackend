from datetime import datetime

from src.schemas.base import MatchGraftBaseModel
from src.utils import format_datetime_to_iso


class CaseDetails(MatchGraftBaseModel):
    case_id: str
    created_at: str = format_datetime_to_iso(date_time=datetime.now())


class Case(CaseDetails):
    patient_pseudonym: str
    total_donors: int


class CasesResponse(MatchGraftBaseModel):
    cases: list[Case] | list
