import setup
from Chap_20__Attribute_Descriptors.ex_20_6__model_v5 import (
    Quantity,
    NonBlank,
    Validated,
)


class EntityMeta(type):
    """Metaclass for business entities with validated fields"""

    def __init__(cls, name, bases, attr_dict):
        super().__init__(name, bases, attr_dict)
        for key, attr in attr_dict.items():
            if isinstance(attr, Validated):
                type_name = type(attr).__name__
                attr.storage_name = '_{}#{}'.format(type_name, key)


class Entity(metaclass=EntityMeta):
    """Business entity with validated fields"""
