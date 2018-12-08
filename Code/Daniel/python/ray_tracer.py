from PIL import Image, ImageDraw
import math
import numpy as np

#   Camera location

#   Sphere dimensions and location
#   Light source dimensions and location 
class Sphere():
    def __init__(self, center, radius, color):    # Position as center of sphere
        self.center = center
        self.radius = radius
        self.color = color
    



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
    
    


#   Find if ray intersects with sphere and return distance along the ray
#   return 1st point on ray that is {radius} distance from sphere.position 
#   Computation Ref: https://www.scratchapixel.com/lessons/3d-basic-rendering/minimal-ray-tracer-rendering-simple-shapes/ray-sphere-intersection
def intersection(ray, obj):  # Ray is from camera origin to current pixel in render
    dist_origin_to_center = get_magnitude(ray.origin, obj.center)
    ray_magnitude = get_magnitude(ray.origin, ray.vector)
    ray_vector_normal = [ray.vector[0]/ray_magnitude, ray.vector[1]/ray_magnitude, ray.vector[2]/ray_magnitude]

    # Projection of dist_origin_to_center onto normalized ray
    projection = np.dot(ray_vector_normal, dist_origin_to_center)

    # Returns None if projection is negative. Negative projections are potentially behind camera?
    if projection < 0: 
        return None 
     
    dist_center_to_ray = math.sqrt(dist_origin_to_center**2 - projection**2)
    if dist_center_to_ray < 0:
        return None

    if dist_center_to_ray > obj.radius:
        return None

    side = math.sqrt(obj.radius**2 - dist_center_to_ray**2)     # Needed to computate distance from origin to intersection
    dist_intersect = ray_magnitude - side

    # Verified format and calculation as correct using python interactive
    hit_point = list(np.asarray(ray.origin) + list(np.asarray(ray_vector_normal) * dist_intersect))

    return hit_point

def get_magnitude(origin, direction):
    #   Verified as correct calculation. Refer to ray_test.py
    magnitude = math.sqrt((origin[0] - direction[0])**2 + (origin[1] - direction[1])**2 + (origin[2] - direction[2])**2)


#   Create scene (As constant? Ref:https://softwareengineering.stackexchange.com/questions/342374/should-i-really-use-all-uppercase-for-my-constants )
#       - Create two spheres. One for sphere, one for light. Creating a sphere object vs calling a get_sphere function?
#         Requires position, radius, and color to create
#       - Create plane. Use point-normal form? (Ref: https://en.wikipedia.org/wiki/Plane_(geometry)#Point-normal_form_and_general_form_of_the_equation_of_a_plane)
SCENE = [
    Sphere([0,0,0], 0, [255,255,0]),     # Light (Yellow)
    Sphere([0,0,0], 0, [0,0,255]),       # Sphere (Blue)
    # Plane([0,0,0,],[0,0,0], [0,255,0]),  # Ground (Green)
]



#   Render the image (by pixel?)

render = Image.new('RGB', (800, 600), color = 0)
render.show()





