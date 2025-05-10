import datetime

now = datetime.datetime.now()

christmas = datetime.datetime(now.year, 12, 25)

if now > christmas:
    christmas = datetime.datetime(now.year + 1, 12, 25)

delta = christmas - now
days = delta.days
hours = delta.seconds // 3600  
print(f"오늘은 {now.year}년 {now.month}월 {now.day}일입니다.")
print(f"다음 크리스마스까지는 {days}일 {hours}시간 남았습니다.")
