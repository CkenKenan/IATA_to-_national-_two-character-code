import requests


from lxml import etree

def init():


    url = "http://doc.chacuo.net/iso-3166-1"

    payload = {}
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Cookie': '__yjs_duid=1_5fd111c6e8af85f0832bfc72ba5403121660653882538; yjs_js_security_passport=1a312a98dd92fbf8dff940ef032ab6f25368bb0b_1660653884_js; Hm_lvt_ef483ae9c0f4f800aefdf407e35a21b3=1660653885; __gads=ID=952c029dd115945c-22e197db9cd500e6:T=1660653885:RT=1660653885:S=ALNI_MYPhw7_qVQuYchTyoM09tGeO-gjvw; __gpi=UID=000008ab1a5611a4:T=1660653885:RT=1660653885:S=ALNI_Maz9pWKX8U9q-hrM137ZOa8Ua9r6A; Hm_lpvt_ef483ae9c0f4f800aefdf407e35a21b3=1660654663',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://doc.chacuo.net/iso-3166-1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    html = etree.HTML(response.text)

    place = html.xpath('//*[@id="main"]/div[2]/table/tbody/tr/td[6]/text()')
    two_code = html.xpath('//*[@id="main"]/div[2]/table/tbody/tr/td[1]/text()')
    dic = dict(zip(place,two_code))
    dic['中国']='CN'
    return dic


def get_national_name(x):
    import requests

    url = "https://jichang.gjcha.com/jichang/"+x+".html"

    payload = {}
    headers = {
        'authority': 'jichang.gjcha.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cookie': 'Hm_lvt_2be8a8b6a88aeec60e4767195cfee53f=1660653934; __gads=ID=f1bf8a90eba5d176-221e6c4f9ed50011:T=1660653933:RT=1660653933:S=ALNI_MZ1-_Vp3JkVPxthuyNKLujb5GpJnw; __gpi=UID=000008ab1e571670:T=1660653933:RT=1660653933:S=ALNI_MadBRRm7bHv6ci_m3J9lnD7YAK_PA; Hm_lpvt_2be8a8b6a88aeec60e4767195cfee53f=1660653994',
        'referer': 'https://jichang.gjcha.com/so/csx__jichang/',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    html = etree.HTML(response.text)

    name = html.xpath('/html/body/div[2]/div/div[1]/div[1]/div/div/ul/li[4]/text()')
    return name


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    dic = init()
    while 1 :
        iata = input()
        name = get_national_name(iata)
        print(dic[name[0]])



