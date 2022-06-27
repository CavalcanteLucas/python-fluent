import setup
from Chap_20__Attribute_Descriptors.ex_20_6__model_v5 import (
    Quantity,
    NonBlank,
    Validated,
)


def entity(cls):
    for key, attr in cls.__dict__.items():
        if isinstance(attr, Validated):
            type_name = type(attr).__name__
            attr.storage_name = '_{}#{}'.format(type_name, key)
    return cls
