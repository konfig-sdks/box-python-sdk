# coding: utf-8

"""
    Box Platform API

    [Box Platform](https://box.dev) provides functionality to provide access to content stored within [Box](https://box.com). It provides endpoints for basic manipulation of files and folders, management of users within an enterprise, as well as more complex topics such as legal holds and retention policies.

    The version of the OpenAPI document: 2.0.0
    Contact: devrel@box.com
    Created by: https://box.dev
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from box_python_sdk import schemas  # noqa: F401


class SkillCardsMetadata(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The metadata assigned to a using for Box skills.
    """


    class MetaOapg:
        
        class properties:
            can_edit = schemas.BoolSchema
            
            
            class id(
                schemas.UUIDSchema
            ):
                pass
            parent = schemas.StrSchema
            scope = schemas.StrSchema
            template = schemas.StrSchema
            type = schemas.StrSchema
            type_version = schemas.IntSchema
            version = schemas.IntSchema
        
            @staticmethod
            def cards() -> typing.Type['SkillCardsMetadataCards']:
                return SkillCardsMetadataCards
            __annotations__ = {
                "$canEdit": can_edit,
                "$id": id,
                "$parent": parent,
                "$scope": scope,
                "$template": template,
                "$type": type,
                "$typeVersion": type_version,
                "$version": version,
                "cards": cards,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["$canEdit"]) -> MetaOapg.properties.can_edit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["$id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["$parent"]) -> MetaOapg.properties.parent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["$scope"]) -> MetaOapg.properties.scope: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["$template"]) -> MetaOapg.properties.template: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["$type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["$typeVersion"]) -> MetaOapg.properties.type_version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["$version"]) -> MetaOapg.properties.version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cards"]) -> 'SkillCardsMetadataCards': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["$canEdit", "$id", "$parent", "$scope", "$template", "$type", "$typeVersion", "$version", "cards", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["$canEdit"]) -> typing.Union[MetaOapg.properties.can_edit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["$id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["$parent"]) -> typing.Union[MetaOapg.properties.parent, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["$scope"]) -> typing.Union[MetaOapg.properties.scope, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["$template"]) -> typing.Union[MetaOapg.properties.template, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["$type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["$typeVersion"]) -> typing.Union[MetaOapg.properties.type_version, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["$version"]) -> typing.Union[MetaOapg.properties.version, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cards"]) -> typing.Union['SkillCardsMetadataCards', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["$canEdit", "$id", "$parent", "$scope", "$template", "$type", "$typeVersion", "$version", "cards", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        cards: typing.Union['SkillCardsMetadataCards', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SkillCardsMetadata':
        return super().__new__(
            cls,
            *args,
            cards=cards,
            _configuration=_configuration,
            **kwargs,
        )

from box_python_sdk.model.skill_cards_metadata_cards import SkillCardsMetadataCards
