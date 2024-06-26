import reflex as rx
from enum import Enum
from .colors import Color, TextColor
from .fonts  import Font as Font, FontWeight


# Constants
MAX_WIDTH = "600px"


STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap"
]


# Sizes
class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.9em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"


# Styles
    
BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    "background_color": Color.BACKGROUND.value,
    rx.chakra.heading: {
        "font_family": Font.DEFAULT.value,
        "font_weight": FontWeight.MEDIUM.value,
        "color":TextColor.HEADER.value
    },
    rx.chakra.Button: {
        "width": "100%",
        "height": "100%",
        "white_space": "normal",
        "text_align": "start",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "background_color": Color.CONTENT.value,
        "color": TextColor.HEADER.value,
        "_hover": {
            "background_color": Color.SECONDARY.value
        }
    },
    rx.chakra.link: {
        "text_decoration": "none",
        "_hover": {}
    }
}

navbar_title_style = dict(
    font_family=Font.LOGO.value,
    font_weight= FontWeight.MEDIUM.value,
    font_size=Size.LARGE.value
)

title_style = dict(
    width = "100%",
    padding_top = Size.DEFAULT.value
)

button_title_style = dict(
    font_size= Size.DEFAULT.value,
    color=TextColor.HEADER.value,
    font_family=Font.TITLE.value,
    font_weight= FontWeight.MEDIUM.value
)


button_body_style = dict(
    font_size= Size.MEDIUM.value,
    color=TextColor.BODY.value,
    font_family=Font.DEFAULT.value,
    font_weight= FontWeight.LIGHT.value
)
