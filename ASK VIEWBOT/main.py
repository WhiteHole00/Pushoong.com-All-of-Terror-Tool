import threading
import requests
import asyncio
async def isView(target,cnt):

    cnt = int(cnt)
    if isRunViewBot(target) == True:
        for _ in range(1,cnt+1):
            r = requests.get(f"https://pushoong.com/ask/{target}")
            #print("[SUCCESS] | {}".format(cnt))
        return input("작업이 완료 되었습니다.")
    else:
        return input("없는 유저 일거임")



def isCheck(user_id):
        r = requests.get(f"https://pushoong.com/ask/{user_id}")

        if r.status_code == 200:
            print(f"[+] {user_id} is exist!")
            return True

        else:
            return False


def main():
    id_ = input("유저 고유 아이디를 적어주세요 (ex.1234567890) > ")
    cnt = input("횟수를 적어주세요 > ")

    
    if len(id_) != 10 :
        return input("푸슝 아이디는 10 자리 입니다.")
    else:
        threading.Thread(target=asyncio.run,args=(isRunViewBot(id_,cnt),)).start()

if __name__ == "__main__":
    main()
    

