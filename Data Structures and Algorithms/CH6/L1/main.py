def count_marketers(job_titles):
    count = 0
    job = "marketer"
    for each in job_titles:
        if each.lower() == job:
            count += 1
    return count
