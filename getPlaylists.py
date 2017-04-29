import requests

headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer BQArRx4V3mXClwKNUIXOHp-nICg_eirBieSoMm8Q5nfwOZSGubfXMmGZFlKAF0TEQexHbN20khmKypOGhI1QPm042NuZjLeDF6ZlUXgSXWsvbb66z2kkv-zybG6T2BvXo1SiTMrsKf6WUb7zZs7JRLitDCcnyIrXR7pV',
}

requests.get('https://api.spotify.com/v1/users/12186663114/playlists', headers=headers)
