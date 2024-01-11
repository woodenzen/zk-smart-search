import os
import re

def find_matching_files(directory, words, max_distance):
    file_links = []
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as f:
                    content = f.read()
                    sentences = re.split(r"[.!?]", content)
                    
                    for sentence in sentences:
                        sentence_words = sentence.split()
                        matching_words = [word for word in words if word in sentence_words]
                        
                        if len(matching_words) >= 2:
                            distance = min([abs(sentence_words.index(matching_words[i]) - sentence_words.index(matching_words[i+1])) for i in range(len(matching_words)-1)])
                            
                            if distance <= max_distance:
                                file_name = os.path.basename(file_path)
                                file_link = f"[[{file_name[-15:-3]}]]"
                                file_links.append((file_link, file_name[:-16], matching_words, distance))


    #  Sort file_links based on the number of matching words and the distance
    file_links.sort(key=lambda x: (-len(x[2]), x[3]))
    # Format the links after sorting
    file_links = [f"[{file_name} - {distance}](thearchive://match/›{link} {' '.join(words)})" for link, file_name, words, distance in file_links]
    return file_links

if __name__ == "__main__":
    file_links = find_matching_files("/Users/will/Dropbox/zettelkasten", ["sky","tree", "cloud"], 100)
    # Remove duplicates while preserving order
    seen = set()
    file_links = [x for x in file_links if not (x in seen or seen.add(x))]
    for file in file_links:
        print(f'{file}')
        