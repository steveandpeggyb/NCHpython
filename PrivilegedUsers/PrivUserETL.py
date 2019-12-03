def UserData():
    import csv

    with open ("R:/RESBCR/FISMA/PrivilegedUserAudits/PrivilegedUserAudit.csv") as f:
        reader = csv.reader(f)
        next(reader) # skip header
        data = []
        for row in reader:
            if len(row)>0:
                # data.append(row)
                sandbox = row[0]
                sandbox = sandbox.lower()
                sandbox = sandbox.replace("research\\","")
                sandbox = sandbox.strip()
                data.append(sandbox)
        return data

for row in UserData():
    print(row)
