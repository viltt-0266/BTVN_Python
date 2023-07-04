def process_name(name):
    name = name.strip().lower().replace(" ", "")
    return name.capitalize()

def process(full_name):
    name_parts = full_name.strip()
    full_name = name_parts.split()
    Result = process_name(full_name[-1])
    Result += ''.join(process_name(word)[0] for word in full_name[:-1])
    return Result

def main():
    fulll_name = input("Nhập họ và tên: ")
    print(process(fulll_name))

main()
