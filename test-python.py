import datetime,time
def main():
    start_time=datetime.datetime.utcnow()
    print("welcome")
    for i in range(0,3):
        time.sleep(1)
    end_time=datetime.datetime.utcnow()
    print("performance={}".format(end_time-start_time))

if __name__=='__main__':
    main()