import flask


app = flask.Flask(__name__)
peer_addresses = set()


@app.route('/get_peer_addresses', methods=['GET'])
def home():
    return_peer_addresses = list(peer_addresses).copy()
    client_address = flask.request.remote_addr
    if client_address in return_peer_addresses:
        return_peer_addresses.remove(client_address)
    peer_addresses.add(flask.request.remote_addr)
    return flask.jsonify(return_peer_addresses)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
