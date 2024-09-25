import asyncio
from pydantic import ValidationError

from config import settings
from services import vcr as vcr_service

from schemas import Issuer


async def register_issuers():
    issuers = settings.issuers or []

    for issuer in issuers:
        try:
            issuer_data = Issuer(**issuer).model_dump(exclude_none=True)
            svc_response = await vcr_service.register_issuer(issuer_data)
            print(f"Issuer registered: {issuer}", svc_response, sep="\n")
        except (ValidationError, Exception) as e:
            print(f"Unable to register issuer: {issuer}", e, sep="\n")


if __name__ == "__main__":
    asyncio.run(register_issuers())
