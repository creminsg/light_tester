# -*- coding: utf-8 -*-

"""Console script for light_tester."""
import sys
import click
import light_tester.ledSolve
click.disable_unicode_literals_warning = True

@click.command()
@click.option("--input", default=None, help="input URI (file or URL)")

def main(input=None):
    print("input", input)
    input = sys.argv[2]
    result = ledSolve.parseFile(input)
    print("There are ", result, "lights on")
    return 0


if __name__ == "__main__":
    sys.exit(main())
