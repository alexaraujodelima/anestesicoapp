from kivy_ios.toolchain import PythonRecipe

class AnestesicoAppRecipe(PythonRecipe):
    version = "1.0"
    depends = ["kivy"]
    site_packages_name = "anestesicoapp"
    
    # Adicione a variável url
    url = "https://github.com/username/anestesicoapp/archive/refs/heads/main.zip"  # Substitua pela URL correta do seu repositório

recipe = AnestesicoAppRecipe()
