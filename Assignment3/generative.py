from __future__ import annotations
from ai import predict_number, read_image
import math
def flatten_image(image: list[list[int]]) -> list[int]:
    """
    Flattens a 2D list into a 1D list.
    
    :param image: 2D list of integers representing an image.
    :return: 1D list of integers representing a flattened image.
    """
    return [pixel for row in image for pixel in row]
    
def unflatten_image(flat_image: list[int]) -> list[list[int]]:
    """
    Unflattens a 1D list into a 2D list.
        
    :param flat_image: 1D list of integers representing a flattened image.
    :return: 2D list of integers.
    """
    retVal = []
    side_length = int(math.sqrt(len(flat_image)))
    for i in range(side_length):
        retVal.append(flat_image[i * side_length:(i + 1) * side_length])
    return retVal

def check_adjacent_for_one(flat_image: list[int], flat_pixel: int) -> bool:
    """
    Checks if a pixel has an adjacent pixel with the value of 1.
    
    :param flat_image: 1D list of integers representing a flattened image.
    :param flat_pixel: Integer representing the index of the pixel in question.
    :return: Boolean.
    """
    edge = int(math.sqrt(len(flat_image)))
    current_row = flat_pixel // edge
    current_column = flat_pixel % edge

    # Check adjacent pixels in the same row
    if current_column > 0 and flat_image[flat_pixel - 1] == 1:
        return True
    elif current_column < edge - 1 and flat_image[flat_pixel + 1] == 1:
        return True

    # Check adjacent pixels in the row above
    if current_row > 0 and flat_image[flat_pixel - edge] == 1:
        return True

    # Check adjacent pixels in the row below
    if current_row < edge - 1 and flat_image[flat_pixel + edge] == 1:
        return True

    # No adjacent 1 found
    return False

def pixel_flip(lst: list[int], orig_lst: list[int], budget: int, results: list, i: int = 0) -> None:
    """
    Uses recursion to generate all possibilities of flipped arrays where
    a pixel was a 0 and there was an adjacent pixel with the value of 1.

    :param lst: 1D list of integers representing a flattened image.
    :param orig_lst: 1D list of integers representing the original flattened image.
    :param budget: Integer representing the number of pixels that can be flipped.
    :param results: List of 1D lists of integers representing all possibilities of flipped arrays, initially empty.
    :param i: Integer representing the index of the pixel in question.
    :return: None.
    """

    # Exit if we've reached the end of the budget
    if budget == 0:
        return

    # If we've reached the end of the list, add the result to the results list
    if i == len(orig_lst):
        # results.append(lst)
        return

    # Check if we can flip the current pixel
    if orig_lst[i] == 0 and check_adjacent_for_one(orig_lst, i):
        # Flip the pixel and explore the new possibilities
        new_lst = lst[:]
        new_lst[i] = 1
        results.append(new_lst)
        pixel_flip(new_lst, orig_lst, budget-1, results, i+1)

    # Continue exploring without flipping the current pixel
    pixel_flip(lst, orig_lst, budget, results, i+1)



def write_image(orig_image: list[list[int]], new_image: list[list[int]], file_name: str) -> None:
    """
    This function writes the new image to a file, marking the modified pixels with 'X'.

    :param orig_image: A 2D list representing the original image.
    :param new_image: A 2D list representing the newly generated image.
    :param file_name: A string representing the filename for the output file.
    :return: None.
    """
    # Getting the size of the image
    length_orig_image = len(orig_image)

    # Opening the file for writing
    with open(file_name, 'w') as file:
        # Iterating over each row of the image
        for i in range(length_orig_image):
            # Iterating over each pixel in the row
            for j in range(length_orig_image):
                # Checking if the pixel is modified
                if(orig_image[i][j] != new_image[i][j]):
                    # Writing 'X' to indicate modification
                    file.write("X")
                else:
                    # Writing the original value
                    file.write(str(new_image[i][j]))
            # Writing a new line after each row
            file.write('\n')



def generate_new_images(image, budget):
    """
    This function generates all the possible new images that can be created within the given budget.

    :param image: A 2D list representing the original image.
    :param budget: An integer indicating the number of pixels that can be flipped.
    :return: A list of 2D lists representing all possible new images.
    """
    #flattening the original image
    flat_image = flatten_image(image)

    # List to store the flipped image possibilities
    flipped_possibilities = []

    # Recursive function to generate all possible flipped images
    pixel_flip(flat_image, flat_image, budget, flipped_possibilities)

    #unflattening the flipped possibilities to get the original image format
    unflattened_possibilities = [unflatten_image(flat_image) for flat_image in flipped_possibilities]

    # Predicting the number of the original image
    predicted_number = predict_number(image)

    # Filtering the possibilities to include only images with the predicted number
    final_images = [img for img in unflattened_possibilities if predict_number(img) == predicted_number]

    # Returning the final list of generated images
    return final_images


if __name__ == "__main__":
    image = [
        [1, 0, 0],
        [1, 0, 0],
        [1, 1, 1]
    ]

    flat_image = flatten_image(image)
    budget = 2
    flipped_possibilities = []
    pixel_flip(flat_image, flat_image, budget, flipped_possibilities)

    print(f"Number of flipped possibilities: {len(flipped_possibilities)}")
    for i, possibility in enumerate(flipped_possibilities):
        unflattened_possibility = unflatten_image(possibility)
        print(f"Flipped possibility {i+1}:")
        for row in unflattened_possibility:
            print(row)