from .cli import app
import air
import uvicorn

app = air.Air()
packages = ['feldroy/air', 'feldroy/air-cli', 'feldroy/air-convert', 'feldroy/air-markdown', 'feldroy/airdocs', 'feldroy/AirPackages', 'kentro-tech/EidosUI',]
examples = ['kentro-tech/web-dev-patterns', 'ndanielsen/air-address-demo',]


@app.get("/")
async def index():
    return air.layouts.mvpcss(
        air.H1("AirPackages"),
        air.P("A directory of libraries, tools, reusable components, and example Air sites to help you with your Air projects"),
        air.H2("Packages"),
        air.Ul(
            *[air.Li(air.A(package, href=f"https://github.com/{package}")) for package in packages]),
        air.H2("Examples"),
        air.Ul(
            *[air.Li(air.A(example, href=f"https://github.com/{example}")) for example in examples]),
        air.H2("Contributing"),
        air.P("This directory is a community effort to collect useful Air packages and examples. If you have a package or example you'd like to add, please submit a pull request to:"),
        air.A("https://github.com/feldroy/AirPackages", href="https://github.com/feldroy/AirPackages")
    )


if __name__ == "__main__":
    uvicorn.run("AirPackages.__main__:app", reload=True)
