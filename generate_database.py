import os
from shutil import copyfile
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    '''
    Command line options
    '''
    parser.add_argument(
        '--num_images', type=str,default='10',
        help='number of images per class'
    )
    parser.add_argument(
        '--num_class', type=str,default='20',
        help='number of class'
    )
    parser.add_argument(
        '--base', type=str,default='GHIM-10K',
        help='Your datasets  '
    )
    FLAGS = parser.parse_args()
    num_images = FLAGS.num_images
    num_class = FLAGS.num_class
    datasets = FLAGS.base
    total_images=int(num_images)*int(num_class)
    if int(total_images) % 1000 == 0 :
        last_word = int(total_images/1000)
        last_word = str(last_word) + "K"
    else :
        last_word = total_images
    new_datasets=datasets.split('-')[0]+"-"+str(last_word)
    if os.path.exists(new_datasets) == False:
        os.makedirs(new_datasets)
    current_classe = 0
    current_number = 1
    for i_images in range(0,int(total_images)) :    
        current_number_per_class = 1
        for j in os.listdir(datasets) :
            if not j.endswith(".jpg"):
                continue
            class_number, number = j.split("_")
            #number = number.split(".")[0]
            #number = int(number)
            data = os.path.join(datasets, j)
            #print ("current_classe : "+ str(current_classe))
            if int(current_number_per_class)  <= int(num_images) :
                if int(class_number) == int(current_classe) :
                    copyfile(data, new_datasets+"/"+str(class_number)+"_"+str(current_number)+".jpg")
                    current_number = current_number + 1
                    current_number_per_class = current_number_per_class + 1
        current_classe = current_classe + 1
            
        





