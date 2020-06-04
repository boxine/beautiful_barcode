import argparse
import sys

from . import renderers
from . import UPCA


def main():
    parser = argparse.ArgumentParser('Generate a barcode')
    parser.add_argument('-o', '--output', metavar='FILENAME', help='Output file', default='-')
    parser.add_argument(
        '-r', '--renderer', default='auto', choices=renderers.NAMED_RENDERERS.keys(),
        help='Renderer implementation to use.')
    parser.add_argument('NUMBER', help='UPC-A number, for example 012345678905')
    args = parser.parse_args()

    barcode = UPCA(args.NUMBER)
    render_kwargs = {
        'renderer': args.renderer,
    }
    if args.output == '-':
        sys.stdout.buffer.write(barcode.render(**render_kwargs))
    else:
        barcode.write(args.output, **render_kwargs)


if __name__ == '__main__':
    main()
