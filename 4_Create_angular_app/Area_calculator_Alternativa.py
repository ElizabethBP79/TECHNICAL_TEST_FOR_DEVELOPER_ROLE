import numpy as np
from PIL import Image
import random

def load_binary_image(image_path):
    img = Image.open(image_path).convert('L')  
    img_array = np.array(img)
    binary_image = (img_array < 128).astype(int) 
    return binary_image

def generate_random_points(image_shape, n):
    height, width = image_shape
    points = [(random.randint(0, width - 1), random.randint(0, height - 1)) for _ in range(n)]
    return points

def count_points_in_stain(points, binary_image):
    ni = sum(binary_image[y, x] for x, y in points)
    return ni

def estimate_area(binary_image, ni, n):
    total_area = binary_image.size  
    estimated_area = (total_area * ni) / n
    return estimated_area

def main(image_path, n):
    binary_image = load_binary_image(image_path)
    random_points = generate_random_points(binary_image.shape, n)
    ni = count_points_in_stain(random_points, binary_image)
    estimated_area = estimate_area(binary_image, ni, n)

    print(f'Número de puntos dentro de la mancha (ni): {ni}')
    print(f'Área estimada de la mancha: {estimated_area} píxeles')

if __name__ == "__main__":
    image_path = "C:\\Users\\eliza\\OneDrive\\Escritorio\\Imexhs\\TECHNICAL_TEST_FOR_DEVELOPER_ROLE\\4_Create_angular_app\\Mancha.jpg"
    n = 100  
    main(image_path, n)
