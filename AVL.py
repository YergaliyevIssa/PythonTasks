#height of node == number of vertex in longest path
class TreeNode:
	def __init__(self, key):
		self.key = key
		self.height = 1
		self.left = None
		self.right = None



class AVLtree:
	
	def insert(self, root, key):
		
		if root == None:
			return TreeNode(key)
		elif key < root.key:
			root.left = self.insert(root.left, key)
		else:
			root.right = self.insert(root.right, key)

			
		root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1

		balance = self.get_balance(root)

		if balance < -1:
			if key >= root.right.key:
				root = self.LeftRotate(root)
			else: 
				root.right = self.RightRotate(root.right)
				root = self.LeftRotate(root)
			
		elif balance > 1:
			if key < root.left.key:
				root - self.RightRotate(root)
			else:
				root.left = self.LeftRotate(root.left)
				root = self.RightRotate(root)

		return root

	def delete(self, root, key):


	def find(self, root, key):
		if root == None:
			return False
		if root.key == key:
			return (True, root)
		if key < root.key:
			return self.find(root.left, key)
		if key > root.key:
			return self.find(root.right, key)


	def get_height(self, root):
		if root != None:
			return root.height
		return 0


	def get_balance(self, root):

		return self.get_height(rool.left) - self.get_height(root.right)

	def LeftRotate(self, root):
		new_root = root.right
		tmp = new_root.left

		new_root.left = root
		root.right = tmp

		root.height =  max(self.get_height(root.left), self.get_height(root.right)) + 1
		new_root.height =  max(self.get_height(new_root.left), self.get_height(new_root.right)) + 1

		return new_root

	def RightRotate(self, root):
		new_root = root.left
		tmp = new_root.right

		new_root.right = root
		root.left = tmp

		root.height =  max(self.get_height(root.left), self.get_height(root.right)) + 1
		new_root.height =  max(self.get_height(new_root.left), self.get_height(new_root.right)) + 1

		return new_root


	def InOrderByPass(self, root):
		if root.left != None:
			self.InOrderByPass(root.left)
		print(root.key)
		if root.right != None:
			self.InOrderByPass(root.right)


def main():
	import random



if __name__ == '__main__':
	main()