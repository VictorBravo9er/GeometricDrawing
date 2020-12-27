import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer
import re

text = "A line AB is drawn using two points A(2,3) and B(4,4). \
        Draw a perpendicular_bisector CD to the line AB. \
        Given two points E(1,2) and F(8,6), draw a line."


def parseNaturalInput(text:str=..., debug:bool=False):

    objects = ['point', 'line', 'curve', 'plane', 'chord', 'triangle', 'quadrilateral', 'parallelogram', 'square', 'rectangle'\
                'rhombus', 'kite', 'trapezium', 'diagonal', 'circle', 'sphere']

    props = ['length', 'perimeter', 'area', 'volume', 'parallel', 'perpendicular_bisector', 'perpendicular', 'angle', 'bisector', \
            'center', 'radius', 'diameter', 'circumference', 'intersect', 'equilateral', 'isosceles', 'scalene']

    if not isinstance(text, str):
        raise TypeError(
            f"Expected str, received {type(text).__name__}"
        )
    tokenized = sent_tokenize(text)
    stop_words = set(stopwords.words('english'))
    for i in tokenized:
        if debug:
            print("sent: ",i)
        # Using Word tokenizer to find the words and punctuation in a string 
        words_in_sent = nltk.word_tokenize(i)
    
        # removing stop words from wordList 
        wordsList = [w for w in words_in_sent if not w in stop_words]
        if debug:
            print("Wordlist: ",wordsList)
        
        # stemming using Porter Stemmer
        ps = PorterStemmer()
        stemList = [ps.stem(w) for w in wordsList]
        if debug:
            print('Stemlist: ',stemList)
        
        # Classifying stems to objects and props
        objList = [stem for stem in stemList if stem in objects]
        propList = [stem for stem in stemList if stem in props]
        if debug:
            print("List of objects present: ",objList)
            print("List of properties present: ",propList)
        
        # extracting point coordinates in 2D (if any)
        point_coordinates = re.findall('(\d+),(\d+)', i) # handles only integer coordinates
        #point_coordinates = re.findall('(\d+\.\d+),(\d+\.\d+)', i) # handles only float coordinates
        if debug:
            print("Coordinates of points (if any): ",point_coordinates)
            print('\n')


    def getObjects(id_c, line_ref):    
        objects = []
        count = 0 # gets incremented when an object is handled
        noOfObjects = len(objList)
        ref_list = []

        # Handling point objects
        if 'point' in objList:
            #obj = []
            count += 1
            for j in range(len(point_coordinates)):
                obj = []
                ref_list.append(chr(id_c))
                id_c += 1
                obj.append(ref_list[j])
                obj.append('new')
                obj.append('point')
                x,y = point_coordinates[j]
                obj.append(x)
                obj.append(y)
                objects.append(obj)


        # Handling line objects
        if 'line' in objList:
            obj = []
            
            count += 1
            obj.append(chr(id_c))
            if len(ref_list) > 0:
                obj.append('new')
                obj.append('line')
                line_ref.append(chr(id_c))
            else:
                if len(line_ref) > 0:
                    obj.append(line_ref[-1])
            id_c += 1
            for r in ref_list:
                obj.append(r)
            for p in propList:
                obj.append(p)
        objects.append(obj)

        assert count == noOfObjects, "All objects in objList not handled"
        return objects, id_c, line_ref


    # Text Preprocessing
    tokenized = sent_tokenize(text) # Extract sentences
    stop_words = set(stopwords.words('english'))  # Get list of stopwords in 'English' language
    all_objects = []
    line_ref = [] # keep refernce of line objects
    id_c = 65 #used for assigning id to objects
    for i in tokenized:
        
        # Using Word tokenizer to find the words and punctuation in a string 
        words_in_sent = nltk.word_tokenize(i)
    
        # removing stop words from wordList 
        wordsList = [w for w in words_in_sent if not w in stop_words]
        
        # stemming using Porter Stemmer
        ps = PorterStemmer()
        stemList = [ps.stem(w) for w in wordsList]
        
        # Classifying stems to objects and props
        objList = [stem for stem in stemList if stem in objects]
        propList = [stem for stem in stemList if stem in props]
        
        # extracting point coordinates in 2D (if any)
        point_coordinates = re.findall('(\d+),(\d+)', i) # handles only integer coordinates
        #point_coordinates = re.findall('(\d+\.\d+),(\d+\.\d+)', i) # handles only float coordinates
        
        currentObjList, id_c, line_ref = getObjects(id_c, line_ref) # Function call to get list of objects in a sentence
        for i in currentObjList:
            all_objects.append(i)
        
    return(all_objects)

if __name__ == "__main__":
    a = parseNaturalInput(text)
    print(a)
