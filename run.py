"""
Use this to create a usable PYPi mirror based on the files
that are in the ./files directory.
"""
import glob
from basketweaver.makeindex import main as basketweaver


def main():
    basketweaver(glob.glob("./files/*"))


if __name__ == "__main__":
    main()
