#json-схема для ответа с кодом ошибки 404
class ResponseError404:
    schema = {"error": {
        "code": 404,
        "errors": [
          {
            "domain": "global",
            "location": "fileId",
            "locationType": "parameter",
            "message": "File not found: .",
            "reason": "notFound"
          }
        ],
        "message": "File not found: ."
      },
        "required": ["error"]
    }

#json-схема для ответа с кодом ошибки 403
class ResponseError403:
    schema = {"error": {
        "code": 403,
        "errors": [
          {
            "domain": "global",
            "message": "The request is missing a valid API key.",
            "reason": "forbidden"
          }
        ],
        "message": "The request is missing a valid API key.",
        "status": "PERMISSION_DENIED"
      },
        "required": ["error"]
    }
