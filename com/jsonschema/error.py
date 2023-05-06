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
      }
    }
