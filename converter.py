import pandas as pd
from datetime import date, timedelta
import re
import click

def valor_replacer(valor):
    return int(valor.strip("R$ ").replace(".", "")) 

def date_replacer(string): 
    hoje = date.today()
    ontem = hoje - timedelta(1)
    string = string.replace("Hoje", hoje.isoformat()) 
    string = string.replace("Ontem", ontem.isoformat()) 
    match = re.match(r"(\d{1,2}) (\w{3})", string)
    if match:
        meses = ["jan", "fev", "mar", "abr", "mai", "jun", 
        "jul", "ago", "set", "out","nov", "dez"]
        meses_dict = {val: k+1 for k, val in enumerate(meses)}
        dia, mes = match.groups()
        data = date(2020, meses_dict[mes], int(dia))
        string = string.replace(f"{dia} {mes}", data.isoformat())

    return string


@click.command()
@click.option("-i","--input", type=click.Path(),default="database.json",
    help="Caminho para o .json que o scrapy baixou.",
)
@click.option('-c', '--count', default=100, help='Quantidade de registros para exportar pro .csv')
@click.option("-o", "--output", type=click.Path(), default="database.csv",
help="Caminho para o .csv com os resultados selecionados"
)
def converter(input,count,output): 
    df = pd.read_json(input)
    df.valor = df.valor.apply( valor_replacer ) 
    df.data = df.data.apply( date_replacer )
    df.data = pd.to_datetime(df.data)
    sample = df.head(n=count).copy()
    sample.to_csv(output)


if __name__ == "__main__":
    converter()
