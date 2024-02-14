import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(name="Brais Díaz", size="xl"),
        rx.text("@braisdr11"),
        rx.text("HOLA MI NOMBRE ES BRAIS DÍAZ"),
        rx.text("""Soy ingeniero de software desde hace más de 12 años.
                Actualmente trabajo como freelance full-stack developer iOS y Android.
                Además creo contenido formativo sobre programación y tecnología en redes.
                Aquí podrás encontrar todos mis enlaces de interés. ¡Bienvenida!)""")
    )