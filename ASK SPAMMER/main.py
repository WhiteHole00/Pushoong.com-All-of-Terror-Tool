import time
import asyncio
from playwright.async_api import async_playwright
import requests
import threading

async def isRunSpam(user_id,messsage):
    async with async_playwright() as go:
        browser = await go.firefox.launch(headless=True)
        ck = isCheck(user_id)
        if ck == True:
            while 1:
                try:
                    bot = await browser.new_page()
                    await bot.goto(f"https://pushoong.com/ask/{user_id}")
                    await bot.click("#hide-modal-long") #광고 제거
                    await bot.type("#ask_textarea" , messsage)
                    await bot.click("#ask_send.send_button")
                    await asyncio.sleep(1.5)
                    print("[+] Success")
                except Exception as e:
                    return input("[-] Unknown Error")
        else:
            return input(f"[-] {user_id} is not found user or not exist page")


def isCheck(user_id):
        r = requests.get(f"https://pushoong.com/ask/{user_id}")

        if r.status_code == 200:
            print(f"[+] {user_id} is exist!")
            return True

        else:
            return False


def main():
    id_ = input("유저 고유 아이디를 적어주세요 (ex.1234567890) > ")
    thread = int(input("스레드를 적어주세요  > "))
    msg = input("도배할 말을 적어주세요 > ")

    
    if len(id_) > 10 or len(id_) < 10 :
        return input("푸슝 아이디는 10 자리 입니다.")
    else:
        for i in range(thread):
            threading.Thread(target=asyncio.run,args=(isRunSpam(id_,msg),)).start()

if __name__ == "__main__":
    main()
    

