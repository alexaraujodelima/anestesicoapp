from kivy_ios.toolchain import PythonRecipe

class AnestesicoAppRecipe(PythonRecipe):
    version = "1.0"
    url = "https://github.com/alexaraujodelima/anestesicoapp/archive/refs/heads/main.zip"
    depends = ["kivy"]
    site_packages_name = "anestesicoapp"

recipe = AnestesicoAppRecipe()
