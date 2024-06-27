
from typing import Union

class HttpHandler:
  
  @staticmethod
  def success(code: int, message: str, data = None):

    status = HttpHandler.__httpStatus(code)

    if (code >= 300):
      return HttpHandler.error()
    
    return { "code": code, "status": status, "message": message, "data": data }
  
  @staticmethod
  def __httpStatus(code: int):
    if (code == 200):
      return "success"
    if (code == 404):
      return "notFound"
    if (code == 403):
      return "badRequest"
    
    return "internalError"
    
  @staticmethod
  def error(error):
    dictionaryError = HttpHandler.convertError(error.args)

    if isinstance(dictionaryError, dict):
      return HttpHandler.handleError(dictionaryError)

    return HttpHandler.defaultError()
  
  @staticmethod
  def defaultError():
    return { "code": 500, "message": "ocorreu um erro interno", "status": HttpHandler.__httpStatus(500) }
  
  @staticmethod
  def handleError(dictionaryError = dict): 

    code = dictionaryError.get("code", 500)
    
    return { 
      "code": code, 
      "message": dictionaryError.get("message"), 
      "status": HttpHandler.__httpStatus(code),
      "errors": dictionaryError.get("data") 
    }
    
  @staticmethod
  def convertError(arg):
  
    dictionary = dict()
    
    index = 0
    
    for elem in arg:
        print(index, elem)
        if index is 0:
          if not isinstance(elem, int):
            return None
          dictionary["code"] = elem
            
        if index is 1:
          if not isinstance(elem, str):
            return None
          dictionary["message"] = elem
            
        if index is 2:
            dictionary["data"] = elem

        index = index + 1

    if index > 3:
      return None
    
    return dictionary 

def customError(code: int, message: str, data = None):
  return Exception(code, message, data)

  