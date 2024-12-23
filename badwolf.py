"""
    Badwolf Pygments Style
    ~~~~~~~~~~~~~~~~~~~~~~

    A Pygments style inspired by the Badwolf Vim theme.

    :author: Generated by ChatGPT
    :license: BSD, see LICENSE for details.
"""

from pygments.style import Style
from pygments.token import Token, Comment, Keyword, Name, String, Number, Operator, Generic, Punctuation, Literal, Whitespace, Error, Other


class BadwolfStyle(Style):
    """
    A Pygments style inspired by the Badwolf Vim theme.
    """
    name = 'badwolf'

    background_color = "#1c1b1a"  # blackgravel
    highlight_color = "#242321"   # darkgravel

    styles = {
        Token:                     "#f8f6f2",  # plain
        Whitespace:                "",

        Comment:                   "#857f78",  # gravel
        Comment.Preproc:           "#aeee00",  # lime
        Comment.Special:           "bold #ffffff bg:#ff2c4b",

        Keyword:                   "bold #ff2c4b",  # taffy
        Keyword.Type:              "#ff9eb8",        # dress
        Keyword.Declaration:       "#ff2c4b",
        Keyword.Reserved:          "bold #ff2c4b",

        Operator:                  "#ff2c4b",  # taffy
        Operator.Word:             "#ff2c4b",

        Punctuation:               "#f8f6f2",  # plain

        Name:                      "#ffa724",  # orange
        Name.Function:             "#ffa724",
        Name.Class:                "#ffa724",
        Name.Namespace:            "#ffa724",
        Name.Exception:            "bold #aeee00",  # lime
        Name.Variable:             "#ffa724",
        Name.Constant:             "bold #b88853",  # toffee
        Name.Label:                "bold #ff2c4b",
        Name.Entity:               "#aeee00",  # lime
        Name.Attribute:            "#c7915b",  # coffee
        Name.Tag:                  "bold #c7915b",
        Name.Decorator:            "#ff9eb8",  # dress

        String:                    "#f4cf86",  # dirtyblonde
        String.Char:               "bold #b88853",
        String.Escape:             "bold #ff9eb8",
        String.Doc:                "#857f78",
        String.Interpol:           "#f4cf86",
        String.Other:              "#f4cf86",

        Number:                    "bold #b88853",  # toffee
        Number.Float:              "bold #b88853",
        Number.Integer:            "bold #b88853",
        Number.Hex:                "bold #b88853",
        Number.Oct:                "bold #b88853",

        Generic:                   "",
        Generic.Emph:              "italic",
        Generic.Strong:            "bold",
        Generic.Prompt:            "bold #0a9dff",  # tardis
        Generic.Subheading:        "#857f78",

        Error:                     "bold #ffffff bg:#ff2c4b",
    }