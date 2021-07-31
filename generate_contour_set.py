import json
import numpy as np
import cv2

res = []
for pic in range(1, 12):
    t = json.load(open("{}.json".format(pic)))
    img = cv2.imread("org/{}.jpg".format(pic))

    all_lines = t["shapes"]
    for k in range(len(all_lines)):
        contour = {}
        graph = np.zeros(img.shape)
        graph[:] = 1
        points = all_lines[k]["points"]
        for i in range(len(points)):
            cv2.line(graph, pt1=(int(points[i][0]), int(points[i][1])),
                    pt2=(int(points[(i+1)%len(points)][0]), int(points[(i+1)%len(points)][1])),
                    color=(0, 0, 0),
                    thickness=2)

        contour['line'] = points
        contour['graph'] = graph
        res.append(contour)
res = np.array(res, dtype=object)
np.save('contour.npy', res)
    
