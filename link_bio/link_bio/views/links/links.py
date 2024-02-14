import reflex as rx
from link_bio.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button("Twitch", 
                    "https://reflex.dev/docs/library/"),
        link_button("YouTube", 
                    "https://reflex.dev/docs/library/"),
        link_button("YouTube (canal secundario)", 
                    "https://reflex.dev/docs/library/"),
        link_button("Discord", 
                    "https://reflex.dev/docs/library/")
    )