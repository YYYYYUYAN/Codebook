import argparse 



if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Parameter setting')
  parser.add_argument('--pretrain', type=str, default='chackpoint/resnet.pth', help='pretrain model path')
  parser.add_argument('--data', type=str, default='data' help='data path')
  args = parser.parse_args()
  
  
