from extractors.remoteok import extract_remoteok_jobs
from extractors.wwr import extract_wwr_jobs
# from extractors.file import save_to_file
from flask import Flask, render_template, request

app = Flask("JobScrapper")

@app.route("/")
def home():
    return render_template("home.html",name="nico")

@app.route("/search")
def hello():
    keyword = request.args.get("keyword")
    wwr = extract_wwr_jobs(keyword)
    remoteok = extract_remoteok_jobs(keyword)
    jobs = wwr + remoteok
    return render_template("search.html",keyword=keyword,jobs = jobs)

app.run("0.0.0.0")

# keyword = input("What do you want to search for?")

# remoteok = extract_jobs(keyword)
# weworkremotely = extract_jobs(keyword)
# jobs = remoteok + weworkremotely

# save_to_file(keyword,jobs)