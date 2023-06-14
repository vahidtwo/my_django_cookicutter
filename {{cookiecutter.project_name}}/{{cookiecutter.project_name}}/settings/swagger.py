SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {
        "Basic": {"type": "basic"},
        "Token": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": 'Add word "Token " before your token value',
        },
    }
}