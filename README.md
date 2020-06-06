# olx-scrapy
Spider para fazer um webcrawling no site da OLX.

# Como usar

- Instale as dependências do `requirements.txt` com `$ pip install -r requirements.txt`
- Ajuste as configurações do `settings.py`, especificando a URL da página que desejas pesquisar. 
  A página deve ser uma página de resultados de pesquisa. A recomendação é sempre filtrar a 
  pesquisa por cidade, para evitar baixar muitas páginas de resultados.
- Execute o `$ ./run.sh`, que ira executar os scripts `downloader.py` e `converter.py` com as 
  configurações padrão. 
  
 Para mais informações sobre os scripts, use `$ python <script> --help`
