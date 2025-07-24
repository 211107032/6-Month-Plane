import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import requests
from io import BytesIO 

# from PIL import Image
# import requests
# from io import BytesIO

def load_image_from_url(url):
    response = requests.get(url)  # ✅ fixed typo
    return Image.open(BytesIO(response.content))  # ✅ fixed BytesIO

elephant_url = "https://upload.wikimedia.org/wikipedia/commons/3/37/African_Bush_Elephant.jpg"
elephant = load_image_from_url(elephant_url)

plt.figure(figsize=(6, 4))
plt.imshow(elephant)  # ✅ fixed function name: should be imshow, not image
plt.axis('off') 
plt.title('Elephant')# Optional: to hide axis
plt.show()

def load_image_from_url(url):
    response = requests.get(url)  # ✅ fixed typo
    return Image.open(BytesIO(response.content))  # ✅ fixed BytesIO

peacock_feather = "https://m.media-amazon.com/images/I/81JSw5mE54L._UF894,1000_QL80_.jpg"
Peacock = load_image_from_url(peacock_feather)

plt.figure(figsize=(6, 4))
plt.imshow(Peacock)  # ✅ fixed function name: should be imshow, not image
plt.axis('off') 
plt.title('peacock feather')# Optional: to hide axis
plt.show()