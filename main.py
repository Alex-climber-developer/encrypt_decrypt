
def encrypt():
  index54 = 54
  index0 = 0

  text = open('encrypt_decrypt/text.txt','r')
  text_str = str(text.read())

  start_img = open('encrypt_decrypt/start.bmp','rb')
  start_img_str=str(start_img.read())

  end_img = open('encrypt_decrypt/end.bmp','wb')
  first54 = str(start_img.read(54))
  # print(first54)
  end_img.write(first54)

  count_bits_all_bmp = (len(start_img_str)-54)
  bits_possible_mas = [k for k in [1,2,4] if len(text_str)*64//k - count_bits_all_bmp < 0 ]
  count_bits_inEnd = int(input(f' Enter count (smaller- better) bit which will cut, options- {bits_possible_mas}   '))

  if count_bits_inEnd not in bits_possible_mas:
    print('will 1')

  mask = (8 - count_bits_inEnd) * '1' + count_bits_inEnd * '0'
  # для кажд буквы
  while len(text_str) > 0:
    code_letter = str(ord(text_str[index0]))
    code_letter = (8 - len(code_letter)) * 0 + code_letter

    for _ in range(8/count_bits_inEnd):
      # для каждой части кода буквы
      each_code_letter = code_letter[index0 : index0 + count_bits_inEnd]
      each_code_letter = (8 - count_bits_inEnd) * 0 + each_code_letter

      index0 += count_bits_inEnd
      # code_letter = code_letter[count_bits_inEnd:] 

      each_pixel = start_img_str[index54:index54+8]
      after_mask = each_pixel & mask
      after_concat = after_mask | each_code_letter

      end_img.write(after_concat)

    text_str = text_str[1:]


def decrypt():


  start_img = open('encrypt_decrypt/start.bmp','rb')
  start_img_str=str(start_img.read())[54: ]
  end_text = open('encrypt_decrypt/end2.txt','wb')

  count_bits_inEnd = int(input(f' Enter count bit which will cut   '))
  while 1:
    # 
    code_letter=''

    # восьмерками перебирать буквы
    for i in range(0,len(start_img_str),8):
      each_pixel = start_img_str[i : i+8]
      if len(code_letter) != 8:
        code_letter += (each_pixel[-1 * count_bits_inEnd :])
      else:
        end_text.write(code_letter)
        code_letter = ''

  




def start():
  global encrypt
  while 1:
    choice=int(input('your choice: 1- encrypt , 2- decrypt, 3- quit (one integer):  '))

    if choice== 1:
      encrypt()

    elif choice== 2:
      decrypt()

    if choice== 3:
      print('End')
      break
      return


start()
