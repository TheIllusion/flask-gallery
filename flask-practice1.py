from flask import Flask, render_template
import os, glob

app = Flask(__name__)

#REPORT_DIRECTORY_PATH = '/Users/Illusion/IdeaProjects/flask-practice1/static/gallery/'
REPORT_DIRECTORY_PATH = '/Users/Illusion/PycharmProjects/flask-gallery/static/gallery/'

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/gallery/<directory_name>')
# show the images in the date directory
def show_images_of_the_dir(directory_name):
    print 'directory_name = ', directory_name

    img_path = os.path.join(REPORT_DIRECTORY_PATH, directory_name)
    if os.path.exists(img_path):
        print 'the path exists: ', img_path
        os.chdir(img_path)
        img_list = glob.glob('*.jpg')
        print img_list
        return render_template('gallery.html', dir_name=directory_name, img_list=img_list)
    else:
        return 'path does not exist'

@app.route('/view_image_columns/<directory_name>')
# show the images in columns
def show_images_in_columns(directory_name):

    # get the names of sub-directories
    print 'directory_name = ', directory_name

    img_path = os.path.join(REPORT_DIRECTORY_PATH, directory_name)
    if os.path.exists(img_path):
        print 'the path exists: ', img_path
        os.chdir(img_path)
        img_list = glob.glob('*.jpg')
        print img_list
        return render_template('view_image_columns.html', dir_name=directory_name, img_list=img_list)
    else:
        return 'path does not exist'

    return render_template('view_image_columns.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
