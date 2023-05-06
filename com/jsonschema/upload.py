class ResponseUpload:
    schema = {"type": "object",
              "properties": {
                  "kind": {"type": "string"},
                  "mimeType": {"type": "string"},
                  "id": {"type": "string"},
                  "name": {"type": "string"}},
              "required": ["kind", "mimeType", "id",  "name"]
              }
