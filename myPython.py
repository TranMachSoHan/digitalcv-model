# importing required modules
from json import load
import zipfile

def load_data():
  print("Initializing recommender model")

  filepath = './'
  zf = zipfile.ZipFile('./pickle_folder/contentBaseDf.zip')
  # if you want to see all files inside zip folder
  print(zf.namelist() )


load_data()
