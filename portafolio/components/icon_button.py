import reflex as rx

def icon_button(icon: str, url: str, text="", solid=False) -> rx.Component:
    button_style = "solid" if solid else "surface"
    
    # La variable button_style determina el estilo del botón: solid o surface
    button = rx.button(
        rx.icon(icon),
        text,
        class_name="icon-button",
        variant="outline"
    )
    
    return rx.link(
        button,
        href=url,
        is_external=True
    )
