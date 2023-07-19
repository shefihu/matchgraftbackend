from src.schemas.base import MatchGraftBaseModel


class CaseDetails(MatchGraftBaseModel):
    case_id: str
    created_at: str


class Case(CaseDetails):
    patient_pseudonym: str
    total_donors: int


class CasesResponse(MatchGraftBaseModel):
    cases: list[Case] | list
