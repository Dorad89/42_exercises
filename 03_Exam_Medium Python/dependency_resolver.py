#Subject: Given a dict mapping packages to their dependencies,
#return a valid install order (dependencies before dependents),
#raising an error on a cycle. 
#This is topological sort via DFS.


class DependencyResolver:
	def __init__(self, deps):
		self.deps = deps
		self.visited = set()
		self.visiting = set()
		self.order = []
	
	def resolve(self):
		for pkg in self.deps:
			if pkg not in self.visited:
				self._dfs(pkg)
		return self.order[::-1]
	
	def _dfs(self, pkg):
		if pkg in self.visiting:
			raise ValueError(f"Cyclic dependency detected involving '{pkg}'")
		
		if pkg in self.visited:
			return
		
		self.visiting.add(pkg)

		for dep in self.deps.get(pkg, []):
			self._dfs(dep)
			
		self.visiting.remove(pkg)
		self.visited.add(pkg)
		self.order.append(pkg)

# Claude version
class DependencyResolver:
    def __init__(self, deps: dict[str, list[str]]):
        self.deps = deps

    def resolve(self) -> list[str]:
        visited, visiting, order = set(), set(), []

        # include packages that only ever appear as dependencies
        all_pkgs = set(self.deps) | {d for ds in self.deps.values() for d in ds}

        def dfs(pkg):
            if pkg in visiting:
                raise ValueError(f"Cyclic dependency detected involving '{pkg}'")
            if pkg in visited:
                return
            visiting.add(pkg)
            for dep in self.deps.get(pkg, []):
                dfs(dep)
            visiting.discard(pkg)
            visited.add(pkg)
            order.append(pkg)

        for pkg in sorted(all_pkgs):
            dfs(pkg)

        return order