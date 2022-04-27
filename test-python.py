import datetime,time
def main():
    start_time=datetime.datetime.utcnow()
    print("hello world")
    time.sleep(3)
    end_time=datetime.datetime.utcnow()
    print("performance={}".format(end_time-start_time))

if __name__=='__main__':
    main()