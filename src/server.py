import flask


app = flask.Flask(__name__)
peer_addresses = set()


@app.route('/get_peer_addresses', methods=['GET'])
def home():
    return_peer_addresses = list(peer_addresses).copy()
    peer_addresses.add(flask.request.remote_addr)
    return flask.jsonify(return_peer_addresses[:int(flask.request.args.get("n"))])


if __name__ == '__main__':
    app.run()
