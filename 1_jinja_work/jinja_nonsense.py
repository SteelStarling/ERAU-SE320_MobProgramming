from jinja2 import Environment
from json import load

with open("MobProgramming/data/jinja.json", encoding="utf-8") as file:
    context = load(file)

with open("MobProgramming/templates/host_info.jinja", encoding="utf-8") as src:
    with open("MobProgramming/public/jinja.html", mode="w", encoding="utf-8") as tgt:
        tgt.write(Environment().from_string(src.read()).render(context))

