# import requests

# def get_access_token(client_id, client_secret):
#     token_url = 'https://api.hotjar.io/v1/oauth/token'
#     data = {
#         'grant_type': 'client_credentials',
#         'client_id': client_id,
#         'client_secret': client_secret
#     }
#     response = requests.post(token_url, data=data)
#     response.raise_for_status()
#     return response.json()['access_token']


# def get_survey_responses(site_id, access_token):
#     # "/v1/sites/:site_id/surveys"
#     breakpoint()
#     base_url = 'https://api.hotjar.io/v1'
#     endpoint = f'/sites/{site_id}/surveys/responses'
#     headers = {
#         'Authorization': f'Bearer {access_token}'
#     }
#     response = requests.get(base_url + endpoint, headers=headers)
#     response.raise_for_status()
#     return response.json()



# def main():
#     client_id = '5530999'
#     client_secret = '8sDLeUQ3DZ7vnBiajOVbRbKC'
#     site_id = '5339518'
#     # site_id = '4325673'
#     # site_id = '3883486'
#     # Credential name: Konardesign
#     # Client ID: 5530999
#     # Client secret: 8sDLeUQ3DZ7vnBiajOVbRbKC
#     breakpoint()
#     try:
#         access_token = get_access_token(client_id, client_secret)
#         surveys = get_survey_responses(site_id, access_token)
#         print(surveys)
#     except requests.exceptions.HTTPError as http_err:
#         print(f'HTTP error occurred: {http_err}')
#     except Exception as err:
#         print(f'Other error occurred: {err}')

# if __name__ == '__main__':
#     main()



from clarity_api import Clarity

# Initialize with your API token
clarity = Clarity(api_token='YOUR_API_TOKEN')

# Fetch data for the last day
data = clarity.get_data(num_of_days=1)

# Process the data as needed
