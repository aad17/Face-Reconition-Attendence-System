import face_recognition
import numpy
from os import listdir, path
from FaceSQL import FaceSQL


class FaceTools:
    def __init__(self):
        try:
            self.facesql = FaceSQL()
        except:
            print("Database connection error")

    def encoding_FaceStr(self, image_face_encoding):
        # Convert numpy array type to list
        encoding__array_list = image_face_encoding.tolist()
        # Convert the elements in the list to a string
        encoding_str_list = [str(i) for i in encoding__array_list]
        # Splice the strings in the list
        encoding_str = ','.join(encoding_str_list)
        return encoding_str

    def decoding_FaceStr(self, encoding_str):
        # print("name=%s,encoding=%s" % (name, encoding))
        # Convert string to numpy ndarray type, that is, matrix
        # Convert to a list
        dlist = encoding_str.strip(' ').split(',')
        # Convert str from list to float
        dfloat = list(map(float, dlist))
        face_encoding = numpy.array(dfloat)
        return face_encoding

    def add_Face(self, image_name, id):
        # Load local image file to a numpy ndarray type object
        image = face_recognition.load_image_file("./photo/"+image_name)
        # Return the 128-dimensional face encoding of each face in the image
        # There may be multiple faces in the image, remove the face code marked with 0 to indicate the clearest face recognized
        image_face_encoding = face_recognition.face_encodings(image)[0]
        encoding_str = self.encoding_FaceStr(image_face_encoding)
        # Store face feature codes in the database
        self.facesql.saveFaceData(id, encoding_str)

    def updata_Face(self, image_name, id):
        # Load local image file to a numpy ndarray type object
        image = face_recognition.load_image_file("./photo/"+image_name)
        # Return the 128-dimensional face encoding of each face in the image
        # There may be multiple faces in the image, remove the face code marked with 0 to indicate the clearest face recognized
        image_face_encoding = face_recognition.face_encodings(image)[0]
        encoding_str = self.encoding_FaceStr(image_face_encoding)
        # Update the database of face feature encoding
        self.facesql.updateFaceData(id, encoding_str)

    def sreach_Face(self, id):
        face_encoding_strs = self.facesql.sreachFaceData(id)
        # Face feature coding collection
        face_encodings = []
        # Face feature name collection
        face_names = []
        for row in face_encoding_strs:
            name = row[0]
            face_encoding_str = row[1]
            # Append the information obtained from the database to the collection
            face_encodings.append(self.decoding_FaceStr(face_encoding_str))
            face_names.append(name)
        return face_names, face_encodings

# THIS FUNCTION IS IMPORTANT
    def load_faceoffile(self):
        filepath = 'photo'
        filename_list = listdir(filepath)
        # Face feature coding collection
        face_encodings = []
        # Face feature name collection
        face_names = []
        a = 0
        for filename in filename_list:  # read the contents of the list in sequence

            if filename.endswith('jpg'):  # Suffix name'jpg' matches
                # Remove the last four digits of the file name.jpg to get the person's name
                face_names.append(filename[:-4])
                file_str = 'photo' + '/' + filename
                a_images = face_recognition.load_image_file(file_str)
                print(file_str)
                a_face_encoding = face_recognition.face_encodings(a_images)[0]
                face_encodings.append(a_face_encoding)
            a += 1
        print(face_names, a)
        return face_names, face_encodings

    def load_faceofdatabase(self):
        try:
            face_encoding_strs = self.facesql.allFaceData()
        except:
            print("Database connection error")
    # Face feature coding collection
        face_encodings = []
    # Face feature name collection
        face_names = []
        for row in face_encoding_strs:
            name = row[0]
            face_encoding_str = row[1]
            # Append the information obtained from the database to the collection
            face_encodings.append(self.decoding_FaceStr(face_encoding_str))
            face_names.append(name)
        return face_names, face_encodings

    def load_images_face(self, filepath):
        filename_list = listdir(filepath)
        for filename in filename_list:  # read the contents of the list in sequence
            if path.isdir(filepath+filename):
                self.load_images_face(filepath+filename+"\\")
                if filename.endswith('jpg'):  # Suffix name'jpg' matches
                    file_str = filepath + filename
                    a_images = face_recognition.load_image_file(file_str)
                    print(file_str)
                    face_encoding = face_recognition.face_encodings(a_images)
                if face_encoding != []:
                    a_face_encoding = face_encoding[0]
                    encoding_str = self.encoding_FaceStr(a_face_encoding)
                    self.facesql.saveFaceData(filename[:-4], encoding_str)

    def load_images_faces(self, filepath):
        filename_list = listdir(filepath)
        a = 0
        for filename in filename_list:  # read the contents of the list in sequence
            if filename.endswith('jpg'):  # Suffix name'jpg' matches
                file_str = filepath + filename
                a_images = face_recognition.load_image_file(file_str)
                print(file_str)
                face_encoding = face_recognition.face_encodings(a_images)
                for a_face_encoding in face_encoding:
                    a += 1
                    encoding_str = self.encoding_FaceStr(a_face_encoding)
                    self.facesql.saveFaceData(
                        filename[:-4] + "-" + str(a), encoding_str)


obj = FaceTools()
obj.add_Face("69.jpg", 69)
