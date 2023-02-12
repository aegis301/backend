def ResponseModel(data, message, headers):
    """Response model for API responses"""
    return {
        "payload": data,
        "code": 200,
        "message": message,
        "headers": headers,
    }


def ErrorResponseModel(error, code, message):
    """Error response model for API responses"""
    return {"error": error, "code": code, "message": message}
