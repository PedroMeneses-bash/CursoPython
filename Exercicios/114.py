#import webbrowser
import urllib.request

try:
    site = urllib.request.urlopen("http://www.pudim.com.br")
except:
    print('Não foi possivel acessar o site.')
else:
    print('Acesso concluído.')
