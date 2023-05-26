from __future__ import annotations
import unittest
from generative import flatten_image, unflatten_image, check_adjacent_for_one, pixel_flip, generate_new_images
from ai import read_image

class TestGenerative(unittest.TestCase):

    def test_flatten_image(self):
        # verify output of flatten_image for different sizes of images
        image1 = [[1, 0], [0, 1]]
        image2 = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
        image3 = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1]]

        self.assertEqual(flatten_image(image1), [1, 0, 0, 1])
        self.assertEqual(flatten_image(image2), [1, 0, 1, 0, 1, 0, 1, 0, 1])
        self.assertEqual(flatten_image(image3), [1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1])

    def test_unflatten_image(self):
        # verify output of unflatten_image for different sizes of flattened images
        flat_image1 = [1, 0, 0, 1]
        flat_image2 = [1, 0, 1, 0, 1, 0, 1, 0, 1]
        flat_image3 = [1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1]

        self.assertEqual(unflatten_image(flat_image1), [[1, 0], [0, 1]])
        self.assertEqual(unflatten_image(flat_image2), [[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        self.assertEqual(unflatten_image(flat_image3), [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1]])

    def test_check_adjacent_for_one(self):
        # Verify output of check_adjacent_for_one for different scenarios
        image = [
            [0, 1, 0], 
            [1, 0, 0], 
            [0, 1, 0]
            ]
        # flat image for check_adjacent_for_one to use
        flat_image = flatten_image(image)

        # Middle of the image
        self.assertTrue(check_adjacent_for_one(flat_image, 4))

        # Edge of the image
        self.assertFalse(check_adjacent_for_one(flat_image, 1))

        # corner of the image
        self.assertTrue(check_adjacent_for_one(flat_image, 0))

        # Edge of the image
        self.assertFalse(check_adjacent_for_one(flat_image, 5))

    def test_pixel_flip(self):
        #verify output of pixel_flip for a 5x5 image with a budget of 2
        image = [
        [0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0], 
        [0, 0, 1, 0, 0], 
        [0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0]
        ]
        result_image1 = [
        [0, 0, 0, 0, 0], 
        [0, 0, 1, 0, 0], 
        [0, 0, 1, 0, 0], 
        [0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0]
        ]
        result_image2 = [
        [0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0], 
        [0, 0, 1, 1, 0], 
        [0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0]
        ]
        result_image3 = [
        [0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0], 
        [0, 0, 1, 0, 0], 
        [0, 0, 1, 0, 0], 
        [0, 0, 0, 0, 0]
        ]
        result_image4 = [
        [0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0], 
        [0, 1, 1, 0, 0], 
        [0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0]
        ]
        result_image5 = [
        [0, 0, 0, 0, 0], 
        [0, 0, 1, 0, 0], 
        [0, 0, 1, 1, 0], 
        [0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0]
        ]
        result_image6 = [
        [0, 0, 0, 0, 0], 
        [0, 0, 1, 0, 0], 
        [0, 0, 1, 0, 0], 
        [0, 0, 1, 0, 0], 
        [0, 0, 0, 0, 0]
        ]
        result_image7 = [
        [0, 0, 0, 0, 0], 
        [0, 0, 1, 0, 0], 
        [0, 1, 1, 0, 0], 
        [0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0]
        ]
        result_image8 = [
        [0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0], 
        [0, 0, 1, 1, 0], 
        [0, 0, 1, 0, 0], 
        [0, 0, 0, 0, 0]
        ]
        result_image9 = [
        [0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0], 
        [0, 1, 1, 1, 0], 
        [0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0]
        ]
        result_image10 = [
        [0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0], 
        [0, 1, 1, 0, 0], 
        [0, 0, 1, 0, 0], 
        [0, 0, 0, 0, 0]
        ]
        flattened_image = flatten_image(image)
        results = []
        pixel_flip(flattened_image, flattened_image, 2, results)

        self.assertEqual(len(results), 10) # Total possibilities

        # trying every single posibility
        self.assertIn(flatten_image(result_image1), results)
        self.assertIn(flatten_image(result_image2), results)
        self.assertIn(flatten_image(result_image3), results)
        self.assertIn(flatten_image(result_image4), results)
        self.assertIn(flatten_image(result_image5), results)
        self.assertIn(flatten_image(result_image6), results)
        self.assertIn(flatten_image(result_image7), results)
        self.assertIn(flatten_image(result_image8), results)
        self.assertIn(flatten_image(result_image9), results)
        self.assertIn(flatten_image(result_image10), results)

    def test_generate_new_images(self):
        # Verify output of generate_new_images with the input image.txt
        image = read_image("image.txt")
        budget = 2

        new_images = generate_new_images(image, budget)
        self.assertTrue(len(image), 28) # checks the vertical length
        self.assertTrue(all(len(sublist) == 28 for sublist in image)) # checks the horizontal length
        self.assertEqual(len(new_images), 2556)  # Total possibilities
        self.assertTrue(all(len(img) == 28 and all(0 <= pixel <= 1 for pixel in row) for img in new_images for row in img))  # Verify size and value constraints
        
        """ 
        My attempt at the final test case. I am trying to compare every new_image to the original image
        and use the index to check_adjacent_for_one(original_image, index). Below is my best attempt
        """
        #self.assertTrue(all(check_adjacent_for_one(new_images, i) for i, (original_row, modified_row) in enumerate(zip(image, new_images)) if original_row != modified_row))



if __name__ == '__main__':
    unittest.main()






