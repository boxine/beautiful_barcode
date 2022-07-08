import argparse
import sys

from . import GTIN, renderers


def main():
    parser = argparse.ArgumentParser('Generate a barcode')
    parser.add_argument('-o', '--output', metavar='FILENAME', help='Output file', default='-')
    parser.add_argument(
        '-r', '--renderer', default='auto', choices=renderers.NAMED_RENDERERS.keys(),
        help='Renderer implementation to use.')
    parser.add_argument(
        'NUMBER',
        help='UPC-A or EAN number, for example 123456789012 or 4251192108913')
    args = parser.parse_args()

    barcode = GTIN(args.NUMBER)
    render_kwargs = {
        'renderer': args.renderer,
    }
    if args.output == '-':
        sys.stdout.buffer.write(barcode.render(**render_kwargs))
    else:
        barcode.write(args.output, **render_kwargs)


if __name__ == '__main__':
    main()
