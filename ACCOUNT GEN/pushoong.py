import time
import asyncio
from playwright.async_api import async_playwright
from random_username.generate import generate_username

async def isAccGen():
    name = generate_username(1)[0]
    email = f"{generate_username(1)[0]}@whitehole.xyz"
    pw = "whwjwhwhwwhwh!!!!!!!!"
    async with async_playwright() as go:
        browser = await go.firefox.launch(headless=True)
        try:
            page = await browser.new_page()
            await page.goto("https://pushoong.com/accounts/join?next=/balance/")
            await page.type("#email",email) #password
            await page.type("#password",pw)
            await page.type("#password2",pw)
            await page.type("#nickname",name)
            await asyncio.sleep(1.5)
            await page.click("#submit")
            await page.click("#content_zone > div > div > a.btn.btn-light.btn-block.btn-lg")

            await asyncio.sleep(3)
            await page.reload()
            await page.close()

            print(f"EMAIL : {email}\nPW : {pw}")

            r = open("accounts.txt","w")
            r.writelines("ID : {} | PW : {} | EMAIL : {} | Made By WhiteHole".format(name,pw,email))
            r.close()
            return input("계정 생성이 완료 되었습니다.")
        except Exception as e:
            return print("알 수 없는 오류가 발생하였습니다.")

asyncio.run(isAccGen())
