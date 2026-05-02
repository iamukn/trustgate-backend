import os, requests
from core.config import headers
from urllib.parse import quote

API_KEY = os.environ.get('nokiaApiKey')
BASE_URL = os.environ.get('BASE_URL')

async def number_verify(phone: str):

    result = ''

    # get client credentials
    url = "{}/oauth2/v1/auth/clientcredentials".format(BASE_URL)
    response = requests.get(
        url,
        headers=headers
            ) 

    # get client_id and client_secret
    if response.status_code == 200:
        data = response.json()
        client_id = data.get('client_id')
        client_secret = data.get('client_secret')

        

        # get Authorization token
        auth_token_url = '{}/.well-known/openid-configuration'.format(BASE_URL)
        res = requests.get(
                auth_token_url,
                headers=headers
                )

        if res.status_code == 200:
            # get authorization_endpoint and token_endpoint
            auth_data = res.json()
            authorization_endpoint = auth_data.get('authorization_endpoint')
            token_endpoint = auth_data.get('token_endpoint')

            # get NaC authorization code using the auth_endpoint
            redirect_uri = 'https://example.com'
            scope = quote('dpv:FraudPreventionAndDetection number-verification:verify')
            login_hint = quote(phone)

            auth_token_url = f"{authorization_endpoint}?scope={scope}&state=state&response_type=code&client_id={client_id}&redirect_uri={redirect_uri}&login_hint={login_hint}"

            # Retrieving Nac authorization code query should be made by the users device
            auth_code_res = requests.get(auth_token_url)
            
            if (auth_code_res.status_code == 200):
            
                # get the authentication code from the url
                url_path = auth_code_res.url
                if 'code' in url_path:
                    nac_code = url_path.split('code=')[-1]

                    # Obtain single-use Access Token for Number Verification
                    
                    data = {
                        'client_id': client_id,
                        'client_secret': client_secret,
                        'grant_type': 'authorization_code',
                        'code': nac_code
                            }
                    response = requests.post(
                            token_endpoint,
                            data=data,
                            )


                    if (response.status_code == 200):
                        # get the access token
                        data = response.json()
                        access_token = data.get('access_token')

                        # query the Numbers Verification API using the access token
                        # Note this token should be generated from the call made from the clients device
                        # not the backend

                        headers['Authorization'] = 'Bearer {}'.format(access_token)

                        payload = {
                            'phoneNumber': phone
                                }

                        numbers_verification_url = '{}/passthrough/camara/v1/number-verification/number-verification/v0/verify'.format(BASE_URL)

                        response = requests.post(
                                numbers_verification_url,
                                json=payload,
                                headers=headers
                                )

                        if (response.status_code == 200):
                            result = response.json()

    return result
