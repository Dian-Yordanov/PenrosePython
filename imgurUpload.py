__author__ = 'zyan'
from imgurpython import ImgurClient

client_id = '8e6cf031726addc'
client_secret = '1b43217aced31b74193534115d363c9c9d4fa090'

client = ImgurClient(client_id, client_secret)

authorization_url = client.get_auth_url('pin')

# ... redirect user to `authorization_url`, obtain pin (or code or token) ...

credentials = client.authorize('53df311ae2', 'pin')
client.set_user_auth(credentials['access_token'], credentials['refresh_token'])

# Example request
for album in client.get_account_albums('dianyordanov'):
    album_title = album.title if album.title else 'Untitled'
    print('Album: {0} ({1})'.format(album_title, album.id))

for image in client.get_album_images(album.id):
    image_title = image.title if image.title else 'Untitled'
    print('\t{0}: {1}'.format(image_title, image.link))

# Save some API credits by not getting all albums
    break

client.upload_from_path('/home/zyan/PycharmProjects/PenrosePython/penrose.png', config='None', anon='False')
