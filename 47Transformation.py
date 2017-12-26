from PIL import Image

dog = Image.open('dog.jpg')
square_dog = dog.resize((250, 250))
flip_dog = dog.transpose(Image.FLIP_LEFT_RIGHT)
spin_dog = dog.transpose(Image.ROTATE_270)

# dog.show()
# square_dog.show()
# flip_dog.show()
spin_dog.show()