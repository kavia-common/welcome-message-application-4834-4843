# Welcome Backend

A FastAPI backend that serves a welcome message and basic health check. CORS is enabled for all origins to allow the frontend to access the API during development.

## Run Instructions

Start the server with uvicorn:

```bash
uvicorn src.api.main:app --host 0.0.0.0 --port 3001
```

- Host: 0.0.0.0 (listens on all interfaces)
- Port: 3001
- App path: src.api.main:app

Once running:
- OpenAPI/Swagger UI: http://localhost:3001/docs
- OpenAPI JSON: http://localhost:3001/openapi.json

## Endpoints

- GET `/` — Health Check
  - Summary: Health Check
  - Returns: `{ "message": "Healthy" }`

- GET `/api/welcome` — Get Welcome Message
  - Summary: Returns a JSON object containing the welcome greeting.
  - Response shape:
    ```json
    {
      "message": "Welcome"
    }
    ```

## CORS

CORS is enabled for all origins via FastAPI's CORSMiddleware:

- allow_origins: ["*"]
- allow_methods: ["*"]
- allow_headers: ["*"]
- allow_credentials: true

Note: For production, you should restrict `allow_origins` to known frontend URLs using environment variables or a configuration file.

## Development Notes

- Requirements are listed in `requirements.txt`. Install with:
  ```bash
  pip install -r requirements.txt
  ```
- To regenerate the OpenAPI spec in `welcome_backend/interfaces/openapi.json`, you can run the app and fetch `/openapi.json` or execute the helper script:
  ```bash
  python -m src.api.generate_openapi
  ```
