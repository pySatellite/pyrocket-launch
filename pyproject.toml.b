[project]
name = "pyrocket-launch"
version = "0.3.0"
description = "Rocket Simulation Toy"
authors = [
    {name = "pysatellite", email = "pysatellite@gmail.com"},
]
dependencies = [
    "glfw>=2.6.2",
    "p5>=0.7.1",
]
requires-python = ">=3.9"
readme = "README.md"
license = {text = "MIT"}

[build-system]
requires = ["setuptools>=61", "wheel"]
build-backend = "setuptools.build_meta"

[tool.setuptools.packages.find]
# scanning for namespace packages is true by default in pyproject.toml, so
# you do NOT need to include the following line.
namespaces = true
where = ["src"]

[tool.setuptools.package-data]
"pyrocket_launch.images" = ["planet.png", "rocket.png"]


[project.urls]
"Homepage" = "https://github.com/pySatellite/pyrocket-launch"
"Bug Tracker" = "https://github.com/pySatellite/pyrocket-launch/issues"

[project.scripts]
pyrocket-launch = 'pyrocket_launch.main:run'
