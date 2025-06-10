import random
import json
import pickle
import numpy as np
import tensorflow as tf

import nltk
from nltk import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

intents = json.loads(open('intents.json').read())