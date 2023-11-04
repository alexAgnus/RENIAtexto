from pprint import pprint

import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import seaborn as sns
import psycopg2
#import psycopg2.extras
from conexion import conn, cur,record

module_url = "https://tfhub.dev/google/universal-sentence-encoder/4" #@param ["https://tfhub.dev/google/universal-sentence-encoder/4", "https://tfhub.dev/google/universal-sentence-encoder-large/5"]
model = hub.load(module_url)
print ("module %s loaded" % module_url)
def embed(input):
  return model(input)

def plot_similarity(labels, features, rotation):
  corr = np.inner(features, features)
  sns.set(font_scale=1.2)
  g = sns.heatmap(
      corr,
      xticklabels=labels,
      yticklabels=labels,
      vmin=0,
      vmax=1,
      cmap="YlOrRd")
  g.set_xticklabels(labels, rotation=rotation)
  g.set_title("Semantic Textual Similarity")
  print(corr)
#messages = [messages]
def run_and_plot(messages_):
  message_embeddings_ = embed(messages_)
  plot_similarity(messages_, message_embeddings_, 90)

messages = input("Ingrese los datos: ")
messages = [messages]

cantidad =99
#c = cur
#cur = conn.cursor()
messages2=[]

cur.execute('SELECT senasParticulares FROM Persona')
for record in cur.fetchall():
    messages2.append(record[0])


#messages2 = [

    # Smartphones
    #"Buen dia como te va",
    #"Hola como estas",
    #"Hola buenas noches",
    #"Que tal, bien dias como has estado",
    #"Ahi hay un perro",
  #]
  # run_and_plot(messages)


from tensorflow.python.framework.ops import numpy_text
import math

def run_sts_benchmark():

  scores = []
  sts_encode1 = tf.nn.l2_normalize(embed(messages), axis=1)
  sts_encode2 = tf.nn.l2_normalize(embed(messages2), axis=1)
  cosine_similarities = tf.reduce_sum(tf.multiply(sts_encode1, sts_encode2), axis=1)
  clip_cosine_similarities = tf.clip_by_value(cosine_similarities, -1.0, 1.0)
  scores = 1.0 - tf.acos(clip_cosine_similarities) / math.pi
  """Returns the similarity scores"""

  return scores

scores = []
scores.extend(run_sts_benchmark())

print(scores)

lista = []
cantidad = 1
mayor = 0
menor = 0
cont = 1
i = 0

while (cantidad < 99):
  #numero = (scores[i], (cont + (i)))
  numero = (scores[i],messages2[i], (cont + (i)))
  lista.append(numero)
  i = i + 1
  cantidad = cantidad + 1

mayor = max(lista)
menor = min(lista)
lista.append(mayor)
top = lista.remove(mayor)
lista.sort(reverse=True)

#can=1
#a=0
#while (can <  2):
 #   print("Descripcion: ",messages2[a],(a))
print("Menor ", menor)
print("Mayor ", mayor)
print("Top 5: ")
NList = sorted(lista, reverse=True)
while len(NList) > 5:
    NList.pop()
pprint(NList)

    #can =can+1
conn.commit()
conn.close()



