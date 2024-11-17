from flask import Flask, Response
import json

app = Flask(__name__)
@app.route('/alkuluku/<luku>')
def alkuluku(luku):
    try:
        luku = int(luku)
        if luku <= 1:
            alkuluku = False
        elif luku <= 3:
            alkuluku = True
        elif luku % 2 == 0 or luku % 3 == 0:
            alkuluku = False
        else:
            alkuluku = True
            i = 5
            while i * i <= luku:
                if luku % i == 0 or luku % (i + 2) == 0:
                    alkuluku = False
                    break
                i += 6

        tilakoodi = 200
        vastaus = {
            "luku": luku,
            "alkuluku": alkuluku
        }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen yhteenlaskettava"
        }

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status" : "404",
        "teksti" : "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)