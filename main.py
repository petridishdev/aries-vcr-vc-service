import uvicorn
import json
from tests.data import credential_type_request

if __name__ == "__main__":
    print(json.dumps(credential_type_request, indent=2))
    uvicorn.run("app:app", host="0.0.0.0", port=8080, proxy_headers=True)
