import requests
from PIL import Image
from io import BytesIO
from urllib.parse import urlparse

def download_images_from_urls(urls, folder_path):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        for url in urls:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                image = Image.open(BytesIO(response.content))
                image = image.convert("RGB")
                # Отримання останнього шматка URL як назви файла
                filename = urlparse(url).path.split("/")[-1]
                image.save(folder_path + filename)
                print(f"Фото {filename} успішно завантажено!")
            else:
                print(f"Помилка при завантаженні з URL {url}: статус {response.status_code}")
    except Exception as e:
        print("Сталася помилка:", str(e))

# Приклад використання
urls = [
    "https://example.com/image1.jpg",
    "https://example.com/image2.jpg",
    "https://example.com/image3.jpg"
]  # Масив URL-посилань на фото

folder_path = "./images/"  # Шлях до каталогу для збереження фото

download_images_from_urls(urls, folder_path)
