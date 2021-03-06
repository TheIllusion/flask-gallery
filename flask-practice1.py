from flask import Flask, render_template
import os, glob

app = Flask(__name__)

#GALLERY_REPORT_DIRECTORY_PATH = '/Users/Illusion/IdeaProjects/flask-practice1/static/gallery/'
GALLERY_REPORT_DIRECTORY_PATH = '/data1/users/rklee/flask-gallery/static/gallery/'

COLUMN_VIEW_REPORT_DIRECTORY_PATH = '/data1/users/rklee/flask-gallery/static/view_image_columns/'

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/gallery/')
def show_dirs_in_gallery():
    if os.path.exists(GALLERY_REPORT_DIRECTORY_PATH):
        os.chdir(GALLERY_REPORT_DIRECTORY_PATH)
        sub_directories = glob.glob('*')

        full_string = ''
        for sub_dir in sub_directories:
            full_string = full_string + '[' + sub_dir + ']  '

        return full_string

@app.route('/gallery/<directory_name>/')
# show the images in the date directory
def show_images_of_the_dir(directory_name):
    print 'directory_name = ', directory_name

    img_path = os.path.join(GALLERY_REPORT_DIRECTORY_PATH, directory_name)
    if os.path.exists(img_path):
        print 'the path exists: ', img_path
        os.chdir(img_path)
        img_list = glob.glob('*.jpg')
        print img_list
        return render_template('gallery.html', dir_name=directory_name, img_list=img_list)
    else:
        return 'path does not exist'

@app.route('/columns/')
def show_dirs_in_columns():
    if os.path.exists(COLUMN_VIEW_REPORT_DIRECTORY_PATH):
        os.chdir(COLUMN_VIEW_REPORT_DIRECTORY_PATH)
        sub_directories = glob.glob('*')

        full_string = ''
        for sub_dir in sub_directories:
            full_string = full_string + '[' + sub_dir + ']  '

        return full_string

@app.route('/columns/<directory_name>/')
# show the images in columns
def show_images_in_columns(directory_name):

    # get the names of sub-directories
    print 'directory_name = ', directory_name

    img_path = os.path.join(COLUMN_VIEW_REPORT_DIRECTORY_PATH, directory_name)
    if os.path.exists(img_path):
        os.chdir(img_path)
        sub_directories = glob.glob('*')

        print 'list of sub-directories: ', sub_directories

	sub_directories.sort()

        img_list_searched = False

        for directory in sub_directories:

            dir_fullpath = os.path.join(img_path, directory)

            if os.path.exists(dir_fullpath) and img_list_searched == False:
                print 'sub-dir: ', dir_fullpath
                os.chdir(dir_fullpath)
                img_list = glob.glob('*.png')
                img_list_searched = True
                print img_list
            elif img_list_searched == True:
                pass
            else:
                return 'sub-dir path does not exist'

        for i in range(len(sub_directories)):
            sub_directories[i] = sub_directories[i].split('-')[1]
    else:
        return 'path does not exist'

    return render_template('view_image_columns.html', directory_name=directory_name,
                           sub_directories=sub_directories, len_sub_dir=len(sub_directories), img_list=img_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
