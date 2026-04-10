import urllib.request
import re

url = "https://www.instagram.com/utku.blc/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'})
try:
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    match = re.search(r'<meta property="og:image" content="([^"]+)"', html)
    if match:
        img_url = match.group(1).replace('&amp;', '&')
        print("Found image URL:", img_url)
        # Download the image
        req_img = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req_img) as response, open(r"c:\Users\User\Desktop\veriler\landing-page\profile.png", 'wb') as out_file:
            out_file.write(response.read())
        print("Downloaded successfully!")
    else:
        print("Image URL not found in meta tags.")
except Exception as e:
    print("Error:", e)
