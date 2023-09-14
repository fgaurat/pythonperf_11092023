import requests


def main():
    url ="https://cemantix.certitudes.org/score"
    form_data = {
        "word":"contradiction"
    }
    response= requests.post(url, data=form_data)
    print(response.json())


if __name__=='__main__':
    main()
