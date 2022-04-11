import os
def main():
    files = os.listdir('Task3')
    with open('./Task3_copy/Task3.txt') as file:
        for i, line in enumerate(file):
            os.rename("Task3/" + files[i] + ".mp3", line)
if __name__ == "__main__":
    main()