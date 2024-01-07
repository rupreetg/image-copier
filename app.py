# Images have copyright issues. We can't use the images without the permission or mention about the source of the image. 
# This project aims to generate similar images as the uploaded images so that there is no copyright issues. The images generated
# are similar in nature and pattern.

import openai_lib

# Lets first upload the image and get description of the image. 
step1_prompt = "Describe the image."
description = openai_lib.look(step1_prompt, "./images/sea-man.jpg")

print(description)

step2_prompt = f""" You are an image generator. Based on the description of the image provided, 
            create a new similar image matching the descripiton. Here is image description: '''{description}''' """

image_url = openai_lib.generate_image(step2_prompt)
print(image_url)