import asyncio
from playwright.async_api import async_playwright
import threading

async def isRunSpam(messsage):
    async with async_playwright() as go:
        browser = await go.firefox.launch(headless=False)
        while 1:
            try:
                bot = await browser.new_page()
                await bot.goto(f"https://pushoong.com/test/create")
                await bot.type('#test_create_form > div:nth-child(1) > div:nth-child(2) > input',messsage)
                await bot.type('#test_create_form > div:nth-child(2) > div:nth-child(2) > input',messsage)
                await bot.type('#test_option_col > div > div.col.test_option_text_col > textarea',messsage)
                await bot.click("#create_button")
                await asyncio.sleep(1.5)
                print("[+] 테스트 게시물 작성 완료!")
            except Exception as e:
                return input("[-] Unknown Error")
        


def main():
    thread = int(input("스레드를 적어주세요 > "))
    msg = input("도배할 말을 적어주세요 > ")


    for i in range(thread):
        threading.Thread(target=asyncio.run,args=(isRunSpam(msg),)).start()

if __name__ == "__main__":
    main()
    

