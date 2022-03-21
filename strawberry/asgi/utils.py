import pathlib


def get_graphiql_html() -> str:
    here = pathlib.Path(__file__).parents[1]
    path = here / "static/graphiql.html"

    template = pathlib.Path(path).read_text()
    return template.replace("{{ SUBSCRIPTION_ENABLED }}", "true")
