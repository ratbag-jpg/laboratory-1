from PIL import Image
def use_pillow():
    img = Image.new('RGB', (100, 100), color = 'red')
    print(f"Pillow: Створено картинку {img.size} формату {img.format}")