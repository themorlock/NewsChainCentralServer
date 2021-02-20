import flask


app = flask.Flask(__name__)
peer_addresses = set()


@app.route('/get_peer_addresses', methods=['GET'])
def home():
    return_peer_addresses = list(peer_addresses).copy()
    return_peer_addresses.remove(flask.request.remote_addr)
    peer_addresses.add(flask.request.remote_addr)
    return flask.jsonify(return_peer_addresses)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
