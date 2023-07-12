from typing import Literal

from src.schemas.base import MatchGraftBaseModel


class General(MatchGraftBaseModel):
    pseudonym: str
    age: str
    is_male: bool
    is_prior_autologous_transplant: bool


class DiseaseStatus(MatchGraftBaseModel):
    underlying_disease: str | None
    is_malignant: bool
    remission: Literal[
        "No - Remission",
        "Partial - Remission",
        "Complete - Remission",
        "Not Applicable"
    ]
    relapse_count: int | float


class HLATypes(MatchGraftBaseModel):
    hla_a1: str
    hla_a2: str
    hla_b1: str
    hla_b2: str
    hla_c1: str
    hla_c2: str
    hla_drb11: str
    hla_drb12: str
    hla_dqa11: str
    hla_dqa12: str
    hla_dqb11: str
    hla_dqb12: str
    hla_dpa11: str
    hla_dpa12: str
    hla_dpb11: str
    hla_dpb12: str


class InfectionStatus(MatchGraftBaseModel):
    is_cmv: bool
    is_ebv: bool
    is_hhv6_igg: bool
    is_hhv6_dna: bool


class EASIXScore(MatchGraftBaseModel):
    creatinine: int | float
    ldh: int | float
    thrombocytes: int | float
