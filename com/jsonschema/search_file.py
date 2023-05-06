from com.jsonschema.upload import ResponseUpload

class Response_search_files:
    schema = {
        "nextPageToken": {"type": "string"},
        "kind": {"type": "string"},
        "incompleteSearch": {"type": "boolean"},
        "files": {"type": "array",
                  "items": str(ResponseUpload.schema)},
        "required": ["kind", "incompleteSearch"]
    }
