import asyncio
from playwright.async_api import async_playwright
import requests
import os

async def isParser(user_id):
    asyncio.sleep(1)
    os.system("cls")
    async with async_playwright() as go:
        browser = await go.firefox.launch(headless=True)
        ck = isCheck(user_id)
        if ck == True:
                try:
                    bot = await browser.new_page()
                    await bot.goto(f"https://pushoong.com/ask/{user_id}")
                    await bot.click("#hide-modal-long") #광고 제거
                    await bot.click("#more_button")
                    name__ = await bot.query_selector('xpath=//*[@id="content_zone"]/div[1]/div/div[2]/div[2]/h4')
                    real_name = await name__.inner_text()
                    dec__ = await bot.query_selector('xpath=//*[@id="content_zone"]/div[1]/div/div[2]/div[3]')
                    real_dec = await dec__.inner_text()
                    view__ = await bot.query_selector('xpath=//*[@id="content_zone"]/div[1]/div/div[3]/div[1]/span[2]')
                    real_view = await view__.inner_text()
                    ask__ = await bot.query_selector('xpath=//*[@id="content_zone"]/div[1]/div/div[3]/div[2]/span[2]')
                    real_ask = await ask__.inner_text()
                    answer__ = await bot.query_selector('xpath=//*[@id="content_zone"]/div[1]/div/div[3]/div[3]/span[2]')
                    real_answer = await answer__.inner_text()
                    await asyncio.sleep(1.5)
                    msg = f"""
                    아이디 : {user_id}

                    이름 : {real_name}

                    설명 : {real_dec}

                    조회수 : {real_view}개

                    질문 수 : {real_ask}개

                    답변 완료 : {real_answer}개
                    """
                    print(msg)
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

    
    if len(id_) != 10 :
        return input("푸슝 아이디는 10 자리 입니다.")
    else:
        print("파싱을 시작합니다..")
        asyncio.run(isParser(id_))

if __name__ == "__main__":
    main()
    

