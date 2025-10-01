import pytest
from source.service import UserService, APIClient


def test_get_username_with_mock(mocker):
    mock_api_client = mocker.Mock(spec = APIClient) # create a Mock API Client

    mock_api_client.get_user_data.return_value = {'id': 1, 'name' : 'Alice'}

    service = UserService(mock_api_client)

    result = service.get_username(1)


    #Assertions
    assert result == 'ALICE' # check if processing was done correctly
    mock_api_client.get_user_data.assert_called_once_with(1) # Ensure correct API call
  
    