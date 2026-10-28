import requests

# Dicionário com as 50 APIs
APIS = {
    # 1. Informações sobre países
    "1": ("Países", "https://restcountries.com/v3.1/name/brasil"),
    # 2. Pokémon
    "2": ("Pokémon", "https://pokeapi.co/api/v2/pokemon/pikachu"),
    # 3. Cachorros
    "3": ("Imagens de cachorros", "https://dog.ceo/api/breeds/image/random"),
    # 4. Gatos
    "4": ("Imagens de gatos", "https://api.thecatapi.com/v1/images/search"),
    # 5. Conselhos aleatórios
    "5": ("Conselhos", "https://api.adviceslip.com/advice"),
    # 6. Fatos sobre gatos
    "6": ("Fatos sobre gatos", "https://catfact.ninja/fact"),
    # 7. Citações
    "7": ("Citações", "https://zenquotes.io/api/random"),
    # 8. Atividades aleatórias
    "8": ("Atividades", "https://bored-api.appbrewery.com/random"),
    # 9. Piadas
    "9": ("Piadas", "https://official-joke-api.appspot.com/random_joke"),
    # 10. Universidades
    "10": ("Universidades", "http://universities.hipolabs.com/search?country=Brazil"),
    # 11. Dados de IP
    "11": ("IP público", "https://api.ipify.org?format=json"),
    # 12. Informações de IP
    "12": ("Geolocalização de IP", "https://ipapi.co/json/"),
    # 13. CEP brasileiro
    "13": ("CEP", "https://viacep.com.br/ws/01001000/json/"),
    # 14. Dados de feriados
    "14": ("Feriados", "https://date.nager.at/api/v3/PublicHolidays/2026/BR"),
    # 15. Países e capitais
    "15": ("Capital", "https://restcountries.com/v3.1/capital/brasilia"),
    # 16. Dados de astronomia
    "16": ("Astronomia NASA", "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"),
    # 17. ISS
    "17": ("Estação Espacial", "https://api.wheretheiss.at/v1/satellites/25544"),
    # 18. Notícias Hacker News
    "18": ("Hacker News", "https://hacker-news.firebaseio.com/v0/topstories.json"),
    # 19. Livros
    "19": ("Livros", "https://openlibrary.org/search.json?q=python"),
    # 20. Filmes
    "20": ("Filmes", "https://www.omdbapi.com/?t=batman&apikey=thewdb"),
    # 21. Jogos
    "21": ("Jogos", "https://www.freetogame.com/api/games"),
    # 22. Conselhos de programação
    "22": ("Programação", "https://api.adviceslip.com/advice"),
    # 23. Repositórios GitHub
    "23": ("GitHub", "https://api.github.com/repos/python/cpython"),
    # 24. Usuário aleatório
    "24": ("Usuário aleatório", "https://randomuser.me/api/"),
    # 25. Gerador de UUID
    "25": ("UUID", "https://httpbin.org/uuid"),
    # 26. Dados de teste
    "26": ("JSON de teste", "https://jsonplaceholder.typicode.com/posts/1"),
    # 27. Comentários
    "27": ("Comentários", "https://jsonplaceholder.typicode.com/comments/1"),
    # 28. Fotos
    "28": ("Fotos", "https://jsonplaceholder.typicode.com/photos/1"),
    # 29. Tarefas
    "29": ("Tarefas", "https://jsonplaceholder.typicode.com/todos/1"),
    # 30. Usuários de teste
    "30": ("Usuários", "https://jsonplaceholder.typicode.com/users/1"),
    # 31. Posts de teste
    "31": ("Posts", "https://jsonplaceholder.typicode.com/posts"),
    # 32. Países e moedas
    "32": ("Moedas", "https://open.er-api.com/v6/latest/USD"),
    # 33. Bitcoin
    "33": ("Bitcoin", "https://api.coinbase.com/v2/prices/BTC-USD/spot"),
    # 34. Ethereum
    "34": ("Ethereum", "https://api.coinbase.com/v2/prices/ETH-USD/spot"),
    # 35. Criptomoedas
    "35": ("Criptomoedas", "https://api.coingecko.com/api/v3/ping"),
    # 36. Clima
    "36": ("Clima", "https://api.open-meteo.com/v1/forecast?latitude=-3.72&longitude=-38.53&current=temperature_2m"),
    # 37. Previsão do tempo
    "37": ("Previsão", "https://api.open-meteo.com/v1/forecast?latitude=-3.72&longitude=-38.53&daily=temperature_2m_max,temperature_2m_min&timezone=America%2FFortaleza"),
    # 38. Países por região
    "38": ("Países da Europa", "https://restcountries.com/v3.1/region/europe"),
    # 39. Arte
    "39": ("Arte", "https://api.artic.edu/api/v1/artworks/4"),
    # 40. Museu
    "40": ("Museu", "https://collectionapi.metmuseum.org/public/collection/v1/objects/1"),
    # 41. Pokémon por número
    "41": ("Pokémon número 25", "https://pokeapi.co/api/v2/pokemon/25"),
    # 42. Personagens de Rick and Morty
    "42": ("Rick and Morty", "https://rickandmortyapi.com/api/character/1"),
    # 43. Episódios de Rick and Morty
    "43": ("Episódios", "https://rickandmortyapi.com/api/episode/1"),
    # 44. Personagens de anime
    "44": ("Anime", "https://api.jikan.moe/v4/anime?q=naruto&limit=5"),
    # 45. Jogos de xadrez
    "45": ("Xadrez", "https://api.chess.com/pub/player/hikaru"),
    # 46. Informações de domínio
    "46": ("Domínio", "https://rdap.org/domain/example.com"),
    # 47. Conversão de texto em código Morse
    "47": ("Morse", "https://api.funtranslations.com/translate/morse.json?text=ola"),
    # 48. Texto em Yoda
    "48": ("Yoda", "https://api.funtranslations.com/translate/yoda.json?text=ola"),
    # 49. Gatos HTTP
    "49": ("HTTP Cats", "https://http.cat/200"),
    # 50. Teste de conexão HTTP
    "50": ("HTTPBin", "https://httpbin.org/get"),
}


def consultar_api(numero):
    if numero not in APIS:
        print("API inválida!")
        return

    nome, url = APIS[numero]

    print(f"\nConsultando: {nome}")
    print(f"URL: {url}\n")

    # Adicionado User-Agent para evitar bloqueios (ex: GitHub API)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) CentralAPIsPython"
    }

    try:
        resposta = requests.get(url, headers=headers, timeout=15)
        resposta.raise_for_status()

        tipo = resposta.headers.get("Content-Type", "")

        if "application/json" in tipo:
            print("Resultado:")
            print(resposta.text[:12000])
        else:
            print("Resposta:")
            print(resposta.text[:2000])

    except requests.RequestException as erro:
        print(f"Erro ao consultar a API: {erro}")


def menu():
    while True:
        print("\n" + "=" * 40)
        print("        CENTRAL DE 50 APIS")
        print("=" * 40)

        # Ordena as chaves numericamente para exibir de 1 a 50 perfeitamente
        chaves_ordenadas = sorted(APIS.keys(), key=int)

        for numero in chaves_ordenadas:
            nome, _ = APIS[numero]
            print(f"{numero:>2} - {nome}")

        print(" 0  - Sair")

        escolha = input("\nEscolha uma API: ").strip()

        if escolha == "0":
            print("Até mais!")
            break

        consultar_api(escolha)


if __name__ == "__main__":
    menu()
