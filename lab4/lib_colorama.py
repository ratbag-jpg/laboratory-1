from colorama import Fore, init
def use_colorama():
    init(autoreset=True)
    print(Fore.CYAN + "colorama: Це текст блакитного кольору.")