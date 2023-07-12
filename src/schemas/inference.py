from src.schemas.base import MatchGraftBaseModel


class MatchingInference(MatchGraftBaseModel):
    donor_pseudonym: str
    grade2_plus: float
    grade3_plus: float


class InferenceResultPayload(MatchGraftBaseModel):
    case_id: str
    patient_pseudonym: str
    result: list[MatchingInference]


class InferenceResult(MatchGraftBaseModel):
    patient_pseudonym: str
    result: list[MatchingInference]


class SaveInferenceResponse(MatchGraftBaseModel):
    is_saved: bool
