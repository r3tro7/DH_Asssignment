import csv
from datetime import datetime

def main():
    infile = "sample_data.csv"
    outfile = "output.csv"
    format = '%m/%d/%Y %H:%M'

    with open(infile, "r") as csvfile:
        with open(outfile, "w", newline='') as outcsv:
            reader = csv.DictReader(csvfile)
            fieldnames = reader.fieldnames + ["elapsed_time", "business_logic"]
            writer = csv.DictWriter(outcsv, fieldnames=fieldnames)

            writer.writeheader()

            for row in reader:
                try:
                    # Generate Field indicating time elapsed in minutes
                    start = datetime.strptime(row["starting_timestamp"], format)
                    end = datetime.strptime(row["ending_timestamp"], format)
                    row["elapsed_time"] = int((end - start).total_seconds() / 60)

                    # Condition to satisfy the business rule
                    row['business_logic'] = row['elapsed_time'] > 90 and row['result'] == 'Fail'
                    writer.writerow(row)

                # Skipping the rows containing incorrect Date formats or empty cells
                except ValueError:
                    pass

if __name__ == "__main__":
    main()