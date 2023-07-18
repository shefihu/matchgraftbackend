from typing import Literal

from src.schemas.base import MatchGraftBaseModel
from src.schemas.info import (
    General,
    DiseaseStatus,
    HLATypes,
    InfectionStatus,
    EASIXScore,
)


class Patient(MatchGraftBaseModel):
    general: General
    disease_status: DiseaseStatus
    hla_types: HLATypes
    infection_status: InfectionStatus
    easix_score: EASIXScore


class DonorGeneral(General):
    donor_relation: Literal["Unrelated", "Related-Sibling", "Related-Non-Sibling"]


class DonorHLATypes(HLATypes):
    ab0_compatibility: Literal[
        "Full-Compatibility",
        "Minor-Compatibility",
        "Major-Compatibility",
        "Bidirectional-Incompatibility",
    ]


class Donor(MatchGraftBaseModel):
    general: DonorGeneral
    hla_types: DonorHLATypes
    infection_status: InfectionStatus
    easix_score: EASIXScore
