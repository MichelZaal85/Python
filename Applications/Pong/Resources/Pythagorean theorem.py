import math

# python, list of coordinates

[p[0],p[1],q[0],q[1]]
# 	X			Y


# Pythagorean theorem
	def dist(p, q):
		return math.sqrt((p[0]-q[0])**2 + (p[1]-q[1])**2)


'''
        	
        	      	    .. p = [p[0],p[1]]
        	      	   . .
        	          .  .
        	         .   .
        	        .    .
        	       .     .
        	      .      . p[1] - q[1]
         	    .        .
         	   .         .
         	  .          .
q = q[0],q[1] `...........

				p[0] - q[0]


'''



