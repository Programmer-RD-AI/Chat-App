from server import *


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/Sign/Up", methods=["POST", "GET"])
@app.route("/Sign/Up/", methods=["POST", "GET"])
def signup():
    db = cluster["Auth"]
    collection = db["Auth"]
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        similar = collection.find_all({"Email": email, "Password": password})
        if similar is None or similar == []:
            collection.insert_one({"Email": email, "Password": password})
        session["Login"] = True
        session["Password"] = password
        session["Email"] = email
        flash("Successfully signed up", "success")
        return redirect("/Sign/In")
    return render_template("sign_up.html")


@app.route("/Sign/In")
@app.route("/Sign/In/")
def signin():
    db = cluster["Auth"]
    collection = db["Auth"]
    if "Login" in session:
        session.pop("Login")
        session["Auth"] = True
        flash("Login successful", "success")
        return redirect("/Chat")
    if request.method == "POST":
        email = request.form("email")
        password = request.form("password")
        similar = collection.find_all({"Email": email, "Password": password})
        if similar is not None or similar != []:
            session["Auth"] = True
            session[""]
            flash("Login successful", "success")
            return redirect("/Chat")
        flash("Login Failed", "danger")
        return redirect("/Sign/In")
    return render_template("sign_in.html")


@app.route("/Chat", methods=["POST", "GET"])
@app.route("/Chat/", methods=["POST", "GET"])
def chat():
    if "Auth" in session:
        db = cluster["Chat"]
        collection = db["Chat"]
        chats = collection.find_all()
        if request.method == "POST":
            chat = request.POST.get("chat")
            collection.insert_one({'Message':chat,'Email':session.get('Email')})
        return render_template("chat.html", chats=chats)
    return redirect("/")


@app.route(
    "/LogOut",
)
@app.route(
    "/LogOut/",
)
def logout():
    if "Auth" in session:
        session.pop("Auth", None)
        session.pop("Email", None)
        session.pop("Password", None)
        flash("Loged Out", "success")
        return redirect("/")
    return redirect("/")
