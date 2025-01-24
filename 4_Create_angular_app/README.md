# Estimation of a Stain's Area in Binary Images

This project is a Python script that estimates the area of a stain in a binary image using a probabilistic method based on random point generation.

# Features

    * Converts images to grayscale and then to binary format.
    * Generates random points within the image.
    * Counts how many of those points fall inside the stain.
    * Calculates the estimated area of the stain based on the number of random points and their distribution.

# Prerequisites
    1. Ensure Python 3 is installed on your system.
    2. Clone this repository:

        git clone https://github.com/ElizabethBP79/TECHNICAL_TEST_FOR_DEVELOPER_ROLE
        cd TECHNICAL_TEST_FOR_DEVELOPER_ROLE/4_Create_angular_app
    
    3. Make sure you have the following Python packages installed:
        * `numpy`
        * `Pillow`

        Install them using pip:


                pip install numpy pillow
    

# Usage
    1. Set the parameters:

        * Specify the image path in the image_path variable.
        * Adjust the number of random points generated (n) as needed. More points increase accuracy.
    2. Run the script:

        python Area_calculator_Alternativa.py
    
    3. Expected output:

    The script will print the number of points inside the stain (ni) and the estimated area of the stain in pixels.


# Main Functions

    load_binary_image(image_path)
        Converts an image to grayscale and then to binary (0 and 1). Pixels with a value below 128 are considered part of the stain (1).

    generate_random_points(image_shape, n)
        Generates n random points within the image's dimensions.

    count_points_in_stain(points, binary_image)
        Counts how many random points fall inside the stain in the binary image.

    estimate_area(binary_image, ni, n)
        Calculates the estimated area of the stain using the formula:

        Estimated Area = (Total Image Area × 𝑛𝑖)/  𝑛
        
        ​
 
# Customization
    * Image Path: Update the image_path value to use different images.
    * Number of Points: Adjust n to increase or decrease the accuracy of the area calculation.

# Limitations
    * The script only works with binary images. If the image contains multiple colors, the processing may not be accurate.
    * The accuracy of the calculation depends on the number of random points generated (n).