def save_to_file(file_name,jobs):
    file = open(f"{file_name}.csv","w")
    file.write("Company, Location, Position, Link\n")

    for job in jobs:
        file.write(
            f"{job['company']},{job['location']},{job['position']}, {job['link']}\n"
        ) 

    file.close()