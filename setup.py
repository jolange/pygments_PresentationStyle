from setuptools import setup


setup(name='pygments_PresentationStyle',
      version='0.1',
      description='Color style for presentations.',
      long_description='''
Color style for presentations, mainly intended for usage with the
LibreOffice extension Code Highlighter:
https://extensions.libreoffice.org/extensions/code-highlighter
https://github.com/slgobinath/libreoffice-code-highlighter

Based on the builtin style 'manni'.
''',
      long_description_content_type='text/markdown',
      url='https://github.com/jolange/pygments_PresentationStyle',
      author='Johannes Lange',
      license='GPL-3.0',
      packages=['pygments_PresentationStyle'],
      python_requires='>=3',
      entry_points='''[pygments.styles]
presentation = pygments_PresentationStyle.style:PresentationStyle''',)
