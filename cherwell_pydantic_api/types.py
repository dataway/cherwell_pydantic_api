
import keyword
import re
from typing import Annotated, Any, AsyncIterable, Iterable, Literal, NewType, Optional, Union

from pydantic import GetCoreSchemaHandler
from pydantic_core import PydanticCustomError, core_schema



class _BaseStringType(str):
    @classmethod
    def _validate(cls, x: str, _: core_schema.ValidationInfo):
        return cls(x)

    @classmethod
    def __get_pydantic_core_schema__(cls, source: type[Any], handler: GetCoreSchemaHandler) -> core_schema.CoreSchema:
        return core_schema.general_after_validator_function(cls._validate, core_schema.str_schema())


class IDType(_BaseStringType):
    """A subtype of str with a constructor that converts identifiers to lower case.
    Non-hex characters will throw a ValueError."""
    def __new__(cls, x: str):
        x = x.lower()
        if not re.match(r'^[0-9a-f]+$', x):
            raise ValueError(f"Invalid IDString: {x}")
        return super().__new__(cls, x)

    @classmethod
    def _validate(cls, x: str, _: core_schema.ValidationInfo):
        try:
            return cls(x)
        except:
            raise PydanticCustomError('cherwell_api_idtype', 'invalid IDType')


class IdentifierType(_BaseStringType):
    """A subtype of str with a constructor that converts field names, etc. to a string
    that can be used as a Python identifier, except python keywords and fields that begin with a digit,
    in which case a prefix of I_ will be added (capitals)."""
    def __new__(cls, x: str):
        x = re.sub(r'[^0-9A-Za-z_]', '_', x)
        if x[0].isdigit() or x[0] == '_' or keyword.iskeyword(x):
            x = 'I_' + x
        return super().__new__(cls, x)


class LCIdentifierType(_BaseStringType):
    """A subtype of str with a constructor that converts field names, etc. to a _lowercase_ string
    that can be used as a Python identifier, except python keywords and fields that begin with a digit,
    in which case a prefix of I_ will be added (capitals)."""
    def __new__(cls, x: str):
        x = re.sub(r'[^0-9a-z_]', '_', x.lower())
        if x[0].isdigit() or x[0] == '_' or keyword.iskeyword(x):
            x = 'I_' + x
        return super().__new__(cls, x)


CherwellObjectID = dict[str, Any]
class BusObID(IDType):
    pass
class BusObRecID(IDType):
    pass
BusObIDParamType = BusObID
class BusObIdentifier(LCIdentifierType):
    pass
FieldID = NewType("FieldID", str)
class ShortFieldID(IDType):
    pass
class FieldIdentifier(IdentifierType):
    pass
class RelationshipID(IDType):
    pass
FileType = Union[str, bytes, Iterable[bytes], AsyncIterable[bytes]]
FileUpload = Annotated[FileType, "FileUpload"]
FileDownload = Annotated[FileType, "FileDownload"]
StringResponse = NewType("StringResponse", str)


BusinessObjectType = Literal["All", "Major", "Supporting", "Lookup", "Groups"]
RecordAttachmentType = Literal[
    "None",
    "File",
    "FileManagerFile",
    "BusOb",
    "History",
    "Other",
    "Solution",
    "UsedAsSolution",
    "ExternalSolution",
]
RecordAttachmentType.__doc__ = """Record attachment type:
        None - Not applicable to the REST API.
        File - Linked files.
        FileManagerFile - Imported files.
        BusOb - Attached Business Objects.
        History - Information about the attachment, if any is available. For example, an e-mail message may store the name of an attachment sent.
        Other - Not applicable to the REST API."""

AttachmentType = Literal["Imported", "Linked", "URL"]
AttachmentType.__doc__ = """For file types, select the type of attachment:
        Imported - Attachment was imported into database.
        Linked - Attachment is linked to an external file.
        URL - Attachment is a URL."""


class CherwellAPIError(Exception):
    extras: dict[str, Any]

    def __init__(self, msg: str = "Cherwell API error", *, errorCode: Optional[str] = None,
                 errorMessage: Optional[str] = None,
                 httpStatusCode: Optional[Any] = None,
                 **kwargs: Any):
        message = f"{msg}: {errorCode=} {errorMessage=} {httpStatusCode=}"
        self.errorCode = errorCode
        self.errorMessage = errorMessage
        self.httpStatusCode = httpStatusCode
        self.extras = kwargs
        super().__init__(message)


class SaveBusinessObjectError(CherwellAPIError):
    pass
