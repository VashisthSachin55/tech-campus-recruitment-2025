import sys
import os

def extract_logs(log_file, date):
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True) 
    output_file = os.path.join(output_dir, f"output_{date}.txt")

    found = False

    try:
        with open(log_file, 'r', encoding='utf-8', errors='ignore') as f, open(output_file, 'w', encoding='utf-8') as out:
            for line in f:
                if line.startswith(date):
                    out.write(line)
                    found = True

        if not found:
            print(f"No logs found for {date}. Check if the date format matches your log file.")
        else:
            print(f"Logs for {date} saved in {output_file}")

    except FileNotFoundError:
        print(f"Error: Log file '{log_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":  
    if len(sys.argv) != 3:
        print("Usage: python extract_logs.py <log_file_path> YYYY-MM-DD")
        sys.exit(1)

    log_file_path = sys.argv[1]  
    date_to_search = sys.argv[2]  

    extract_logs(log_file_path, date_to_search)
