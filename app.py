from flask import Flask, jsonify, request, Response
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import RomanModel
from sqlalchemy.sql.expression import func
import json

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


def get_session():

    engine = create_engine('sqlite:///database/roman_demo.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

@app.route("/")
def home():
    return jsonify({"Hello": "Welcome to Roman API"}), 200

@app.route("/api/random_data", methods=['GET'])
def random_data():
    session = get_session()
    data = session.query(RomanModel).order_by(func.random()).first()
    try:
        session.close()
        data = {
                "name": data.name,
                "birth_year": data.year_birth,
                "death_year": data.year_dead,
                "role": data.role,
                "facts/curiosities": data.curiosities

            }

        response = Response(
            json.dumps(data, ensure_ascii=False, indent=4),
            content_type="application/json; charset=utf-8"
        )

        return response

    except:
        session.close()
        return jsonify({"error_msg":"Invalid request"})

@app.route("/api/emperor", methods=['GET'])
def random_emperor():
    session = get_session()
    data = session.query(RomanModel).filter_by(role="Emperor").order_by(func.random()).first()
    try:
        session.close()
        data = {
                    "name": data.name,
                    "birth_year": data.year_birth,
                    "death_year": data.year_dead,
                    "role": data.role,
                    "facts/curiosities": data.curiosities

                }

        response = Response(
                json.dumps(data, ensure_ascii=False, indent=4),
                content_type="application/json; charset=utf-8"
            )

        return response

    except:
        session.close()
        return jsonify({"error_msg":"Invalid request"})


@app.route("/api/myth", methods=['GET'])
def random_myth():
    session = get_session()
    data = session.query(RomanModel).filter_by(role="Myth").order_by(func.random()).first()
    try:
        session.close()
        data = {
                    "name": data.name,
                    "role": data.role,
                    "description": data.curiosities

                }

        response = Response(
                json.dumps(data, ensure_ascii=False, indent=4),
                content_type="application/json; charset=utf-8"
            )

        return response

    except:
        session.close()
        return jsonify({"error_msg":"Invalid request"})

@app.route("/api/senator", methods=['GET'])
def random_senator():
    session = get_session()
    data = session.query(RomanModel).filter_by(role="Senator").order_by(func.random()).first()
    try:
        session.close()
        data = {
                    "name": data.name,
                    "birth_year": data.year_birth,
                    "death_year": data.year_dead,
                    "role": data.role,
                    "facts/curiosities": data.curiosities
                }

        response = Response(
                json.dumps(data, ensure_ascii=False, indent=4),
                content_type="application/json; charset=utf-8"
            )

        return response

    except:
        session.close()
        return jsonify({"error_msg":"Invalid request"})

@app.route("/api/consul", methods=['GET'])
def random_consul():
    session = get_session()
    data = session.query(RomanModel).filter_by(role="Consul").order_by(func.random()).first()
    try:
        session.close()
        data = {
                    "name": data.name,
                    "birth_year": data.year_birth,
                    "death_year": data.year_dead,
                    "role": data.role,
                    "facts/curiosities": data.curiosities
                }

        response = Response(
                json.dumps(data, ensure_ascii=False, indent=4),
                content_type="application/json; charset=utf-8"
            )

        return response

    except:
        session.close()
        return jsonify({"error_msg":"Invalid request"})

@app.route("/api/military", methods=['GET'])
def random_military():
    session = get_session()
    data = session.query(RomanModel).filter_by(role="Military").order_by(func.random()).first()
    try:
        session.close()
        data = {
                    "name": data.name,
                    "birth_year": data.year_birth,
                    "death_year": data.year_dead,
                    "role": data.role,
                    "facts/curiosities": data.curiosities
                }

        response = Response(
                json.dumps(data, ensure_ascii=False, indent=4),
                content_type="application/json; charset=utf-8"
            )

        return response

    except:
        session.close()
        return jsonify({"error_msg":"Invalid request"})

@app.route("/api/historian", methods=['GET'])
def random_historian():
    session = get_session()
    data = session.query(RomanModel).filter_by(role="Historian").order_by(func.random()).first()
    try:
        session.close()
        data = {
                    "name": data.name,
                    "birth_year": data.year_birth,
                    "death_year": data.year_dead,
                    "role": data.role,
                    "facts/curiosities": data.curiosities
                }

        response = Response(
                json.dumps(data, ensure_ascii=False, indent=4),
                content_type="application/json; charset=utf-8"
            )

        return response

    except:
        session.close()
        return jsonify({"error_msg":"Invalid request"})

@app.route("/api/philosopher", methods=['GET'])
def random_philosopher():
    session = get_session()
    data = session.query(RomanModel).filter_by(role="Philosopher").order_by(func.random()).first()
    try:
        session.close()
        data = {
                    "name": data.name,
                    "birth_year": data.year_birth,
                    "death_year": data.year_dead,
                    "role": data.role,
                    "facts/curiosities": data.curiosities
                }

        response = Response(
                json.dumps(data, ensure_ascii=False, indent=4),
                content_type="application/json; charset=utf-8"
            )

        return response

    except:
        session.close()
        return jsonify({"error_msg":"Invalid request"})

@app.route("/api/artist", methods=['GET'])
def random_artist():
    session = get_session()
    data = session.query(RomanModel).filter_by(role="Artist").order_by(func.random()).first()
    try:
        session.close()
        data = {
                    "name": data.name,
                    "birth_year": data.year_birth,
                    "death_year": data.year_dead,
                    "role": data.role,
                    "facts/curiosities": data.curiosities
                }

        response = Response(
                json.dumps(data, ensure_ascii=False, indent=4),
                content_type="application/json; charset=utf-8"
            )

        return response

    except:
        session.close()
        return jsonify({"error_msg":"Invalid request"})

@app.route("/api/woman", methods=['GET'])
def random_woman():
    session = get_session()
    data = session.query(RomanModel).filter_by(role="Woman").order_by(func.random()).first()
    try:
        session.close()
        data = {
                    "name": data.name,
                    "birth_year": data.year_birth,
                    "death_year": data.year_dead,
                    "role": data.role,
                    "facts/curiosities": data.curiosities
                }

        response = Response(
                json.dumps(data, ensure_ascii=False, indent=4),
                content_type="application/json; charset=utf-8"
            )

        return response

    except:
        session.close()
        return jsonify({"error_msg":"Invalid request"})

@app.route("/api/lawyer", methods=['GET'])
def random_lawyer():
    session = get_session()
    data = session.query(RomanModel).filter_by(role="Lawyer").order_by(func.random()).first()
    try:
        session.close()
        data = {
                    "name": data.name,
                    "birth_year": data.year_birth,
                    "death_year": data.year_dead,
                    "role": data.role,
                    "facts/curiosities": data.curiosities
                }

        response = Response(
                json.dumps(data, ensure_ascii=False, indent=4),
                content_type="application/json; charset=utf-8"
            )

        return response

    except:
        session.close()
        return jsonify({"error_msg":"Invalid request"})

@app.route("/api/king", methods=['GET'])
def random_king():
    session = get_session()
    data = session.query(RomanModel).filter_by(role="King").order_by(func.random()).first()
    try:
        session.close()
        data = {
                    "name": data.name,
                    "birth_year": data.year_birth,
                    "death_year": data.year_dead,
                    "role": data.role,
                    "facts/curiosities": data.curiosities
                }

        response = Response(
                json.dumps(data, ensure_ascii=False, indent=4),
                content_type="application/json; charset=utf-8"
            )

        return response

    except:
        session.close()
        return jsonify({"error_msg":"Invalid request"})

@app.route("/api/diplomat", methods=['GET'])
def random_diplomat():
    session = get_session()
    data = session.query(RomanModel).filter_by(role="Diplomat").order_by(func.random()).first()
    try:
        session.close()
        data = {
                    "name": data.name,
                    "birth_year": data.year_birth,
                    "death_year": data.year_dead,
                    "role": data.role,
                    "facts/curiosities": data.curiosities
                }

        response = Response(
                json.dumps(data, ensure_ascii=False, indent=4),
                content_type="application/json; charset=utf-8"
            )

        return response

    except:
        session.close()
        return jsonify({"error_msg":"Invalid request"})

@app.route("/api/enemy", methods=['GET'])
def random_enemy():
    session = get_session()
    data = session.query(RomanModel).filter_by(role="Enemy").order_by(func.random()).first()
    try:
        session.close()
        data = {
                    "name": data.name,
                    "birth_year": data.year_birth,
                    "death_year": data.year_dead,
                    "role": data.role,
                    "facts/curiosities": data.curiosities
                }

        response = Response(
                json.dumps(data, ensure_ascii=False, indent=4),
                content_type="application/json; charset=utf-8"
            )

        return response

    except:
        session.close()
        return jsonify({"error_msg":"Invalid request"})

@app.route("/api/praetorian", methods=['GET'])
def random_praetorian():
    session = get_session()
    data = session.query(RomanModel).filter_by(role="Praetorian").order_by(func.random()).first()
    try:
        session.close()
        data = {
                    "name": data.name,
                    "birth_year": data.year_birth,
                    "death_year": data.year_dead,
                    "role": data.role,
                    "facts/curiosities": data.curiosities
                }

        response = Response(
                json.dumps(data, ensure_ascii=False, indent=4),
                content_type="application/json; charset=utf-8"
            )

        return response

    except:
        session.close()
        return jsonify({"error_msg":"Invalid request"})

@app.route("/api/gladiator", methods=['GET'])
def random_gladiator():
    session = get_session()
    data = session.query(RomanModel).filter_by(role="Gladiator").order_by(func.random()).first()
    try:
        session.close()
        data = {
                    "name": data.name,
                    "birth_year": data.year_birth,
                    "death_year": data.year_dead,
                    "role": data.role,
                    "facts/curiosities": data.curiosities
                }

        response = Response(
                json.dumps(data, ensure_ascii=False, indent=4),
                content_type="application/json; charset=utf-8"
            )

        return response

    except:
        session.close()
        return jsonify({"error_msg":"Invalid request"})

@app.route("/api/scientist", methods=['GET'])
def random_scientist():
    session = get_session()
    data = session.query(RomanModel).filter_by(role="Scientist").order_by(func.random()).first()
    try:
        session.close()
        data = {
                    "name": data.name,
                    "birth_year": data.year_birth,
                    "death_year": data.year_dead,
                    "role": data.role,
                    "facts/curiosities": data.curiosities
                }

        response = Response(
                json.dumps(data, ensure_ascii=False, indent=4),
                content_type="application/json; charset=utf-8"
            )

        return response

    except:
        session.close()
        return jsonify({"error_msg":"Invalid request"})

@app.route("/api/search_character", methods=['GET'])
def search_character():
    session = get_session()
    try:
        # Gets parameter from request body
        search_term = request.args["name"]

        if not search_term:
            return jsonify({"error_msg": "You must fill name field."}), 400

        results = session.query(RomanModel).filter(RomanModel.name.like(f'%{search_term}%')).all()

        if results:

            data = [
                {
                    "name": character.name,
                    "birth_year": character.year_birth,
                    "death_year": character.year_dead,
                    "role": character.role,
                    "facts/curiosities": character.curiosities
                }
                for character in results
            ]

            response = Response(
                json.dumps(data, ensure_ascii=False, indent=4),
                content_type="application/json; charset=utf-8"
            )
            return response
        else:
            return jsonify({"error_msg": "No characters found with this name."})

    except Exception as e:
        return jsonify({"error_msg": f"Error en la solicitud: {str(e)}"}), 500

    finally:
        session.close()

if __name__ == '__main__':
    app.run()
