# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
import json
import time
from datetime import datetime

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjdXN0SWQiOiJjWUtnckFyVjYyU3ZoUS9idW9lUlFrTGV1anJqNnNzUDE5WWg3Umc0cTNGTC9UcDYyaTExMk1DTyt1NUp2WVphTEV3eHBoRDR1Q2NydjZmUURFU3hySTcxbjhMUUdieTRQeXN6anJrWUlMVzgvSE5TQWJoeEVoVGExU2tZUVg5Ym1nbWlYek40RDYzdzZ3QUJDMEE4QVZhR3ZZRUxrcnd6bUVGcGl2MC9jazA9IiwidXNlcklkIjoiTHd5amQzR2phenYxbWlOQklCNFUvaXZvRzcvT0RGQU9kU0FVemtmRzNlMHJlYjM3UVE5WlgweXhrZklVVTRQRnY4VXlJaVdaQlRHeWxLYW9ZOEN1enJGVFJMQ3pFR0VUL1ZjaUh0TDVsVm9PNXAxSUNvWS9LS0dpLy9JSUUvYWJIeVVtYVhCTUp3d0o2djg2ZnUyZytYZFV6dUZkY3BwcmFjNllpejVGcHFBPSIsImVtcElkIjoiVkhLS2pYSHJ6Vm9zUWU0NnVuYlFLeWsrRUFWcUg0cTFycXdIbCt6TnQzV1pIU2xSMktIRFNqM0YvTS83eW56RmJ1d2sxZ3lyeStyVjQzcHhKVHBIb2xUUU1nV2hGQkFlZHBCTjFOWDMyTEdqeS95ZDdjRmZKNVBlQlZJNXZVbU80aEhkWWRlclJwVzYzdFFTNVdlb0M3M0ZBZE5vSTZoUGVxMlZDWkI2empFPSIsInRva2VuVHlwZSI6ImVtcFdlYiIsInRpbWVzdGFtcCI6MTY0MzI5MzcyODU3M30.Uf4Tcs0cNgVEJG01qZww2LT0bY0HGZL04QmaxPhbkCE"
cookie = "portal_presuuid=40289d743f0a2d14013f0a2f8e5c0001; portal_model=show; monitorCustomerKey=35bbe2bd-887a-483b-8ff7-1786556ff935-20210904113900; actionSum=1; notShow=false; RoneUserName=283387; ispass=false; 6e3605d41037445487a9f7d09bfe4150=WyIyOTM0MTEyODUxIl0; webfunny_ip=112.4.44.194; webfunny_province=%E6%B1%9F%E8%8B%8F%E7%9C%81%E5%8D%97%E4%BA%AC%E5%B8%82; notifylobnumber=283387; sessionid=w72e2m6ourowlh4g1hum3umnkkjqaitb; ROLTPAToken=PExUUEFUb2tlbj48bm9kZT5SMUZyYW1ld29yazQuMDwvbm9kZT48cGVyc29udXVpZD40MDI4ODFjNDc5NDI5MzMyMDE3YWVlMGU2ZjllNDM5ODwvcGVyc29udXVpZD48c3lzaWQ%2BMjwvc3lzaWQ%2BPHRpbWU%2BMTY0MzI5MzcyNTE2NzwvdGltZT48dXNlcmlkPjI4MzM4NzwvdXNlcmlkPjwvTFRQQVRva2VuPg%3D%3D; mannjuToken=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJtYW5uanUiLCJwYXNzd29yZCI6InpyZ2pfMDAxIiwiaWQiOiIyODMzODciLCJpYXQiOjE2NDMyNzg5OTMsImp0aSI6ImE4ZmJjOWViLWU4OTAtNGJhNC04MzBkLWQwNzMxMzE2ZTU0YSIsInVzZXJuYW1lIjoibWFubmp1In0.ilvcoK5ekQZctkFT43SPXzACziGB3OExV7SQt7e8izU; fullName=5qKB5ZaE; JSESSIONID=0A5B2090E504289F40D2E7708EA8AE4D; UserToken=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjdXN0SWQiOiJjWUtnckFyVjYyU3ZoUS9idW9lUlFrTGV1anJqNnNzUDE5WWg3Umc0cTNGTC9UcDYyaTExMk1DTyt1NUp2WVphTEV3eHBoRDR1Q2NydjZmUURFU3hySTcxbjhMUUdieTRQeXN6anJrWUlMVzgvSE5TQWJoeEVoVGExU2tZUVg5Ym1nbWlYek40RDYzdzZ3QUJDMEE4QVZhR3ZZRUxrcnd6bUVGcGl2MC9jazA9IiwidXNlcklkIjoiTHd5amQzR2phenYxbWlOQklCNFUvaXZvRzcvT0RGQU9kU0FVemtmRzNlMHJlYjM3UVE5WlgweXhrZklVVTRQRnY4VXlJaVdaQlRHeWxLYW9ZOEN1enJGVFJMQ3pFR0VUL1ZjaUh0TDVsVm9PNXAxSUNvWS9LS0dpLy9JSUUvYWJIeVVtYVhCTUp3d0o2djg2ZnUyZytYZFV6dUZkY3BwcmFjNllpejVGcHFBPSIsImVtcElkIjoiVkhLS2pYSHJ6Vm9zUWU0NnVuYlFLeWsrRUFWcUg0cTFycXdIbCt6TnQzV1pIU2xSMktIRFNqM0YvTS83eW56RmJ1d2sxZ3lyeStyVjQzcHhKVHBIb2xUUU1nV2hGQkFlZHBCTjFOWDMyTEdqeS95ZDdjRmZKNVBlQlZJNXZVbU80aEhkWWRlclJwVzYzdFFTNVdlb0M3M0ZBZE5vSTZoUGVxMlZDWkI2empFPSIsInRva2VuVHlwZSI6ImVtcFdlYiIsInRpbWVzdGFtcCI6MTY0MzI5MzcyODU3M30.Uf4Tcs0cNgVEJG01qZww2LT0bY0HGZL04QmaxPhbkCE; Account=17551795607; roleType=1; UserId=283387"
month = "2022-01"
monthDayStart = 1
monthDayEnd = 31
holTime = 2.5


def _get_request(data: object) -> object:
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
        "Content-Type": "application/json;charset=UTF-8",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "token": token,
        "sec-ch-ua-platform": "Windows",
        "Origin": "https://ics.chinasoftinc.com:18010",
        "Referer": "https://ics.chinasoftinc.com:18010/",
        "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8",
        "Cookie": cookie
    }
    response = requests.post("https://ics.chinasoftinc.com:18010/ehr_saas/web/attEmpLog/getAttEmpLogByEmpId2.empweb?",
                             data=data,
                             headers=header)
    return response.json()


def calculate(start, end):
    num = 0
    startTime = datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
    sb = datetime(startTime.year, startTime.month, startTime.day, 8)
    if sb > startTime:
        startTime = sb
    endTime = datetime.strptime(end, "%Y-%m-%d %H:%M:%S")

    xb1 = datetime(startTime.year, startTime.month, startTime.day, 17, 30)
    xb2 = datetime(startTime.year, startTime.month, startTime.day, 18, 00)
    if endTime > xb1 and endTime < xb2:
        endTime = xb1

    if endTime > xb2:
        num = -0.5

    work = endTime - startTime
    hour = work.total_seconds() / 3600 + num - 1.5
    return float(hour)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    dayNum = 0
    hourNum = 0

    for i in range(monthDayStart, monthDayEnd):
        response = _get_request(json.dumps({"dt": month + "-" + str(i) + " 00:00:00"}))
        dtDetailList = response['result']['data']['attEmpDetail']['dtDetailList']
        if dtDetailList[0]['sbTitle'] == "上班":
            dayNum += 1
            start = response['result']['data']['attEmpDetail']['checkIn2']
            end = response['result']['data']['attEmpDetail']['checkOut2']
            workTime = calculate(start, end)
            hourNum += workTime
            print("打卡时间" + start + "---" + end + "工作时长:" + str(workTime))
        time.sleep(0.2)
    print("工作天数", dayNum)
    print("工作小时", hourNum)
    print("总需要 day*8", dayNum * 8)
    print("总需要加班 day*9", dayNum * 9)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
