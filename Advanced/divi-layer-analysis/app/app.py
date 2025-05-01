from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    return """
        <form action="/favorite" method="post">
            Your favorite number: <input name="number">
            <input type="submit">
        </form>
    """


@app.route("/favorite", methods=["POST"])
def favorite():
    number = request.form.get("number", "unknown")
    return f"<h2>Your favorite number is {number}!</h2>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
