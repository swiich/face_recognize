import avHash
import hamming

img_path = ('.\img\\timg1.jpg', '.\img\\timg0.jpg')

if __name__ == '__main__':
    ham = hamming.hamming(avHash.get_hash(img_path[0]), avHash.get_hash(img_path[1]))
    print(avHash.get_hash(img_path[0]))
    print(avHash.get_hash(img_path[1]))
    print(ham)
    if ham == 0:
        print('the same pic')
    elif ham <= 5:
        print("image alike")
    else:
        print('not alike')
