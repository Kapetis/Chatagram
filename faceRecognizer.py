import kairos_face
import os

kairos_face.settings.app_id = '9f5f1c2f'
kairos_face.settings.app_key = '61fc6b903f001e2943971eaba823556f'

dir_path = os.path.dirname(os.path.realpath(__file__))
#img = '/home/anshuman/coding_practice/testing/kairos-face-sdk-python/data/testy.jpg'

def facerec(web_img):
    print(web_img)
    recognized_faces = kairos_face.recognize_face(file=web_img, gallery_name='bank-faces')
    for x in range(len(recognized_faces)):
        return recognized_faces['images'][x]['candidates'][0]['subject_id']


def enroll_faces():
    kairos_face.enroll_face(file=dir_path+'/data/anshuman.jpg', subject_id='2323', gallery_name='bank-faces')

    kairos_face.enroll_face(file=dir_path+'/data/karan.jpg', subject_id='1234', gallery_name='bank-faces')

    kairos_face.enroll_face(file=dir_path+'/data/vidushi.jpg', subject_id='4444', gallery_name='bank-faces')
