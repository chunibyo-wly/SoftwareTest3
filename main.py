from flask import Flask, request
from model.Baggage import Baggage
from model.Factory import get_plan

app = Flask(__name__, static_url_path='')


@app.route('/')
def hello_world():
    return app.send_static_file('index.html')


@app.route('/baggage', methods=['POST'])
def count_baggage():
    content = request.json
    baggage = [Baggage(i['length'], i['width'], i['height'], i['weight']) for i in content['baggage']]
    rsp = get_plan(
        content['country'], content['ship'], content['price'], baggage, content['area']
    ).get_all_price()[2]
    return str(rsp)


if __name__ == '__main__':
    app.run()
