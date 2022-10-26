import plotly_express as px
gapminder = px.data.gapminder() #läser in exempeldata från Plotly. Om har egen data så behöver köra .read bla bla bla

fig = px.scatter(
    gapminder,
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    log_x=True,
    size_max=70,
    color="country",
    animation_frame="year",
    animation_group="country",
    title = "Gapminder",
    range_y=[25,90],
    range_x=[100, 100_000]
)

fig.show() # körs härifrån så öppnas grafen automatiskt i en webläsare då kör plotlyexpress

fig.write_html("2.2_gapminder.html", auto_open = True)