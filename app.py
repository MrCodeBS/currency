from flask import Flask, request, render_template, jsonify
import requests
import urllib.request, json


app = Flask(__name__)

API_KEY = 'cur_live_kr89NJnCcF9HcUk9z9IkKNMR0AOmqCYPd4UE1d4h'
API_ENDPOINT = 'https://api.currencyapi.com/v3/latest?apikey=cur_live_kr89NJnCcF9HcUk9z9IkKNMR0AOmqCYPd4UE1d4h&currencies={}&base_currency={}'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.form.get('action2'):
        print ("test")
    return render_template('index.html', context={'result': 'asdf'})

@app.route('/get_exchange_rate', methods=['GET'])
def get_exchange_rate():
    if request.method == "GET":
        amount = request.args.get("Amounttext")
        baseCurrency = request.args.get("baseCurrency")
        targetCurrency = request.args.get("targetCurrency")

        print(amount)
        print(targetCurrency)
        print(baseCurrency)

        response = urllib.request.urlopen(API_ENDPOINT.format(targetCurrency, baseCurrency))
        data = response.read()
        dict = json.loads(data)
        #response = requests.get(f'{API_ENDPOINT}&from={baseCurrency}&to={targetCurrency}')
        print (dict)
        if response.code == 200:
            try:
                exchange_rate = dict["data"][targetCurrency]["value"]
                converted_amount = float(amount) * exchange_rate #calculate converted amount
                print (converted_amount)
                return render_template('index.html', amount=amount, baseCurrency=baseCurrency, targetCurrency=targetCurrency, result ='Converted Amount: {:.2f} {}'.format(converted_amount, targetCurrency))
                #return jsonify({'exchange_rate': exchange_rate}) 
            except KeyError:
                return jsonify({'error': 'Exchange rate not found for the target currency'}), 404
        else:
            return jsonify({'error': 'Failed to retrieve exchange rate'}), response.code
        
if __name__ == '__main__':
    app.run(debug=True)
#blyat