# To fix 
# 1. The pairs in line 53

from binance.client import Client
import secret
import percent

#api keys 
api_key = secret.key
api_secret = secret.secret

client = Client(api_key,api_secret)

info = client.get_account()

# personals asssets (gotta be chosen from gui) temp
persoalz =['1INCH', 50.69]

class check():
    def __init__(self):
        self.btc_price = float(client.get_avg_price(symbol= "BTCUSDT")['price'])
# ========================================     
        self.asset_list = []
        self.search()  
# ========================================
        self.assets_with_amount = {}
        self.assets_with_price = {}
        self.grand_total = 0 
        self.get_prices()
# ========================================  
        self.assets_with_amount_last = {}
        self.assets_with_price_last = {}
        self.clone()  
# ======================================== 
        self.grand_total_last = 0
        self.calculate()
# ========================================
        self.ppl_list = [percent.H,percent.Z,percent.F,percent.S,percent.M]
        self.printu()

# ========================================

    def search(self):
        for self.moni in info['balances']:
            #getting the asset list 
            if float(self.moni['free']) > 0 or float(self.moni['locked']) > 0:
                self.asset_list.append(self.moni['asset'])

# ========================================

    def get_prices(self):
        for self.asset in self.asset_list:
            # The pairs that doesn't have btc equivalent
            if self.asset == 'BTC' or self.asset == 'USDT' or self.asset == 'TRY':
                pass
            else:
                # getting the asset amount 
                self.asset_to_btc = float(client.get_avg_price(symbol=f"{self.asset}BTC")['price'])
                self.asset_amount = float(client.get_asset_balance(asset=self.asset)['free']) + float(client.get_asset_balance(asset=self.asset)['locked'])
                self.assets_with_amount[self.asset] = self.asset_amount

                # getting the asset value 
                self.asset_price  = float(self.btc_price * self.asset_to_btc * self.asset_amount)
                self.assets_with_price [self.asset] = self.asset_price
                self.grand_total += self.asset_price 

# ========================================

    def calculate(self):
        # calculate the money excluding the personal amount
        
        # get the personal amount 
        self.personal_to_btc = float(client.get_avg_price(symbol= f"{persoalz[0]}BTC")['price'])
        self.personal_price = float(self.btc_price * self.personal_to_btc * persoalz[1])

        # cloning the dics
        self.assets_with_amount_last[persoalz[0]] -= persoalz[1]             
        self.assets_with_price_last[persoalz[0]] -= self.personal_price
        self.grand_total_last = self.grand_total - self.personal_price


# ========================================

    def clone(self):
        for item in self.asset_list:  
            if item == 'BTC' or item == 'USDT' or item == 'TRY':
                pass
            else:
                self.assets_with_amount_last[item] = self.assets_with_amount[item]
                self.assets_with_price_last[item] = self.assets_with_price[item]
    
# ========================================

    def printu(self):
        #the view port 
        for item in self.assets_with_price:
            if self.assets_with_price[item] >10:
                print(f"{item} = {self.assets_with_price[item]}$ / {self.assets_with_amount[item]} ")
                
        self.cleaned_total = "%.2f" % self.grand_total
        print(f"-------\n= {self.cleaned_total}$")
        print('\n\n\n=======')       
        # ================= 
        print("After Removing Personal")
        for item in self.assets_with_price_last:
            if self.assets_with_price_last[item] >10:
                print(f"{item} = {self.assets_with_price_last[item]}$ / {self.assets_with_amount_last[item]} ")

        self.cleaned_total_last = "%.2f" % self.grand_total_last
        print(f"-------\n= {self.cleaned_total_last}$")
        print(f'Personal is {self.personal_price}$ ')
        print('\n=======')
      
      
# ========================================



check()


# To Add: 
# admin panel
# - specify each inverstor's percentage 
# - specify my personal (with drop menu for the thingie)
# their login
# graphlike thingie to see PnL
# Maybe Goals for each currency 