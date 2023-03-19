import cv2
import numpy as np
import random

# Set parameters
image_size = 512
line_widths = list(range(10, 201, 10))
contrast_levels = list(range(5, 205, 5))
noise_levels = [0, 10, 20, 30, 40]
filter_sizes = [0, 3, 5, 7, 9]

# Generate test images with different line widths, contrast levels, noise levels, filters and orientations
for i in range(1000):
    # Create a new blank image
    image = np.zeros((image_size, image_size), dtype=np.uint8)

    # Randomly choose a line width
    line_width = random.choice(line_widths)

    # Randomly choose the orientation of the line (horizontal or vertical)
    orientation = random.choice(['horizontal', 'vertical'])

    # Add the line to the image with gradually increasing contrast level
    contrast_level = random.choice(contrast_levels)
    if orientation == 'horizontal':
        cv2.line(image, (0, image_size // 2), (image_size, image_size // 2), contrast_level, line_width)
    else:
        cv2.line(image, (image_size // 2, 0), (image_size // 2, image_size), contrast_level, line_width)

    # Add random noise to the image
    noise_level = random.choice(noise_levels)
    if noise_level > 0:
        noise = np.random.normal(scale=noise_level, size=(image_size, image_size))
        noisy_image = np.clip(image + noise, 0, 255).astype(np.uint8)
    else:
        noisy_image = image

    # Apply random Gaussian filter to the image
    filter_size = random.choice(filter_sizes)
    if filter_size > 0:
        filtered_image = cv2.GaussianBlur(noisy_image, (filter_size, filter_size), 0)
    else:
        filtered_image = noisy_image

    # Save the image with a unique filename
    if orientation == 'horizontal':
        filename = "test_image_c{}_w{:03d}_line_h.png".format(contrast_level, line_width)
    else:
        filename = "test_image_c{}_w{:03d}_line_v.png".format(contrast_level, line_width)
    cv2.imwrite(filename, filtered_image)
