#importar paquetes y modulos
import string
import inflect 
import nltk
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer
#from sklearn.feature_extraction.text import TfidfVectorizer

#abrir el archivo
with open ('Corpus-Med500.txt', 'r') as archivo:
    texto = archivo.read()

#Tokenizacion: convertir oraciones en palabras
words = nltk.word_tokenize(texto)
#print(words)

#Normalizacion

#Convertir de mayusculas a minusculas
def minusculas(words):
    new_words = []
    for word in words:
        new_word = word.lower()
        new_words.append(new_word)
    return new_words

#Remover signos de puntuacion
def removerSignosPuntuacion(words):
    new_words = []
    for word in words:
        signos=set(string.punctuation)
        if word not in signos :
            new_words.append(word)
        #new_word = re.sub(r'[^\w\s]', '', word)
        #if new_word != '':
        #    new_words.append(new_word)     
    return new_words

#Numeros a texto
def remplazarNumeros(words):
    p = inflect.engine()
    new_words = []
    for word in words:
        if word.isdigit():
            new_word = p.number_to_words(word)
            new_words.append(new_word)
        else:
            new_words.append(word)
    return new_words

#Eliminar StopWords
def EliminarStopWords(words):
    new_words = []
    for word in words:
        if word not in stopwords.words('english'):
            new_words.append(word)
    return new_words

def stemWords(words):
    stemmer = LancasterStemmer()
    stems = []
    for word in words:
        stem = stemmer.stem(word)
        stems.append(stem)
    return stems

def lematizacion(words):
    lematizacion = WordNetLemmatizer()
    lemmas = []
    for word in words:
        lemma = lematizacion.lemmatize(word, pos='v')
        lemmas.append(lemma)
    return lemmas

def normalizar(words):
    words = minusculas(words)
    words = removerSignosPuntuacion(words)
    words = remplazarNumeros(words)
    words = EliminarStopWords(words)
    words = lematizacion(words)
    return words

words = normalizar(words)
#print(words, "TEXTO NORMALIZADO\n ")

def stem_and_lematizacion(words):
    stems = stemWords(words)
    lemmas = lematizacion(words)
    return stems, lemmas

stems, lemmas = stem_and_lematizacion(words)
#print('STEMMED:\n', stems)
#print('\nLEMATIZACION:\n', lemmas)

words.append(".i")

#Separar el corpus en bolsistas de palabras
def BolsitasPalabras(words):
    MegaBagOfWords = []
    BagOfWordsAux = []
    ID= 400
    for word in range(len(words)):
        if words[word] != '.i':
            BagOfWordsAux.append(words[word])
            if words[word+1] == '.i':
                #MegaBagOfWords.append(ID)
                MegaBagOfWords.append(BagOfWordsAux)
                #ID +=1
                BagOfWordsAux = []
    return MegaBagOfWords

words = BolsitasPalabras(words)  

def convertir(listas):
    nuevaListas = []

    for lista in listas:
        aux = ' '.join(lista)
        nuevaListas.append(aux)
        aux = []

    return nuevaListas


words = convertir(words)
#print(words)

def CalcularTFIDF(words, consulta):
    from sklearn import feature_extraction
    from sklearn.feature_extraction.text import TfidfTransformer
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    vectorizer = CountVectorizer()   
    transformer = TfidfTransformer()     
    tfidf = transformer.fit_transform(vectorizer.fit_transform(words))  
    consulta_tfidf = transformer.transform(vectorizer.transform
    ([consulta]))
    word = vectorizer.get_feature_names()   
    weight = tfidf.toarray()    
    cosineSimilitaries = cosine_similarity(tfidf, consulta_tfidf)
    return cosineSimilitaries

def Ranker (cosineSimList):
    rank = []
    for i in range (len(cosineSimList)):
        if cosineSimList[i] != 0.0 :
            aux = float (cosineSimList[i])
            rank.append((i+ 400, aux))
            #print(".I",i+ 400 , cosineSimList[i])
    rank.sort(key = lambda x: x[1], reverse=True)
    print("Total de ", len(rank), "coincidencias") 
    print('\n'.join(map(str, rank)))

res = 1
while res == 1 :
    consulta = []
    #Consula
    consulta = input("Introduce tu consulta : ")
    busqueda = nltk.word_tokenize(consulta)
    busqueda = normalizar(busqueda)
    busqueda = ' '.join(busqueda)
    resultadoConsulta = CalcularTFIDF(words, consulta)
    Ranker(resultadoConsulta)
    res = int (input("¿Desea hacer otra consulta? 0/ 1: "))

#print("BUSQUEDA NORMALIZADO\n ", busqueda)










    
