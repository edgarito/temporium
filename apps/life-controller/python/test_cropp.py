# Importation des bibliotheques
from PIL import Image 
import colorsys
import time
import os,sys
import threading

def image_cropping(image_a_traiter,outfile,a,b,c,d):

	im = Image.open(image_a_traiter)

	uneImage = im.crop((a,b,c,d))

	uneImage.save(outfile,"jpeg")


compteur = 0


while compteur < 5 :


	print "Start image analysis"

	# Ecrire le nom du path ou seront enregistrees les photos
	PathToFile = "/home/edgar/python_ws/Scripts_WorkShop_Avril/Scripts_finaux"

	os.system("streamer -s 1920x1080 -f jpeg -c /dev/video0 -b 16 -o "+ PathToFile + "/im_BU_level.jpeg")
	os.system("streamer -s 1920x1080 -f jpeg -c /dev/video0 -b 16 -o "+ PathToFile + "/im_BR_level.jpeg")


	#os.system("imagesnap -d DV " + PathToFile + "/im_BU_level.jpeg")
	#os.system("imagesnap -d DV " + PathToFile + "/im_BR_level.jpeg")


	time.sleep(1)


	#Changer le nom des paths

	#Path jusqu'a l'image a cropper 
	image_BU = PathToFile + "/im_BU_level.jpeg"
	image_BR = PathToFile + "/im_BR_level.jpeg"

	#Path jusqu'au dossier ou les sous-images seront sauvegardees
	PathToFile_croppedImages = PathToFile

	outfile_BU1 = PathToFile_croppedImages + "/BU1.jpeg"
	outfile_BU2 = PathToFile_croppedImages + "/BU2.jpeg"
	outfile_BU3 = PathToFile_croppedImages + "/BU3.jpeg"
	outfile_BR1 = PathToFile_croppedImages + "/BR1.jpeg"
	outfile_BR2 = PathToFile_croppedImages + "/BR2.jpeg"
	outfile_BR3 = PathToFile_croppedImages + "/BR3.jpeg"

	# rentrer a la main les coordonnees a,b et c,d qui sont differents pour chacune des photos
	a = 10
	b = 10
	c = 50
	d = 50

	image_cropping(image_BU,outfile_BU1,a,b,c,d)
	image_cropping(image_BU,outfile_BU2,a,b,c,d)
	image_cropping(image_BU,outfile_BU3,a,b,c,d)
	image_cropping(image_BR,outfile_BR1,a,b,c,d)
	image_cropping(image_BR,outfile_BR2,a,b,c,d)
	image_cropping(image_BR,outfile_BR3,a,b,c,d)

	#
	imBU1 = Image.open(outfile_BU1)
	imBU2 = Image.open(outfile_BU2)
	imBU3 = Image.open(outfile_BU3)
	imBR1 = Image.open(outfile_BR1)
	imBR2 = Image.open(outfile_BR2)
	imBR3 = Image.open(outfile_BR3)


	#self.level_mesure("BR1.jpeg")

	#BU_level = "BU1 : " + str(level_mesure("BU1.jpeg")) + " , BU2 : " + str(self.level_mesure("BU2.jpeg")) + " , BU3 : " + str(self.level_mesure("BU3.jpeg")) + " , BR1 : " + str(self.level_mesure("BR1.jpeg")) + " , BR2 : " + str(self.level_mesure("BR2.jpeg")) + " , BR3 : " + str(self.level_mesure("BR3.jpeg")) + "\n"

	#print "message envoye :" + str(BU_level)




	#self.lock.release()

	#if not self.client._send(self.BU_level) :
	#	self.lock.acquire()
		
	print "End image analysis"

	compteur = compteur +1


