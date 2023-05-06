class ResponseInfo:
    schema = {"type": "object",
              "properties": {
                  "createdTime": {"type": "string"},
                  "size": {"type": "string"}},
              "required": ["createdTime",  "size"]
              }
