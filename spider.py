#/usr/env python3
import scrapy
from settings import OLX_URL

class OLXSpider(scrapy.Spider):
    name = "olx" 
    start_urls = [
            OLX_URL
        ] 
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0'
    }  # hack pra desafiar o site da OLX
    
    def parse(self, response):

        lista = response.xpath("/html/body/div[1]/div[2]/div[1]/div[4]/div/div[2]/div[9]/ul/li")
        valores = response.css("p.fnmrjs-16::text").getall()
        data_full = response.css("div.fnmrjs-18")
        titulos = response.css("h2.fnmrjs-10::text").getall()
        links = response.css("a.fnmrjs-0").xpath("@href").getall()
        datas = self.process_data(data_full) 
        for (d, v, t, l) in zip(datas, valores, titulos, links):
            yield {"data": d, "valor": v, "titulo": t, "url": l }
        
        n = response.css("li[selected]::text").get() # numero da pagina

        next_page = response.css("a[data-lurker-detail='next_page']").xpath("@href").get()
        if next_page is not None:
            print(f"Saindo da pagina {n}")
            yield response.follow(next_page, self.parse)
        

    def process_data(self, data_full):
        dias = data_full.xpath("./p[1]/text()").getall()
        horas = data_full.xpath("./p[2]/text()").getall()
        timestamp = [ f"{x} {y}" for (x,y) in zip(dias, horas)]
        return timestamp
