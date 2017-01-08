import scrapy
# papas
class RecepiesSpider(scrapy.Spider):
    name = "papas"
    start_urls = [
        "http://contactoconlodivino.blogspot.com.ar/2013/05/papas-arrugadas-o-arrugas.html",
    ]

    def parse(self, response):
        for recepie in response.css('div.content'):
            yield {
                'titulo': recepie.css('div h3::text').extract_first(),
                'receta': recepie.css('div.MsoNormal span::text').extract(),
            }
# locro
class RecepiesSpider2(scrapy.Spider):
    name = "locro"
    start_urls = [
        "http://contactoconlodivino.blogspot.com.ar/2013/05/locro.html",
    ]

    def parse(self, response):
        for recepie in response.css('div.content'):
            a = response.css('div.content')
            b = a.xpath('//div[@class="post-body entry-content"]')
            
            yield {
                'titulo': recepie.css('h3::text').extract_first(),
                'receta': recepie.css('div.MsoNormal div::text').extract(),
                'ingredientes': recepie.css('div.MsoNormal div span::text').extract(),
                # esta es la que va
                'todo': b.css('div ::text').extract(),
            }
