import pytest
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler
from port_scanner.scanner import is_port_open

@pytest.fixture
def setup():
    server = HTTPServer(("127.0.0.1", 8000), SimpleHTTPRequestHandler)
    thread = threading.Thread(target=server.serve_forever)
    thread.start()
    yield server
    server.shutdown()
    thread.join()

def test_is_port_open(setup):
    # Test with a known open port (e.g., 80 for HTTP)
    assert is_port_open(ip="127.0.0.1", port=8000) == True

def test_is_port_closed(setup):
    # Test with a known closed port (e.g., 81 for HTTPS)
    assert is_port_open(ip="127.0.0.1", port=8001) == False