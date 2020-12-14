import os

for i in range (366):
    d =str(i) + 'days ago'
    with open('bot.txt','a') as file:
        file.write(d+'\n')
        os.system('git add bot.txt')
        os.system('git commit --date="exit'+d+'" -m "Yet another commit here"')

os.system('git push -u oridin master')