import requests
api_id="CG-7GVixdY4bxpCUcyF4QnEG2Uq"
while True:
    coin=input("Enter cryptocoin: ")
    response = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd,inr&x_cg_demo_api_key={api_id}")
    a=response.json()
    if coin in a:
        print("\nCrypto:",coin)
        print("Price:",a[coin]['usd'],"USD")
        print("Price:",a[coin]['inr'],"INR")
    else:
        print("Invalid cryptocoin!")
    b=input("Want to see more cryptocoins?(y/n): ")
    if b.lower() == "n":
        break