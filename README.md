## intuit_raspberypi_workshop
###start server to recieve training images
cd face_rec
python py_server.py
###
#start the intuit_demo/train_client.py file on the pi
press button to start clickin

#images stored at /face_rec on the server
##bash script to create a list of images to crop out the face
find face_rec/face_recognition/images/ -printf "%p\n" | grep .jpg | sort -d > filexlist.txt
#file list stored at /face_rec
cp filexlist.txt face_recognition/
#crop faces
perl face_rec/face_recognition/extractfaces/generate_traindata.pl
#generate image_list to indicate the set of images used for training
find face_rec/face_recognition/extractfaces/faces/ -printf "%p\n" | grep .jpg | sort -d > image_list.txt
#add labels 
<img_path>;<label_number>
cd train_recognizer
#build the model
./train ../image_list.txt new_dir/
#copy the model on to the pi
scp new_dir/lbph_model.yaml  pi@10.10.0.2:/home/pi/face_rec
cd to /face_rec/face_recognition/recognise on the pi
./classify to run the classifier.
Visit https://github.com/jayzsimha/face_recognition to setup openCV and for more instructins
