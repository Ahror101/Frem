
from wsgiref.simple_server import make_server

"rasm chiqarish"
image_path = r"C:\Users\hp\Desktop\Apple-iPhone-11-64GB-A-1900.jpg"

def app(environ, start_response):
    with open(image_path, "rb") as photo_file:
        image_data = photo_file.read()
        status = "200 OK"
        headers = [("Content-type", "image/jpeg")]
        start_response(status, headers)
        return [image_data]

server = make_server("localhost", 8000, app)
print("Server ishlayapti: http://localhost:8000")
server.serve_forever()
