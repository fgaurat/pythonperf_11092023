from celery import Celery

app = Celery('hello', broker='pyamqp://guest@localhost//',backend="redis://localhost:6379/0")



def main():
    result = app.send_task("celery_worker.hello")
    print(result.ready())
    print(result.get())
if __name__=='__main__':
    main()
