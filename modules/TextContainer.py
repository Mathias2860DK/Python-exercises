import string
class TextContainer():
    """TextContainer description"""

    def __init__(self, my_text):
        """Initialize text container"""
        self.my_text = my_text       
    
    def __repr__(self):
        return 'TextContainer(%r)' % (self.my_text)
    
    def number_of_words(self):
        result = len(self.my_text.split())
        print("There are " + str(result) + " words.")
        
    def number_of_chars(self):
        result = len(self.my_text)
        print("There are " + str(result) + " characters.")
        
    def remove_all_punctuation_characters(self):
        for char in self.my_text:
            if char in string.punctuation:
                self.my_text = self.my_text.replace(char, '')
        
        print("String without punctuation characters" + self.my_text)
        
    def number_of_letters(self):
        result = 0
        for char in self.my_text:
            if char in string.ascii_letters:
                result += 1
        
        print("There are " + str(result) + " letters.")


    
    def __str__(self):
        return ''
    
    

