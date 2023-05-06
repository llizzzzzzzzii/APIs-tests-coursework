from com.jsonschema.file import FileResponse

class ResponseSearchFile:
    schema = {
        "nextPageToken": {"type": "string"},
        "kind": {"type": "string"},
        "incompleteSearch": {"type": "boolean"},
        "files": {"type": "array",
                  "items": str(FileResponse.schema)},
        "required": ["kind", "incompleteSearch"]
    }

class ResponseSearchFolder:
    schema = {
        "nextPageToken": {"type": "string"},
        "files": {"type": "array",
                  "items": {"type": "string"}},
    }
