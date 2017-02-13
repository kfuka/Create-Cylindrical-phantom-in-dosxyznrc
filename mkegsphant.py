import math
materialnum=3
materials=["AIR700ICRU","ICRUTISSUE700ICRU","LUNG700ICRU"]
airdensity=0.001
tissuedensity=1
lungdensity=0.32
xnum=130
ynum=50
znum=130
boxcel=0.2#in cm
xmin=-13
xmax=13
ymin=-5
ymax=5
zmin=-13
zmax=13
f=open("/home/fukata/egsnrc_mp/dosxyznrc/test2.egsphant","w")
try:
	f.write(" "+str(materialnum)+"\n")
	for i in range(materialnum):
		f.write(materials[i]+"\n")
	f.write("   0.0000000       0.0000000       0.0000000\n")
	f.write("  "+str(xnum)+"   "+str(ynum)+"  "+str(znum)+"\n")
	for i in range(xnum+1):
		f.write("  "+str(xmin+boxcel*float(i))+"\t")
	f.write("\n")
	for i in range(ynum+1):
		f.write("  "+str(ymin+boxcel*float(i))+"\t")
	f.write("\n")
	for i in range(znum+1):
		f.write("  "+str(zmin+boxcel*float(i))+"\t")
	f.write("\n")
	for i in range(znum):
		for j in range(ynum):
			for k in range(xnum):
				if(math.sqrt((xmin+boxcel*float(k)+boxcel/2)**2+(zmin+boxcel*float(i)+boxcel/2)**2)<11):#Delta4
					if(math.sqrt((xmin+boxcel*float(k)+boxcel/2)**2+(zmin+boxcel*float(i)+boxcel/2)**2)<6):#chest wall
						if(math.sqrt((xmin+boxcel*float(k)+boxcel/2)**2+(zmin+boxcel*float(i)+boxcel/2)**2)<0.5):#Tumor (1cm)
							if(math.sqrt((ymin+boxcel*float(j)+boxcel/2)**2)<0.5):
								f.write("2")
							else:
								f.write("3")
						else:
							f.write("3")
					else:
						f.write("2")
				else:
					f.write("1")
			f.write("\n")
		f.write("\n")
		
	for i in range(znum):
		for j in range(ynum):
			for k in range(xnum):
				if(math.sqrt((xmin+boxcel*float(k)+boxcel/2)**2+(zmin+boxcel*float(i)+boxcel/2)**2)<11):#Delta4
					if(math.sqrt((xmin+boxcel*float(k)+boxcel/2)**2+(zmin+boxcel*float(i)+boxcel/2)**2)<6):#chest wall
						if(math.sqrt((xmin+boxcel*float(k)+boxcel/2)**2+(zmin+boxcel*float(i)+boxcel/2)**2)<0.5):#Tumor (1cm)
							if(math.sqrt((ymin+boxcel*float(j)+boxcel/2)**2)<0.5):
								f.write(str(tissuedensity)+"\t")
							else:
								f.write(str(lungdensity)+"\t")
						else:
							f.write(str(lungdensity)+"\t")
					else:
						f.write(str(tissuedensity)+"\t")
				else:
					f.write(str(airdensity)+"\t")
			f.write("\n")
		f.write("\n")
finally:
	f.close()
