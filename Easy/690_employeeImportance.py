"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        sub_dict, imp_dict = dict(), dict()
        for employee in employees:
            sub_dict[employee.id] = employee.subordinates
            imp_dict[employee.id] = employee.importance
        def importanceOfEmployee(id):
            imp = imp_dict[id]
            for sub in sub_dict[id]:
                imp += importanceOfEmployee(sub)
            return imp
        return importanceOfEmployee(id)

