from jinja2 import Template
def use_jinja2():
    t = Template("Привіт, {{ name }}!")
    print(f"Jinja2: {t.render(name='Станіслав')}")