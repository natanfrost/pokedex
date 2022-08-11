import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

BASE_URL = "https://pokemoncries.com/"

for i in range(905):
    print(f'downloading cry {i + 1} of 905...')
    if i <= 648:
        urllib.request.urlretrieve(f"{BASE_URL}/cries-old/{i + 1}.mp3", f'C:\\Users\\natanielv\\Documents\\Personal\\pokemon-cries\\{i + 1}.mp3')
    else:
        urllib.request.urlretrieve(f"{BASE_URL}/cries/{i + 1}.mp3", f'C:\\Users\\natanielv\\Documents\\Personal\\pokemon-cries\\{i + 1}.mp3')

