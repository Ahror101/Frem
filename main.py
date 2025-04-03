# from wsgiref.simple_server import make_server


from app import FrameWorkApp

app = FrameWorkApp()

@app.route("/home")
def home(request, response):
    response.text = "Home pagega xush kelibsz"

@app.route("/about")
def about(request, response):
    response.text = "About pagega xush kelibsz"

@app.route("/Shohruh")
def shohruh(request, response):
    response.text = "Shohruh 16 yosh. Hozir u PDP schoolda oqiydi. Men eng yaqin ortogin. Tugulgan kuni 30-aprelda. Ekallaiz shu kuni rasa kutyabmiz"


# server = make_server("localhost", 8000, app)
# server.serve_forever()