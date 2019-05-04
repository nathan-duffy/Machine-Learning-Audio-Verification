#Imports
from flask import Flask, request, render_template, jsonify
import pickle
import numpy as np
from skimage.io import imread
import skimage


app = Flask(__name__)

with open('model.pkl', 'rb') as fid:
	model = pickle.load(fid)


#converts to features for ML gives an overall idea of how much black is in the pic
def spek_to_feature(picture):

	im = imread(picture, as_gray = True)

	#Crop Picture to get rid of top section
	#50 pixels is the standard header
	im = im[58:]

	#Find Bounds of image (to give baseline)
	y_bound, x_bound = im.shape

	#Looping across the x-axis (predefined resolution)
	final_score = []

	for ii in range(0, x_bound-1):
	    #Reset Score per-coluimn
	    score = 0
	    for jj in range(0, y_bound-1): #Loop down each "x column"
	        try:
	            if im[ii, jj] == 0:
	                score -= 1
	            elif im[ii,jj] != 0:
	                score += 1
	        except:
	            'IndexError'

	    final_score.append(score)

	return np.asarray(final_score)


@app.route('/')
def render():
	 return render_template('home.html')

@app.route('/', methods=['POST'])
def home():
	if request.method=='POST':
		picture = request.files['file']
		features = spek_to_feature(picture)
		output = str(model.predict([features]))
		proba = np.amax(model.predict_proba([features]))

		return render_template('home.html',output=output,proba=proba)


@app.route("/instructions")
def about():
	return render_template('instructions.html')

if __name__ == '__main__':
	app.debug = True
	app.run()
