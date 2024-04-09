from flickr_photos_api import FlickrPhotosApi
import keyring

api = FlickrPhotosApi(
    api_key=keyring.get_password("flickr_api", "key"),
    user_agent="Alex Chan's personal scripts <alex@alexwlchan.net>",
)
