import os

# Import Model from fastai
from fastai.vision import load_learner, open_image

# Flask utils
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

# Define a flask app
app = Flask(__name__)

learn = load_learner("models", 'Model_train_97_30epoc.pkl')

print('Model loading...')
print('Model loaded. Started serving...')
print('Model loaded. Check http://127.0.0.1:5000/')

def class_pred(img_path):
    
    img = open_image(img_path)
    pred_class,pred_idx,outputs = learn.predict(img)

    return str(pred_class)


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index1.html')

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['image']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        print('Begin Model Prediction...')

        # Make prediction
        preds = class_pred(file_path)

        print('End Model Prediction...')
        
        return preds
    return None

if __name__ == '__main__':    
    app.run(debug=False, threaded=False)