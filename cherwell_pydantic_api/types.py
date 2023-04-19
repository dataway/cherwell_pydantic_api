import keyword
import re
from typing import TYPE_CHECKING, Annotated, Any, AsyncIterable, Iterable, Literal, NewType, Optional, Union



# TODO: There must be a better solution here
if TYPE_CHECKING:
    IDType = NewType
    IdentifierType = NewType
    LCIdentifierType = NewType
else:
    def IDType(name, tp):
        """Create a subtype of str with a constructor that converts identifiers to lower case. Non-hex characters
        will throw a ValidError. For the type checker it is the same as NewType"""
        def id_type(x):
            x = x.lower()
            if not re.match(r'^[0-9a-f]+$', x):
                raise ValueError(f"Invalid {name}: {x}")
            return x
        id_type.__name__ = name
        id_type.__supertype__ = tp
        return id_type

    def IdentifierType(name, tp):
        """Create a subtype of str with a constructor that converts field names, etc. to a string
        that can be used as a Python identifier, except python keywords and fields that begin with a digit,
        in which case a prefix of I_ will be added (capitals). For the type checker it is the same as NewType"""
        def identifier_type(x):
            x = re.sub(r'[^0-9A-Za-z_]', '_', x)
            if x[0].isdigit() or x[0] == '_' or keyword.iskeyword(x):
                x = 'I_' + x
            return x
        identifier_type.__name__ = name
        identifier_type.__supertype__ = tp
        return identifier_type

    def LCIdentifierType(name, tp):
        """Create a subtype of str with a constructor that converts field names, etc. to a _lowercase_ string
        that can be used as a Python identifier, except python keywords and fields that begin with a digit,
        in which case a prefix of I_ will be added (capitals). For the type checker it is the same as NewType"""
        def identifier_type(x):
            x = re.sub(r'[^0-9a-z_]', '_', x.lower())
            if x[0].isdigit() or x[0] == '_' or keyword.iskeyword(x):
                x = 'I_' + x
            return x
        identifier_type.__name__ = name
        identifier_type.__supertype__ = tp
        return identifier_type


CherwellObjectID = dict[str, Any]
BusObID = IDType("BusObID", str)
BusObRecID = IDType("BusObRecID", str)
BusObIDParamType = BusObID
BusObIdentifier = LCIdentifierType("BusObIdentifier", str)
FieldID = NewType("FieldID", str)
ShortFieldID = IDType("ShortFieldID", str)
FieldIdentifier = IdentifierType("FieldIdentifier", str)
RelationshipID = IDType("RelationshipID", str)
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
