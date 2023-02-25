from extractors.remoteok import extract_remoteok_jobs
from extractors.wwr import extract_wwr_jobs
from extractors.file import save_to_file
from flask import Flask, render_template, request, redirect, send_file

app = Flask("JobScrapper")

db = {}

@app.route("/")
def home():
    return render_template("home.html",name="nico")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword in db:
        jobs = db[keyword]
    else:
        wwr = extract_wwr_jobs(keyword)
        remoteok = extract_remoteok_jobs(keyword)
        jobs = wwr + remoteok
        db[keyword] = jobs
    return render_template("search.html",keyword=keyword,jobs=jobs)


@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword not in db:
        return redirect("/search?keyword={keyword}")
    save_to_file(keyword,db[keyword])
    return send_file(f"{keyword}.csv",as_attachment=True)
    




app.run("0.0.0.0")

# keyword = input("What do you want to search for?")

# remoteok = extract_jobs(keyword)
# weworkremotely = extract_jobs(keyword)
# jobs = remoteok + weworkremotely

# save_to_file(keyword,jobs)