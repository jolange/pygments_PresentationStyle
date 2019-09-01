# Copyright 2019 Johannes Lange
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

'''
Color style for presentations, mainly intended for usage with the
LibreOffice extension Code Highlighter:
https://extensions.libreoffice.org/extensions/code-highlighter
https://github.com/slgobinath/libreoffice-code-highlighter

Based on the builtin style 'manni'.
'''


import pygments.style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic, Whitespace


class PresentationStyle(pygments.style.Style):
    '''Color style for presentations.'''

    background_color = '#cccccc'

    styles = {
        Whitespace:         '#bbbbbb',
        Comment:            'italic #0077DD',
        Comment.Preproc:    'noitalic #009999',
        Comment.Special:    'bold',

        Keyword:            'bold #CC0000',
        Keyword.Pseudo:     'nobold',
        Keyword.Type:       '#007788',

        Operator:           '#555555',
        Operator.Word:      'bold #000000',

        Name.Builtin:       '#336666',
        Name.Function:      '#CC00FF',
        Name.Class:         'bold #00AA88',
        Name.Namespace:     'bold #00CCFF',
        Name.Exception:     'bold #CC0000',
        Name.Variable:      '#003333',
        Name.Constant:      '#336600',
        Name.Label:         '#9999FF',
        Name.Entity:        'bold #999999',
        # Name.Attribute:     '#00CC00',
        Name.Tag:           'bold #330099',
        Name.Decorator:     '#9999FF',

        String:             '#505050',
        String.Doc:         'italic',
        String.Interpol:    '#AA0000',
        String.Escape:      'bold #CC3300',
        String.Regex:       '#33AAAA',
        String.Symbol:      '#FFCC33',
        String.Other:       '#CC3300',

        Number:             '#FF6600',

        Generic.Heading:    'bold #003300',
        Generic.Subheading: 'bold #003300',
        Generic.Deleted:    'border:#CC0000 bg:#FFCCCC',
        Generic.Inserted:   'border:#00CC00 bg:#CCFFCC',
        Generic.Error:      '#FF0000',
        Generic.Emph:       'italic',
        Generic.Strong:     'bold',
        Generic.Prompt:     'bold #CC0000',
        Generic.Output:     '#808080',
        Generic.Traceback:  '#99CC66',

        Error:              'bg:#FFAAAA #AA0000'
    }
