import picoweb
import wifiConnect
from machine import UART

ip = wifiConnect.connect()

uart = UART(2, 9600)

app = picoweb.WebApp(__name__)

# Change the HTTP endpoint in accordance with your group ID
@app.route("/red/8")
def red(req, resp):
    # Here your code
    uart.write('80')
    print(uart.read(2))
    # You can change the message
    yield from picoweb.start_response(resp, content_type="text/html")
    yield from resp.awrite("RED")
    yield from resp.aclose()


@app.route("/green/8")
def green(req, resp):
    # Here your code
    uart.write('81')
    print(uart.read(2))
    yield from picoweb.start_response(resp, content_type="text/html")
    yield from resp.awrite("GREEN")
    yield from resp.aclose()
    pass


@app.route("/restore/8")
def restore(req, resp):
    # Here your code
    uart.write('82')
    print(uart.read(2))
    yield from picoweb.start_response(resp, content_type="text/html")
    yield from resp.awrite("RESTORE")
    yield from resp.aclose()
    pass
    
# if __name__ == '__main__':
app.run(debug=True, host = ip, port = 80)


# To check: open a web browser and go to http://<ip>:80/red/<ID>
