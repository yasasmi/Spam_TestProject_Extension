from distutils.core import setup, Extension

def main():
    setup(name="spam",
          version="0.0.1",
          description="Python interface for the spam module.",
          author="<R and c>",
          author_email="your_email@gmail.com",
          ext_modules=[Extension("spam", ["spammodule.c"])])

if __name__ == "__main__":
    main()
