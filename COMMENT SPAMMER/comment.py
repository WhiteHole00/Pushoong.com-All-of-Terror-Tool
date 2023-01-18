import asyncio
from playwright.async_api import async_playwright
import threading

async def isRunSpam(messsage):
    async with async_playwright() as go:
        browser = await go.firefox.launch(headless=True)
        while 1:
            try:
                bot = await browser.new_page()
                await bot.goto(f"https://pushoong.com/comment/")
                await bot.type('#content',messsage)
                await bot.type('#contact','None')
                await bot.click("#content_zone > div > div:nth-child(2) > form > button")
                await asyncio.sleep(1.5)
                print("[+] 작성완료!")
            except Exception as e:
                return input("[-] Unknown Error")
        


def main():
    thread = int(input("스레드를 적어주세요 > "))
    msg = input("도배할 말을 적어주세요 > ")

    warning = input("본 과정은 푸슝 개발자 에게 전송 되는 문의 페이지 입니다.\n도배를 하여 발생하는 모든 불이익은 본인에게 있습니다.\n그래도 진행 하시겠습니까? (Y/N) > ")

    if warning == "Y":
        for i in range(thread):
            threading.Thread(target=asyncio.run,args=(isRunSpam(msg),)).start()
    elif warning == "N":
        return input("도배를 취소 하였습니다.")
    else:
        return input("잘못된 선택 입니다.")

if __name__ == "__main__":
    main()
    

