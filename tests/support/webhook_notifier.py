# pylint: disable=locally-disabled, missing-class-docstring, missing-function-docstring, redefined-outer-name, too-few-public-methods, missing-module-docstring, global-statement

from flask import Flask, Response, request

from fishjam import receive_binary

app = Flask(__name__)
QUEUES = None


@app.route("/", methods=["GET"])
def respond_default():
    return Response(status=200)


@app.route("/webhook", methods=["POST"])
def respond_root():
    data = request.get_data()
    msg = receive_binary(data)
    if msg is not None:
        for q in QUEUES.values():
            q.put(msg)

    return Response(status=200)


def run_server(queues):
    global QUEUES
    QUEUES = queues
    app.run(port=5000, host="0.0.0.0", use_reloader=False, debug=False, threaded=True)
