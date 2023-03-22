from typing import Annotated, Any, AsyncIterable, Iterable, Literal, NewType, Union



CherwellObjectID = dict[str, Any]
BusObID = NewType("BusObID", str)
BusObRecID = NewType("BusObRecID", str)
BusObIDParamType = BusObID
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
