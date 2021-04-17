from PIL import Image
from io import BytesIO
from image_utils.compress.compress_dimension import CompressDimension
from image_utils.compress.image_file import ImageFile


class CompressImage:
    image_file = None
    dimension = None
    output = None

    def auto_resize(self):
        self.image_file.image = self.image_file.image.resize(
            (self.dimension.width, self.dimension.compress_size[1]),
            Image.ANTIALIAS
        )
        print('auto')

    def fixed_resize(self):
        self.image_file.image = self.image_file.image.resize(
            (
                int(self.dimension.width),
                int(self.dimension.height)
            ),
            Image.ANTIALIAS
        )
        print('not auto')

    def resize(self, size, image, name=None):
        # set image
        self.image_file = ImageFile(image)
        self.output = BytesIO()
        # set dimension image
        self.dimension = CompressDimension(size)
        self.dimension.set_compress_size(self.image_file.image)
        # fixed resolution
        if self.dimension.height:
            if self.dimension.height == 0:
                self.auto_resize()
            else:
                self.fixed_resize()
        else:
            self.auto_resize()
        # save and return image
        self.image_file.image.save(self.output, format='JPEG', quality=100)
        self.output.seek(0)
        return self.image_file.save_file(name, self.output)


compress_image = CompressImage()
