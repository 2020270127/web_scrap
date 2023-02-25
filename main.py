from remoteok import extract_jobs
from file import save_to_file

keyword = input("What do you want to search for?")

remoteok = extract_jobs(keyword)
jobs = remoteok

save_to_file(keyword,jobs)