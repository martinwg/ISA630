def Conv2D(image, kernel):
  input_height = image.shape[0]
  input_width = image.shape[1]
  kernel_height = kernel.shape[0]
  kernel_width = kernel.shape[1]

  output_height = input_height - kernel_height + 1
  output_width = input_width - kernel_width + 1

  output_image = np.zeros((output_height, output_width))
  for i in range(0, output_height):
    for j in range(0, output_width):
      for ii in range(0, kernel_height):
        for jj in range(0, kernel_width):
          output_image[i,j] += image[i+ii, j+jj] * kernel[ii,jj]

  return output_image
