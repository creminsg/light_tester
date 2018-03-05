# -*- coding: utf-8 -*-

"""Console script for light_tester."""
import sys
import click
import light_tester
click.disable_unicode_literals_warning = True

@click.command()
@click.option("--input", default=None, help="input URI (file or URL)")

def main(input=None):
    print("input", input)
    result = light_tester.parseFile(input)
    print("There are ", result, "lights on")
    return 0


if __name__ == "__main__":
    sys.exit(main())
