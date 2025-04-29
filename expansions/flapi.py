from flickr_api import FlickrApi
import keyring

api = FlickrApi.with_api_key(
    api_key=keyring.get_password("flickr_api", "key"),
    user_agent="Alex Chan's personal scripts <alex@alexwlchan.net>",
)
