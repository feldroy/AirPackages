from .cli import app
import air

app = air.Air()


@app.get("/")
async def index():
    return air.layouts.mvpcss(
        air.H1("AirPackages"),
        air.P("A directory of libraries, tools, reusable components, and example Air sites to help you with your Air projects")
    )


if __name__ == "__main__":
    app()
