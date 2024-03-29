from typing import Literal

from src.schemas.base import MatchGraftBaseModel


class General(MatchGraftBaseModel):
    pseudonym: str
    age: str
    is_male: bool | None
    is_prior_autologous_transplant: bool | None
    blood_group: Literal["A", "B", "O", "AB"]


class DiseaseStatus(MatchGraftBaseModel):
    underlying_disease: str | None
    is_malignant: bool | None
    remission: Literal[
        "No - Remission",
        "Partial - Remission",
        "Complete - Remission",
        "Not Applicable",
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
    is_cmv: bool | None
    is_ebv: bool | None
    is_hhv6_igg: bool | None
    is_hhv6_dna: bool | None


class EASIXScore(MatchGraftBaseModel):
    creatinine: int | float
    creatinine_unit: Literal[
        "mmol/l", "μmol/l", "mg/dl", "mg/100ml", "mg%", "mg/l", "μg/ml"
    ]
    ldh: int | float
    ldh_unit: Literal[
        "nkat/l",
        "μkat/l",
        "nmol/(s•L)",
        "μmol/(s•L)",
        "U/L",
        "IU/L",
        "μmol/(min•L)",
        "μmol/(h•L)",
        "μmol/(h•mL)",
    ]
    thrombocytes: int | float
    thrombocytes_unit: Literal[
        "10^9/L",
        "G/L",
        "Gpt/L",
        "cells/L",
        "10^3/μL",
        "1000/μL",
        "10^3/mm^3",
        "1000/mm^3",
        "K/μL",
        "K/mm^3",
        "cells/μL",
        "cells/mm^3",
    ]
