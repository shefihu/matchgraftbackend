from pydantic import BaseModel, ConfigDict

from src.utils import snake_to_camel


class MatchGraftBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment=True,
        populate_by_name=True,
        alias_generator=snake_to_camel
    )
