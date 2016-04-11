from scripts.vocabular import matches

with open('header.xml', 'r') as header:
    with open('../output-test.txt', 'r') as finn:
        with open('../decompress-test.txt', 'w') as fout:

            line = finn.readline()
            header = header.readlines()
            header = "".join(header)
            fout.write(header)
            while line != "":

                for key, value in matches.items():
                    if value == "+v" and "+v" in line:
                        print(value, "VALUE")
                        print(key)
                        print(line)
                    line = line.replace("<" + value + ">", "<" + key + ">").strip() + "\n"
                    line = line.replace("<" + value + "K", "<" + key + "/>").strip() + "\n"
                    line = line.replace("<" + value + " ", "<" + key + " ").strip() + "\n"
                    line = line.replace("!" + value, "</" + key).strip() + "\n"
                    line = line.replace("<" + value +'\n', "<" + key + ">\n").strip() + "\n"

                line = line.replace("!", "</" ).strip() + "\n"
                line = line.replace("K", "/>" ).strip() + "\n"

                if len(line)>2 and line[-2] != ">":
                    line = line[0:-1] + ">\n"
                fout.write(line)
                line = finn.readline()
            fout.write('</score-partwise>')


