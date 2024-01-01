## 1. Install Flask dependencies

    pipenv shell
    pipenv install flask

## 2. Run it

    flask --app app run

## 3. Flags

Specify the port:

    flask --app app run --port=8080

## 4. Routes

Open the following routes with your browser:

    http://127.0.0.1:8080/                  # Welcome
    http://127.0.0.1:8080/How%20are%20you   # I'm fine, how about you? (Case sensitive)
    http://127.0.0.1:8080/about             # I'm just a small Flask app :)
    http://127.0.0.1:8080/info              # I have been created just to pass Pau's subject.
