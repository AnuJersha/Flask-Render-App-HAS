from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Render PaaS From Government Polytechnic College Nagercoil.Computer Science Engineering.By,
Jenifa J Hannah Gems
Anu Jersha J
Sivaranjani M
Sharuhashini RS
Akshaya LS"

@app.route("/about")
def about():
    return "This is About Page"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
