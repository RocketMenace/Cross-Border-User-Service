from dataclasses import FrozenInstanceError

import pytest

from app.domain.exceptions import InvalidEmailError
from app.domain.values.email import Email


@pytest.mark.asyncio
async def test_email_created_successful():
    email = Email(value="test@example.com")
    assert email.value == "test@example.com"


@pytest.mark.asyncio
async def test_email_invalid_local_part():
    with pytest.raises(InvalidEmailError) as e:
        Email(value="test-123@example.com")
        assert "Local part must contain only letters and numbers (a-z, A-Z, 0-9)." in str(e)


@pytest.mark.asyncio
async def test_email_invalid_domain_part():
    with pytest.raises(InvalidEmailError) as e:
        Email(value="test@example.com$")
        assert "Domain should be like 'example.com' or 'sub.example.co.uk" in str(e)


@pytest.mark.asyncio
async def test_too_short_email():
    with pytest.raises(InvalidEmailError) as e:
        Email(value="b@ma")


@pytest.mark.asyncio
async def test_too_long_email():
    with pytest.raises(InvalidEmailError):
        Email(value="etryrusaif@sdfhnjsdnksmdfdasdasdasdasdadasdasdak.com")


@pytest.mark.asyncio
async def test_frozen_email_value_object():
    email = Email(value="bob@example.com")
    with pytest.raises(FrozenInstanceError):
        email.value = "bob"


@pytest.mark.asyncio
async def test_cannot_set_wrong_value_type():
    with pytest.raises(ValueError):
        Email(value=123)
