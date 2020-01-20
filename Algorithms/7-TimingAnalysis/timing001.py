import os, time
from bubble import bubbleSort
from mergesort import mergeSort
from quicksort import quickSort

DataSet = [89, 263, 481, 48, 57, 468, 301, 340, 419, 251, 333, 466, 422, 58, 274, 213, 25, 37, 462, 220, 473, 228, 359, 472, 215, 123, 145, 255, 210, 6, 262, 323, 258, 196, 460, 127, 401, 400, 485, 223, 449, 65, 214, 230, 252, 442, 467, 188, 438, 370, 95, 407, 21, 159, 315, 142, 334, 327, 450, 246, 111, 157, 45, 489, 322, 101, 212, 217, 171, 410, 371, 116, 5, 244, 12, 279, 260, 431, 418, 2, 164, 104, 18, 130, 185, 437, 135, 388, 249, 483, 39, 389, 50, 174, 205, 446, 51, 114, 67, 219, 434, 351, 79, 270, 414, 425, 416, 471, 280, 382, 314, 498, 26, 236, 54, 377, 143, 439, 237, 221, 103, 44, 112, 71, 364, 32, 420, 496, 299, 76, 81, 150, 363, 9, 482, 118, 403, 426, 406, 441, 316, 226, 350, 77, 10, 107, 288, 302, 488, 41, 499, 52, 459, 317, 408, 141, 35, 194, 117, 202, 487, 94, 443, 328, 191, 300, 38, 173, 429, 8, 342, 304, 53, 421, 494, 324, 34, 134, 152, 360, 80, 62, 203, 113, 72, 20, 486, 256, 27, 320, 478, 75, 88, 379, 264, 154, 64, 108, 490, 495, 269, 56, 132, 348, 380, 195, 90, 411, 303, 63, 458, 267, 318, 216, 233, 166, 30, 74, 326, 231, 385, 253, 137, 480, 3, 447, 16, 73, 278, 22, 66, 182, 374, 273, 346, 345, 14, 218, 357, 367, 165, 383, 291, 286, 266, 386, 91, 372, 381, 405, 308, 198, 329, 463, 180, 160, 109, 15, 199, 222, 424, 162, 423, 131, 55, 335, 227, 121, 476, 200, 272, 292, 93, 356, 362, 176, 415, 336, 310, 365, 339, 396, 358, 384, 452, 33, 445, 413, 321, 484, 387, 193, 190, 192, 455, 204, 352, 448, 28, 465, 40, 161, 84, 183, 147, 257, 184, 42, 96, 343, 276, 275, 68, 122, 290, 155, 287, 119, 409, 148, 235, 211, 49, 149, 207, 332, 240, 85, 461, 261, 24, 242, 373, 232, 355, 17, 158, 338, 250, 491, 296, 144, 297, 19, 13, 153, 168, 110, 225, 277, 167, 248, 179, 366, 430, 312, 435, 493, 376, 59, 36, 189, 163, 369, 330, 146, 97, 100, 87, 353, 139, 83, 337, 475, 254, 393, 464, 368, 31, 43, 106, 82, 394, 285, 105, 492, 283, 319, 177, 125, 201, 136, 60, 306, 453, 474, 457, 209, 305, 11, 417, 86, 156, 397, 78, 428, 92, 172, 23, 293, 497, 206, 331, 281, 69, 309, 181, 294, 361, 129, 169, 1, 395, 186, 402, 469, 234, 115, 241, 175, 398, 271, 120, 311, 440, 347, 128, 99, 391, 378, 479, 354, 470, 289, 133, 140, 444, 390, 284, 477, 399, 243, 46, 224, 170, 313, 454, 98, 375, 451, 178, 239, 432, 61, 70, 282, 298, 436, 404, 295, 344, 349, 197, 392, 151, 102, 4, 29, 124, 325, 433, 500, 456, 268, 247, 7, 229, 427, 245, 47, 265, 307, 412, 341, 208, 138, 259, 187, 238, 126]

BS_StartTime = time.time()
bubbleSort(DataSet)
BS_EndTime = time.time()

MS_StartTime = time.time()
mergeSort(DataSet)
MS_EndTime = time.time()

QS_StartTime = time.time()
quickSort(DataSet, 0, len(DataSet)-1)
QS_EndTime = time.time()
print('Random Samples sorted: ', len(DataSet))
print('Bubble Sort took ', str(BS_EndTime-BS_StartTime))
print('Merge Sort took ', str(MS_EndTime-MS_StartTime))
print('Quick Sort took ', str(QS_EndTime-QS_StartTime))

# dir_path = os.path.dirname(os.path.realpath(__file__))
# print(dir_path)