from collections import defaultdict
string = "Mississippi and Alabama"
def_dict = defaultdict(int)  # Default factory is integer
for key in string:  # For each character in string, increment a counter for that character
    def_dict[key] += 1

if __name__ == "__main__":
    print(sorted(def_dict.items()))
