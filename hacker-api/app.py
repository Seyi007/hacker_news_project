import os 
import psycopg2
from dotenv import load_dotenv
from flask import Flask, request, jsonify

load_dotenv()

app = Flask(__name__)
url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)



INSERT_story_RETURN_ID = "INSERT INTO newsroom_story(story_type, by, kids, time, url, score, title, descendant) VALUES (%s, %s, %i, current_timestamp, %s, %i, %s, %i) RETURNING id;"
@app.route("/api/story", methods=["POST"])
def create_story():
    data = request.get_json()
    title = data["title"]
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_story_RETURN_ID, (title,))
            story_id = cursor.fetchone()[0]
    return {"id": story_id, "title": title, "message": f"story {title} created."}, 201

SELECT_ALL_STORY = "SELECT * FROM newsroom_story"
@app.route("/api/stories", methods=["GET"])
def get_all_stories():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_ALL_STORY)
            story = cursor.fetchall()
            if story:
                result = []
                for item in story:
                    result.append({"id": item[0], "type": item[1], "by": item[2], "kids": item[3], "time": item[4], "url": item[5], "score": item[6], "title": item[7], "descendant": item[8]})
                return jsonify(result)
            else:
                return jsonify({"error": f"STORY not found."}), 404

@app.route("/api/story/<int:story_id>", methods=["GET"])
def get_story(story_id):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM newsroom_story WHERE id = %s", (story_id,)) 
            story = cursor.fetchone()
            if story:
                return jsonify({"id": story[0], "type": story[1], "by": story[2], "kids": story[3], "time": story[4], "url": story[5], "score": story[6], "title": story[7], "descendant": story[8]})
            else:
                return jsonify({"error": f"story with ID {story_id} not found."}), 404

INSERT_Job_RETURN_ID = "INSERT INTO newsroom_job(by, text, time, score, item_type, title, url) VALUES (%s, %s, current_timestamp, %i, %s, %s, %s) RETURNING id;"
@app.route("/api/job", methods=["POST"])
def create_job():
    data = request.get_json()
    title = data["title"]
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_Job_RETURN_ID, (title,))
            job_id = cursor.fetchone()[0]
    return {"id": job_id, "title": title, "message": f"job {title} created."}, 201

SELECT_ALL_Job = "SELECT * FROM newsroom_job"
@app.route("/api/jobs", methods=["GET"])
def get_all_stories():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_ALL_Job)
            job = cursor.fetchall()
            if job:
                result = []
                for item in job:
                    result.append({"by": item[0], "job_id": item[1], "text": item[2], "time": item[3], "item_type": item[4], "score": item[5], "title": item[6], "url": item[7]})
                return jsonify(result)
            else:
                return jsonify({"error": f"job not found."}), 404

@app.route("/api/job/<int:job_id>", methods=["GET"])
def get_job(job_id):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM newsroom_job WHERE id = %s", (job_id,)) 
            job = cursor.fetchone()
            if job:
                return jsonify({"by": job[0], "id": job[1], "type": job[2], "text": job[3], "time": job[4], "item_type": job[5], "score": job[6], "title": job[7], "url": job[8]})
            else:
                return jsonify({"error": f"job with ID {job_id} not found."}), 404



INSERT_ASK_RETURN_ID = "INSERT INTO newsroom_ask(by, text, time, item_type, score, descendant, title) VALUES (%s, %s, current_timestamp, %i, %i, %s) RETURNING id;"
@app.route("/api/ask", methods=["POST"])
def create_ask():
    data = request.get_json()
    title = data["title"]
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_ASK_RETURN_ID, (title,))
            ask_id = cursor.fetchone()[0]
    return {"id": ask_id, "title": title, "message": f"ASK {title} created."}, 201

SELECT_ALL_ASK = "SELECT * FROM newsroom_ask"
@app.route("/api/asks", methods=["GET"])
def get_all_stories():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_ALL_ASK)
            asks = cursor.fetchall()
            if asks:
                result = []
                for item in asks:
                    result.append({"by": item[0], "ask_id": item[1], "text": item[2], "time": item[3], "item_type": item[4], "score": item[5], "descendant": item[6], "title": item[7]})
                return jsonify(result)
            else:
                return jsonify({"error": f"ASK not found."}), 404

@app.route("/api/ask/<int:ASK_id>", methods=["GET"])
def get_ask(ask_id):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM newsroom_ASK WHERE id = %s", (ask_id,)) 
            ask = cursor.fetchone()
            if ask:
                return jsonify({"by": ask[0], "id": ask[1], "text": ask[2], "time": ask[3], "item_type": ask[4], "score": ask[5], "descendant": ask[6], "title": ask[7]})
            else:
                return jsonify({"error": f"ASK with ID {ASK_id} not found."}), 404
