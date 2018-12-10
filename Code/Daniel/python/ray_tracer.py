from PIL import Image, ImageDraw
import math
import numpy as np

#   Camera location

#   Sphere dimensions and location
#   Light source dimensions and location 
class Sphere():
    def __init__(self, center, radius, color):    # Position at center of sphere
        self.center = center
        self.radius = radius
        self.color = color
    
    def get_center(self):
        return self.center
    
    def get_radius(self):
        return self.radius

    def get_color(self):
        return self.color

    



#   Image plane location
# class Plane():
#     def __init__(self, position, normal_vector, color):
#         self.position = position
#         self.normal_vector = normal_vector

    
#   Create ray from camera through image plane
class Ray():
    def __init__(self, origin, vector):
        self.origin = origin
        self.vector = vector
    
    def get_origin(self):
        return self.origin
    
    def get_vector(self):
        return self.vector


#   Find if ray intersects with sphere and return distance along the ray
#   return 1st point on ray that is {radius} distance from sphere.position 
#   Computation Ref: https://www.scratchapixel.com/lessons/3d-basic-rendering/minimal-ray-tracer-rendering-simple-shapes/ray-sphere-intersection
def intersection(ray, obj):  # Ray is from camera origin to current pixel in render
    dist_origin_to_center = get_magnitude(ray.get_origin(), obj.get_center())   # |L|
    vect_origin_to_center = list(np.asarray(ray.get_origin()) - np.asarray(sphere.get_center()))    #  L (vector)
    ray_magnitude = get_magnitude(ray.get_origin(), ray.get_vector())   # Magnitude of ray from origin through current pixel
    ray_vector_normal = [ray.get_vector()[0]/ray_magnitude, ray.get_vector()[1]/ray_magnitude, ray.get_vector()[2]/ray_magnitude]   # D

    # Projection of dist_origin_to_center onto normalized ray
    projection = np.dot(ray_vector_normal, vect_origin_to_center)   # t_ca

    # Returns None if projection is negative. Negative projections are potentially behind camera?
    # if projection < 0: 
    #     return None 
     
    try:
        dist_center_to_ray = math.sqrt(dist_origin_to_center**2 - projection**2)    # d
    except ValueError:
        return None
    # if dist_center_to_ray < 0:
    #     return None

    if dist_center_to_ray > obj.get_radius():
        return None

    try:
        side = math.sqrt(obj.radius**2 - dist_center_to_ray**2)    # t_hc. Needed to computate distance from origin to intersection
    except ValueError:
        return None


    dist_intersect = projection - side  # t_0
    # dist_intersect = ray_magnitude - side

    # Verified format and calculation as correct using python interactive
    hit_point = list(np.asarray(ray.get_origin()) + list(np.asarray(ray_vector_normal) * dist_intersect))   # P

    color = get_color(hit_point)

    return (color)

def get_magnitude(origin, direction):
    #   Verified as correct calculation. Refer to ray_test.py
    magnitude = math.sqrt((origin[0] - direction[0])**2 + (origin[1] - direction[1])**2 + (origin[2] - direction[2])**2)
    return magnitude

def get_color(position):
    return (0,0,255)


#   Create scene (As constant? Ref:https://softwareengineering.stackexchange.com/questions/342374/should-i-really-use-all-uppercase-for-my-constants )
#       - Create two spheres. One for sphere, one for light. Creating a sphere object vs calling a get_sphere function?
#         Requires position, radius, and color to create
#       - Create plane. Use point-normal form? (Ref: https://en.wikipedia.org/wiki/Plane_(geometry)#Point-normal_form_and_general_form_of_the_equation_of_a_plane)

light = Sphere([200,300,20], 20, [255,255,0])     # Light (Yellow)
sphere = Sphere([400,300,100], 5, [0,0,255])       # Sphere (Blue)
    # Plane([0,0,0,],[0,0,0], [0,255,0]),  # Ground (Green)




#   Render the image (by pixel?)
width = 800
height = 600
render = Image.new('RGB', (width, height), color = 0)
pixels = render.load()
camera_coord = [0, 0, 20 ]
image_plane_z = 90
for i in range(width):
    for j in range(height):
        ray = Ray(camera_coord, [i,j,image_plane_z])
        if intersection(ray, sphere) != None:
            pixels[i,j] = intersection(ray, sphere)
            print('Hit!')
        if intersection(ray, light) != None:
            pixels[i,j] = (255,255,0)
            print('light hit!')
render.show()


vect_origin_to_center = list(np.asarray(ray.get_origin()) - np.asarray(sphere.get_center()))  # [0,0,-25]
dist_origin_to_center = get_magnitude(ray.get_origin(), sphere.get_center())    # 25.0
ray_magnitude = get_magnitude(ray.get_origin(), ray.get_vector())   # 991.65
# [0.8057, 0.6040, 0.0]
ray_vector_normal = [ray.get_vector()[0]/ray_magnitude, ray.get_vector()[1]/ray_magnitude, ray.get_vector()[2]/ray_magnitude]
# [20.1432, 15.1011. 0.      ] ??
projection = np.dot(ray_vector_normal, dist_origin_to_center)

# print(get_color())
# print(vect_origin_to_center)


