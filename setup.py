from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name='GLaDOS alpha',
      version='4.0',
      description='General Lookup of α-Decay for Optimised Search (GLαDOS)',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/Yottaphy/glados',
      author='Jorge Romero',
      author_email='joromero@jyu.fi',
      license='GPL-3.0',
      packages=['glados_alpha'],
      install_requires=[
          'argparse', 'engineering_notation', 'colorama'
      ],
      zip_safe=False,
      entry_points={
        'console_scripts': [
            'glados_alpha = glados_alpha:main'
        ]},
    )