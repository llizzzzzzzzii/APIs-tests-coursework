from com.jsonschema.file import FileResponse

#json-схема для ответа на запрос поиска файла
class ResponseSearchFile:
    schema = {
        "nextPageToken": {"type": "string"},
        "kind": {"type": "string"},
        "incompleteSearch": {"type": "boolean"},
        "files": {"type": "array",
                  "items": str(FileResponse.schema)},
        "required": ["kind", "incompleteSearch"]
    }

#json-схема для ответа на запрос поиска папки
class ResponseSearchFolder:
    schema = {
        "nextPageToken": {"type": "string"},
        "files": {"type": "array",
                  "items": {"type": "string"}},
    }
