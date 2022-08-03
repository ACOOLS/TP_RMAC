import os
from shutil import copyfile

#FUNCTIONS
def str_to_class(str):
    return getattr(sys.modules[__name__], str)

def new_format_classification(old_dataset,new_base):
    classe_list=[]
    for j in os.listdir(old_dataset) :
        data = os.path.join(dataset_path, j)

        if not data.endswith(".jpg"):
            continue
        file_name = os.path.basename(data)
        classe_list.append(file_name.split('_')[0])
    classe_list=list(set(classe_list))

    for k in range(0,len(classe_list)):
        if os.path.exists(new_base+"/"+str(classe_list[k])) == False:
            os.makedirs(new_base+"/"+str(classe_list[k]))

    for j in os.listdir(old_dataset) :
        data = os.path.join(old_dataset, j)

        if not data.endswith(".jpg"):
            continue
        file_name = os.path.basename(data)
        id=file_name.split('_')[0]
        shutil.copy2(data, new_base+"/"+str(id)+"/"+file_name)
    command = os.popen('ls NEW_GHIM > classes.txt')


def get_classes(classes_path,num_classes):
    # Récupurer les noms des classes
    with open(classes_path, 'r') as f:
        classes = f.readlines()
        classes = list(map(lambda x: x.strip(), classes))
    # Récupurer les images et les classes
    input_paths, labels = [], []
    for class_name in os.listdir(dataset_path):
        class_path = os.path.join(dataset_path, class_name)
        class_id = classes.index(class_name)
        for path in os.listdir(class_path):
            path = os.path.join(class_path, path)
            if imghdr.what(path) == None:
                # this is not an image file
                continue
            input_paths.append(path)
            labels.append(class_id)
        # convert labels to one-hot-vector format
    labels = to_categorical(labels, num_classes=num_classes)

    # convert input paths to numpy array
    input_paths = np.array(input_paths)

    # shuffle dataset (permuter les données)
    perm = np.random.permutation(len(input_paths))
    labels = labels[perm]
    input_paths = input_paths[perm]

    # split dataset for training and validation

    percent = 80 #@param {type:"slider", min:0, max:100, step:5}
    border = int(len(input_paths) * (percent/100))
    train_labels, val_labels = labels[:border], labels[border:]
    train_input_paths, val_input_paths = input_paths[:border], input_paths[border:]
    print("Training on %d images and labels" % (len(train_input_paths)))
    print("Validation on %d images and labels" % (len(val_input_paths)))
    return train_input_paths,val_input_paths,train_labels,val_labels

def val_train_bases(new_base_dir,dataset_name):
		# # Creating Train / Val / Test folders (One time use)
	bases = dataset_name

	test_files=0
	val_files=0
	train_files=0
	all_files=0
	train = None
	val = None
	test = None
	train_FileNames = None
	val_FileNames = None 
	test_FileNames = None
	train=new_base_dir +'/train'
	val=new_base_dir +'/val'
	test=new_base_dir +'/test'

	if os.path.exists(train) == False:
	    os.makedirs(train)
	if os.path.exists(val) == False:
	    os.makedirs(val)
	if os.path.exists(test) == False:
	    os.makedirs(test)


	# Creating partitions of the data after shuffeling
	#currentCls = bases
	src = dataset_name # Folder to copy images from

	for j in os.listdir(src):
	    class_path = os.path.join(src, j)
	    allFileNames=[]
	    for k in os.listdir(class_path):
	      allFileNames.append(j+"/"+k)
	    if os.path.exists(train+"/"+j) == False:
	      os.makedirs(train+"/"+j)
	    if os.path.exists(val+"/"+j) == False:
	      os.makedirs(val+"/"+j)
	    if os.path.exists(test+"/"+j) == False:
	      os.makedirs(test+"/"+j)
	    np.random.shuffle(allFileNames)
	    train_FileNames, val_FileNames, test_FileNames = np.split(np.array(allFileNames),
	                                                              [int(len(allFileNames)*0.7), int(len(allFileNames)*0.85)])
	    train_FileNames = [name for name in train_FileNames.tolist()]
	    train_files=train_files+len(train_FileNames)
	    for i in range (0,len(train_FileNames)):
	      copyfile(src+"/"+train_FileNames[i], train+"/"+train_FileNames[i])
	    
	    val_FileNames = [name for name in val_FileNames.tolist()]
	    val_files=val_files+len(val_FileNames)
	    for i in range (0,len(val_FileNames)):
	      copyfile(src+"/"+val_FileNames[i], val+"/"+val_FileNames[i])
	    
	    test_FileNames = [name for name in test_FileNames.tolist()]
	    test_files=test_files+len(test_FileNames)
	    for i in range (0,len(test_FileNames)):
	      copyfile(src+"/"+test_FileNames[i], test+"/"+test_FileNames[i])

	print('Total images: ', train_files+val_files+test_files)
	print('Training: ', train_files)
	print('Validation: ', val_files)
	print('Testing: ', test_files)
	return train_files,val_files,test_files,train,val,test




