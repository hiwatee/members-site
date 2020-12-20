from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator

from .base import BaseModel


class Registration(BaseModel):
    # user = fields.ForeignKeyField(
    #     "models.User", related_name="users")
    department = fields.CharField(max_length=100, null=True)
    position = fields.CharField(max_length=100, null=True)
    portrait = fields.CharField(max_length=1000, null=True)
    profile = fields.TextField(null=True)
    birth = fields.DateField(null=True)


Registration_Pydantic = pydantic_model_creator(
    Registration, name="Registration", exclude=("deleted_at",))
RegistrationIn_Pydantic = pydantic_model_creator(Registration, name="RegistrationIn", include=(
    "department",
    "position",
    "portrait",
    "profile",
    "birth"
), exclude_readonly=True)
