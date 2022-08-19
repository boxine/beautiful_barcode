import os.path

from . import renderers


class Barcode:
    def to_modules(self) -> str:
        """ Convert the Barcode to modules (1 or 0) """
        raise NotImplementedError

    def render(self, renderer='auto', extension=None) -> bytes:
        """ Renders the barcode as a bytes object """

        rend = renderers.make_renderer(renderer, extension=extension)
        self._paint(rend)
        return rend.to_bytes()

    def write(self, filename, renderer='auto'):
        data = self.render(renderer=renderer, extension=os.path.splitext(filename)[1])
        with open(filename, 'wb') as out_file:
            out_file.write(data)
