from enum import Enum


class ParseMode(str, Enum):
    HTML = "HTML"
    MARKDOWN = "MARKDOWN"
    MARKDOWNV2 = "MARKDOWNV2"
