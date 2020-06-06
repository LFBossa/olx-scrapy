from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from spider import OLXSpider
import click

@click.command()
@click.option("-o","--output", type=click.Path(),default="database.json",
    help="Caminho para o .json .",
)
def run_spider(output):
    # vamos fazer a saída para um arquivo 
    sets ={
     "FEEDS": {
            output: {
            'format': 'json',
            'encoding': 'utf8',
            'indent': 2
            }
        }
    }   
    process = CrawlerProcess(settings=sets) 
    process.crawl(OLXSpider)
    process.start() 
if __name__ == "__main__":
    run_spider()