# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring

from unittest.mock import patch

import pytest

from fishjam import FishjamClient
from fishjam.errors import (
    InvalidFishjamCredentialsError,
    MissingFishjamIdError,
    NotFoundError,
)

VALID_FISHJAM_ID = "fjm_test"
VALID_MANAGEMENT_TOKEN = "tok_test"


class TestSyncValidation:
    def test_empty_fishjam_id_raises(self):
        with pytest.raises(MissingFishjamIdError):
            FishjamClient(fishjam_id="", management_token=VALID_MANAGEMENT_TOKEN)

    def test_both_provided_does_not_raise(self):
        FishjamClient(
            fishjam_id=VALID_FISHJAM_ID, management_token=VALID_MANAGEMENT_TOKEN
        )


class TestLiveCheck:
    def test_create_and_verify_raises_invalid_credentials_on_404(self):
        with patch.object(
            FishjamClient,
            "_request",
            side_effect=NotFoundError("Fishjam not found"),
        ):
            with pytest.raises(InvalidFishjamCredentialsError):
                FishjamClient.create_and_verify(
                    fishjam_id=VALID_FISHJAM_ID,
                    management_token=VALID_MANAGEMENT_TOKEN,
                )

    def test_create_and_verify_returns_client_and_pings_once(self):
        with patch.object(
            FishjamClient, "_request", return_value=None
        ) as mock_request:
            client = FishjamClient.create_and_verify(
                fishjam_id=VALID_FISHJAM_ID,
                management_token=VALID_MANAGEMENT_TOKEN,
            )

            assert isinstance(client, FishjamClient)
            assert mock_request.call_count == 1

    def test_check_credentials_raises_invalid_credentials_on_404(self):
        client = FishjamClient(
            fishjam_id=VALID_FISHJAM_ID, management_token=VALID_MANAGEMENT_TOKEN
        )
        with patch.object(
            FishjamClient,
            "_request",
            side_effect=NotFoundError("Fishjam not found"),
        ):
            with pytest.raises(InvalidFishjamCredentialsError):
                client.check_credentials()

    def test_check_credentials_returns_none_on_success(self):
        client = FishjamClient(
            fishjam_id=VALID_FISHJAM_ID, management_token=VALID_MANAGEMENT_TOKEN
        )
        with patch.object(FishjamClient, "_request", return_value=None):
            assert client.check_credentials() is None
