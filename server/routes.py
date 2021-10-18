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
        email = request.form["E"]
        password = request.form["P"]
        similar = []
        similar_iter = collection.find({"Email": email, "Password": password})
        for s in similar_iter:
            similar.append(s)
        print(similar)
        if similar is None or similar == []:
            collection.insert_one({"Email": email, "Password": password})
            session["Login"] = True
            session["Password"] = password
            session["Email"] = email
            flash("Successfully signed up", "success")
            return redirect("/Sign/In")
        flash("There is another user with that info", "danger")
        return redirect("/")
    return render_template("sign_up.html")


@app.route("/Sign/In", methods=["POST", "GET"])
@app.route("/Sign/In/", methods=["POST", "GET"])
def signin():
    db = cluster["Auth"]
    collection = db["Auth"]
    if "Login" in session:
        session.pop("Login")
        session["Auth"] = True
        flash("Login successful", "success")
        return redirect("/Chat")
    if request.method == "POST":
        email = request.form["E"]
        password = request.form["P"]
        similar = []
        similar_iter = collection.find({"Email": email, "Password": password})
        for s in similar_iter:
            similar.append(s)
        if similar is not None or similar != []:
            session["Auth"] = True
            session["Email"] = email
            session["Password"] = password
            flash("Login successful", "success")
            return redirect("/Chat")
        flash("Login Failed", "danger")
        return redirect("/Sign/In")
    return render_template("sign_in.html")


@app.route("/Chat", methods=["GET", "POST"])
@app.route("/Chat/", methods=["GET", "POST"])
def chat():
    db = cluster["Chat"]
    collection = db["Chat"]
    if "Auth" in session:
        if request.method == "POST":
            chat = request.form["C"]
            print(chat)
            collection.insert_one({"Message": chat, "Email": session.get("Email"),'Time':str(datetime.datetime.now())})
            flash("Message Send", "success")
            return redirect("/Chat")
        chats = []
        chats_iter = collection.find()
        for c in chats_iter:
            chats.append(c)

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
