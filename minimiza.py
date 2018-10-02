import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="Nombre del archivo a minimizar")
args = parser.parse_args()

if args.file:
    with open(args.file, 'r') as reader:
        with open('salida_' + args.file, 'w') as file_wroten:
            for line in reader:
                if '//' not in line:
                    new_line = line.replace("\n", " ")
                    new_line = new_line.replace("\t", " ")

                    for _ in range(30):
                        new_line = new_line.replace("  ", " ")

                    file_wroten.write(new_line)

else:
    print("Falta el nombre del archivo!!")
    print("Ejemplo de uso: ")
    print("python minimiza.py -f nombre_del_archivo")