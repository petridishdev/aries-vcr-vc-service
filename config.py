from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    project_title: str = "Aries VCR VC Service"

    aries_vcr_url: str = "http://host.docker.internal:8080"

    issuers: list[dict] = [
        {
            "id": "did:web:test.digitaltrust.traceability.site:petroleum-and-natural-gas-act:director-of-petroleum-lands",
            "name": "Director of Petroleum Lands",
        },
        {
            "id": "did:web:test.digitaltrust.traceability.site:mines-act:chief-permitting-officer",
            "name": "Chief Permitting Officer",
        },
        {
            "id": "did:web:opsecid.github.io:acapy-did-web-demo",
            "name": "Demo Issuer",
        },
    ]


settings = Settings()
