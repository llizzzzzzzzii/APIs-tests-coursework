#json-схема для ответа для запроса на получение даты и времени файла
class ResponseInfo:
    schema = {"type": "object",
              "properties": {
                  "createdTime": {"type": "string"},
                  "size": {"type": "string"}},
              "required": ["createdTime",  "size"]
              }
