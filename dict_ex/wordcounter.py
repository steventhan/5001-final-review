"""
Implement a program that counts how many unique words in a text file. 
    Write the result to new file.
    re.sub(r"[^\w\s]", "", data) -> remove punctuation
"""
import re

class WordCounter:
    def __init__(self, file_name):
        self.file_name = file_name
        self.counts = self.count()
    
    def read_file(self):
        infile = open(self.file_name, "r")
        data = infile.read()
        infile.close()
        return data

    def get_sanitized_low(self):
        data = self.read_file()
        punc_removed = re.sub(r"[^\w\s]", "", data)
        newline_removed = punc_removed.replace("\n", "")
        lowered = newline_removed.lower()
        list_of_words = lowered.split(" ")
        return list_of_words
        
    def count(self):
        try:
            sanitized_list_of_words = self.get_sanitized_low()
        except OSError:
            print("Can't read file.")

        counts = {}

        for word in sanitized_list_of_words:
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1
        return counts

    def write_to_file(self, file_to_write="report.txt"):
        try:
            outfile = open(file_to_write, "w")
            for word, count in self.counts.items():
                outfile.write("{} {}\n".format(word, count))
            outfile.close()
        except OSError:
            print("Can't write file")

    def get_top_n_words(self, n):
        if not hasattr(self, "sorted_counts"):
            counts_list = list(self.counts.items())
            self.sorted_counts = sorted(counts_list, key=lambda item: item[1], reverse=True)
        return self.sorted_counts[:n]

def main():
    word_counter_instance = WordCounter("words.txt")
    word_counter_instance.write_to_file()
    print(word_counter_instance.get_top_n_words(3))
    print(word_counter_instance.get_top_n_words(100))


if __name__ == "__main__":
    main()