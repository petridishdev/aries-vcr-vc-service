"""Service to call Aries VCR API."""

from httpx import AsyncClient


async def register_credential_type(credential_type):
    """Register a new credential type"""

    # Make an HTTP request to the Aries VCR API
    async with AsyncClient(
        base_url="http://host.docker.internal:8008/agentcb/topic"
    ) as client:
        response = await client.post("/vc_di_credential_type/", json=credential_type)
        response.raise_for_status()
        return response.json()
