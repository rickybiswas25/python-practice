import os


class ReadWriteFile:

    def write(self):
        f = open("data.txt", "w+")
        for i in range(0, 10):
            f.write(str(i) + "\n")

        print("Writing complete. Closing the file")
        f.close()

    def read(self):
        f = open("data.txt", "r")
        contents = f.read()
        print(contents)
        f.close()

    def delete(self):
        os.remove("data.txt")


ReadWriteFile().write()
ReadWriteFile().read()
ReadWriteFile().delete()
