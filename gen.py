from PIL import Image, ImageDraw
import random
import os
import colorsys

def generate_random_image(size=(100, 100)):
    # Create random background color
    hue = random.random()
    saturation = random.uniform(0.3, 1.0)
    value = random.uniform(0.3, 1.0)
    rgb = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(hue, saturation, value))
    
    # Create image and drawing context
    image = Image.new('RGB', size, rgb)
    draw = ImageDraw.Draw(image)
    
    # Add random shapes
    for _ in range(random.randint(3, 10)):
        shape_type = random.choice(['circle', 'rectangle', 'line'])
        color = tuple(random.randint(0, 255) for _ in range(3))
        
        if shape_type == 'circle':
            x = random.randint(0, size[0])
            y = random.randint(0, size[1])
            radius = random.randint(5, 30)
            draw.ellipse([x-radius, y-radius, x+radius, y+radius], fill=color)
        
        elif shape_type == 'rectangle':
            x1 = random.randint(0, size[0])
            y1 = random.randint(0, size[1])
            x2 = random.randint(x1, size[0])
            y2 = random.randint(y1, size[1])
            draw.rectangle([x1, y1, x2, y2], fill=color)
        
        else:  # line
            x1 = random.randint(0, size[0])
            y1 = random.randint(0, size[1])
            x2 = random.randint(0, size[0])
            y2 = random.randint(0, size[1])
            draw.line([x1, y1, x2, y2], fill=color, width=random.randint(1, 5))
    
    return image

def generate_assets(output_dir, num_images=2000):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate images with different sizes
    for i in range(num_images):
        # Random size between 50x50 and 300x300
        size = (random.randint(50, 300), random.randint(50, 300))
        image = generate_random_image(size)
        
        # Save with random file extension
        ext = random.choice(['.png', '.jpg', '.webp'])
        filename = f'asset_{i:04d}{ext}'
        filepath = os.path.join(output_dir, filename)
        
        image.save(filepath)
        
        # Print progress
        if (i + 1) % 100 == 0:
            print(f'Generated {i + 1} images')

if __name__ == '__main__':
    output_dir = 'images'  # Change this to your desired output directory
    generate_assets(output_dir)