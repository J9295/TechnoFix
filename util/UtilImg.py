from PIL import ImageTk, Image

def read_img(path, size):
    return ImageTk.PhotoImage(Image.open(path).resize(size, Image.ADAPTIVE))