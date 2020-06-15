# Below two lines need to be commented
import map_10
import map_40
import math

def shortest_path(M,start,goal):

	if start == goal :
		return [start]

	path_obj={}
	path_obj["intersect"] = start
	path_obj["path"] = [start]
	path_obj["g_cost"] = 0
	path_obj["h_est"]  = get_distance(M,start,goal)
	path_obj["f_total"] = path_obj["g_cost"] + path_obj["h_est"] 
 	
	path_obj_list =[]
	path_obj_list.append(path_obj) 
	goal_path_list = []
	p =None



	while (len(path_obj_list) > 0 ):
		goal_reached = False

		#sort the  Path_obj_list in descending order with the min total cost at the end
		path_obj_list.sort(key=lambda p:p["f_total"],reverse=True )
		#remove the last element with the least total cost  f= g+h
		if len(path_obj_list) >0 :
			p = path_obj_list.pop()
		else:
			break

		if p == None:
			break

		intersect_expand = p["intersect"]


		for i in M.roads[intersect_expand]:
			new_path_obj  = create_path_obj(M,i,intersect_expand,p,goal,goal_path_list)
			if new_path_obj :
				# Check if any path_obj has reached the goal such that the path_obj["h_est"] = 0 .
				if new_path_obj["h_est"] == 0 :
					#Add the path  to a new list as a potential candiate for the min paths from start to goal
					goal_path_list.append(new_path_obj)
					goal_path_list.sort(key = lambda p:p["f_total"])
					goal_reached = True
				else:
					if goal_reached == True :
						if new_path_obj['f_total'] < goal_path_list[0]['f_total']:
							path_obj_list.append(new_path_obj)
					else :
						path_obj_list.append(new_path_obj)

	if(len(goal_path_list)>0):
		return goal_path_list[0]['path']
	else:
		return None



def create_path_obj(M,next_intersect,intersect,path_obj,goal,goal_path_list):

	if next_intersect in path_obj["path"] :
		return None
	else:
		next_path_obj={}
		next_path_obj["intersect"] = next_intersect
		next_path_obj["path"] = [] 
		for i in path_obj['path']:
			next_path_obj["path"].append(i)
		next_path_obj["path"].append(next_intersect)
		next_path_obj["g_cost"] = path_obj["g_cost"]+get_distance(M,path_obj["intersect"],next_intersect)
		next_path_obj["h_est"]  = get_distance(M,next_intersect,goal)
		next_path_obj["f_total"] = next_path_obj["g_cost"] + next_path_obj["h_est"] 
		if len(goal_path_list)> 0 :
			if next_path_obj['f_total'] <= goal_path_list[0]['f_total']:
				return next_path_obj
			else:
				return None
		else:
			return next_path_obj



def get_distance(M,s,d):
	source =  M.intersections[s]
	dest   =  M.intersections[d]
	return math.sqrt((source[0]-dest[0])**2 + (source[1]-dest[1])**2)



if __name__ == '__main__':

#	show_map(map_40, start=5, goal=34, path=[5,16,37,12,34])
#	path = shortest_path(map_10, 0, 3)
	path = shortest_path(map_40, 5, 34)
	print(path)

	if path == [5, 16, 37, 12, 34]:
		print("great! Your code works for these inputs!")
	else:
		print("something is off, your code produced the following:")

		#print(path)

	path = shortest_path(map_40, 8, 24)
	print(path)
	if path == [8, 14, 16, 37, 12, 17, 10, 24]:
		print("great! Your code works for these inputs!")
	else:
		print("something is off, your code produced the following:")


	path = shortest_path(map_40, 5, 5)
	print(path)
	if path == [5]:
		print("great! Your code works for these inputs!")
	else:
		print("something is off, your code produced the following:")





