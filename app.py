from binance.client import Client

# add your api keys 
# mine in a private file 

api_key = ''
api_secret = ''
client = Client(api_key,api_secret)

info = client.get_account()
# add it from admin.py later
persoalz =['1INCH', 50.69]

class check():
    def __init__(self):
        # creating the lists will be used in the class 
        self.all_assets = []
        self.all_prices = []
        self.asset_list = [] 
        self.assets_with_prices = {}
        self.assets_with_values = {}
        self.grand_total = 0




        self.searchu()
        self.get_prices()
        self.printu()
        self.calc()
        self.total_without_mine = 0  
        self.assets_with_values_without = {}



    def searchu(self):
        for self.moni in info['balances']: 
            # Searching if there is any balance in any currency 
            if float(self.moni['free']) >0 or float(self.moni['locked']) >0 :
                self.moni_total = float(self.moni['free']) + float(self.moni['locked'])
                self.moni_structure = f"{self.moni_total} : {self.moni['asset']} "
                self.all_assets.append(self.moni_structure)   
                # to get the available assets to use them later 
                self.asset_list.append(self.moni['asset'])   





    def get_prices(self):
        # first getting the price in btc pair than converting it because some of the currencies doesn't have usdt pair
        self.btc_price = client.get_avg_price(symbol='BTCUSDT')
        for self.cur in self.asset_list:
            # excludign the ones doesn't have btc pair
            if self.cur == 'BTC' or self.cur == 'USDT' or self.cur == 'TRY':
                pass
            else:
                # calculating the prices to btc
                self.temp_var = client.get_avg_price(symbol=f"{self.cur}BTC")
                self.price_to_btc = self.temp_var['price']  
                self.btc_price_clean = self.btc_price['price'] #cleaning the results
                self.amount = client.get_asset_balance(asset = self.cur)
                self.amount_clean = float(self.amount['free']) + float(self.amount['locked']) # cleaning the results 
                # multipling price to btc with btc with the amount 
                self.total_price = float(self.btc_price_clean) * float(self.price_to_btc) * float(self.amount_clean)
                self.assets_with_prices[self.cur] = self.total_price
                self.assets_with_values[self.cur] = self.amount_clean
                self.grand_total+= self.total_price

    def printu(self):
        
        for item in self.assets_with_prices:
            if self.assets_with_prices[item] >10:
                print(f"{item} = {self.assets_with_prices[item]}$ / {self.assets_with_values[item]} ")

        self.cleaned_total = "%.2f" % self.grand_total
        print(f"-------\n= {self.cleaned_total}$")

      

    def calc(self):
        # first calculate personalz
        self.personal = persoalz
        self.assets_with_values_without = self.assets_with_values
        print()
        print(self.assets_with_values_without)
        print()
        for item in self.assets_with_values:
            if self.personal[0] == item:
                self.temp = self.assets_with_values[item] - self.personal[1]
                self.assets_with_values_without[item] =  self.temp
                print(self.temp)
        print()
        print(self.assets_with_values_without)


        # self.zezo = self.assets_with_values_without * 0.131 
        self.btc_price_new = client.get_avg_price(symbol='BTCUSDT')
        for self.cur in self.asset_list:
            # excludign the ones doesn't have btc pair
            if self.cur == 'BTC' or self.cur == 'USDT' or self.cur == 'TRY':
                pass
            else:
                self.temp_var = client.get_avg_price(symbol=f"{self.cur}BTC")
                self.price_to_btc = self.temp_var['price']  
                self.btc_price_clean = self.btc_price['price']
                print(self.assets_with_values_without.values)



        
    


check()