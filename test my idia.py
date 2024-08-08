# import library.
from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_price_ranking(text: str):
    return float(
        text.get_text()
        .replace("$", "")
        .replace("", "")
        .replace("\n", "")
        .replace(",", "")
    )


def get_name_ranking(text_name_rank: str):
    return text_name_rank.get_text().replace(",", "").replace("\n", "")


def get_price_market(text_market: str):
    return float(
        text_market.get_text()
        .replace(",", "")
        .replace("", "")
        .replace("$", "")
        .replace("\n", "")
    )


def get_name_market(text_name_mark):
    return text_name_mark.get_text().replace("", "").replace(",", "").replace("\n", "")


# open site coinranking and coinmarket.
open_site_ranking = urlopen("https://coinranking.com/")
open_site_market = urlopen("https://coinmarketcap.com/")


# read html code for two site.
read_html_code_ranking = BeautifulSoup(open_site_ranking.read(), "lxml")
read_html_code_market = BeautifulSoup(open_site_market.read(), "lxml")


# read html tag for two site.
read_html_tag_ranking = read_html_code_ranking.find_all("div", {"class": "valuta"})
read_html_tag_market = read_html_code_market.find_all(
    "div", {"class": "sc-b3fc6b7-0 dzgUIj"}
)


# read html code cryptocurrency for two site
cryptocurrency_ranking = read_html_code_ranking.find_all(
    "span", {"class": "profile__subtitle-name"}
)
cryptocurrency_market = read_html_code_market.find_all(
    "div", {"class": "sc-1c5f2868-3 hHWqgz"}
)


# # loop.
# for i in range(0, 10, 1):
#     price_ranking = get_price_ranking(read_html_tag_ranking[2 * i])
#     price_name_ranking = get_name_ranking(cryptocurrency_ranking[i])
#     print(f"coinranking{price_name_ranking}:{price_ranking}")
# print("===================================================================")
# for n in range(0, 10, 1):
#     price_name_market = get_name_market(cryptocurrency_market[n])
#     price_market = get_price_market(read_html_tag_market[n])
#     print(f"coinmarket       {price_name_market}           :{price_market}")
# print("===================================================================")
# for s in range(0, 10):
#     if price_market > price_ranking:
#         print(f"coinmarket{price_market}   >   coinranking{price_ranking}")
#     else:
#         print(f"coinmarket{price_market}    <    coinranking{price_ranking}")
price_ranking = []
price_name_ranking = []

price_name_market = []
price_market = []

# loop.
for i in range(0, 10, 1):
    price_ranking.append(get_price_ranking(read_html_tag_ranking[2 * i]))
    price_name_ranking.append(get_name_ranking(cryptocurrency_ranking[i]))
    print(f"coinranking{price_name_ranking[i]}:{price_ranking[i]}")
print("===================================================================")
for n in range(0, 10, 1):
    price_name_market.append(get_name_market(cryptocurrency_market[n]))
    price_market.append(get_price_market(read_html_tag_market[n]))
    print(f"coinmarket       {price_name_market[n]}           :{price_market[n]}")
print("===================================================================")
for s in range(0, 10):
    if price_market[s] > price_ranking[s]:
        print(f"coinmarket{price_market[s]}   >   coinranking{price_ranking[s]}")
    else:
        print(f"coinmarket{price_market[s]}    <    coinranking{price_ranking[s]}")
