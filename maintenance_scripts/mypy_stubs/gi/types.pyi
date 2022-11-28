from typing import Any
# from ._constants import TYPE_INVALID as TYPE_INVALID
# from ._gi import GInterface as GInterface, InterfaceInfo as InterfaceInfo, ObjectInfo as ObjectInfo, StructInfo as StructInfo, VFuncInfo as VFuncInfo, hook_up_vfunc_implementation as hook_up_vfunc_implementation, register_interface_info as register_interface_info
# from .docstring import generate_doc_string as generate_doc_string

# def snake_case(name): ...

class MetaClassHelper: ...

# def find_vfunc_info_in_interface(bases, vfunc_name): ...
# def find_vfunc_conflict_in_bases(vfunc, bases): ...

class _GObjectMetaBase(type):
    def __init__(cls, name: str, bases: tuple[type, ...], dict_: dict[str, Any]) -> None: ...

class GObjectMeta(_GObjectMetaBase, MetaClassHelper):
    def __init__(cls, name: str, bases: tuple[type, ...], dict_: dict[str, Any]) -> None: ...
    def mro(cls): ...
    @property
    def __doc__(cls): ...

# def mro(C): ...
# def nothing(*args, **kwargs) -> None: ...

# class StructMeta(type, MetaClassHelper):
#     def __init__(cls, name, bases, dict_) -> None: ...
#     @property
#     def __doc__(cls): ...
