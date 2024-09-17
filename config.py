from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    aries_vcr_url: str = "http://host.docker.internal:8080"
    ISSUERS: list = [
        {"id": "did:web:example.com", "name": "Example Issuer"},
        {
            "id": "did:web:test.digitaltrust.traceability.site:petroleum-and-natural-gas-act:director-of-petroleum-lands",
            "name": "Director of Petroleum Lands",
        },
        {
            "id": "did:web:test.digitaltrust.traceability.site:mines-act:chief-permitting-officer",
            "name": "Chief Permitting Officer",
        },
    ]


settings = Settings()
