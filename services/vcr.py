"""Service to call Aries VCR API."""

import json
from typing import Any
from fastapi import Response
from httpx import AsyncClient

from config import settings


async def register_credential_type(credential_type: dict) -> Any:
    """Register a new credential type"""

    # Make an HTTP request to the Aries VCR API
    async with AsyncClient(
        base_url=f"{settings.aries_vcr_url}/agentcb/topic"
    ) as client:
        response = await client.post("/vc_di_credential_type/", json=credential_type)
        response.raise_for_status()
        return response.json()


async def issue_credential(credential: dict) -> Any:
    """Issue a new credential"""

    # Make an HTTP request to the Aries VCR API
    async with AsyncClient(
        base_url=f"{settings.aries_vcr_url}/agentcb/topic"
    ) as client:
        response = await client.post("/vc_di_credential/", json=credential)
        response.raise_for_status()
        return response.json()


async def get_credential(credential_id: str) -> Response:
    """Get a credential from its UUID"""

    # Make an HTTP request to the Aries VCR API
    async with AsyncClient(base_url=f"{settings.aries_vcr_url}/api") as client:
        headers = {
            "Accept": "application/json, application/ld+json"
        }
        response = await client.get(
            f"/credential/{credential_id}",
            params={"raw_data": "true"},
            headers=headers,
        )
        response.raise_for_status()
        return Response(content=json.dumps(response.json()), media_type="application/ld+json")
