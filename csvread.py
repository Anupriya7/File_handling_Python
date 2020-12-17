import csv

with open('sample.csv','r') as f:
    csv_reader=csv.DictReader(f)

    with open('new.csv','w') as write_new:
        field_names=['first-name','last-name']
        csv_writer=csv.DictWriter(write_new,fieldnames=field_names)

        #csv_writer.writeheader()

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)