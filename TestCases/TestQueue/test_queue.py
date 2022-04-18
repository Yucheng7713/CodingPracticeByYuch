import re
from os import listdir
from os.path import isfile, join
from DataStructure.Queue import LinkedListQueue


testDataPath = "./testdata"


def testQueueOperation():

    # Import all test data from designated directory
    data = sorted([join(testDataPath, f) for f in listdir(testDataPath) if isfile(join(testDataPath, f))])
    num_of_tests, num_of_pass = len(data), 0
    err_msg = ""

    for n in range(len(data)):
        # Read and parse test data.
        f = open(data[n], "r")
        size, ops = int(f.readline()), f.readline().split(",")
        results, output = f.readline().split(","), f.readline()

        # Validate test data' size.
        assert len(ops) == len(results), "Test data [%s] error : number of operations and results are not equal." % \
            data[n]

        q = LinkedListQueue(size)

        # Perform all queue operations specified in test data.
        for i in range(len(ops)):
            command = ops[i].strip()
            r = results[i].strip()
            if command == "front":
                if int(r) != q.front():
                    err_msg = "The front %s is not equal to expected result %s" % (str(q.front()), str(r))
                    break
            elif command == "rear":
                if int(r) != q.end():
                    err_msg = "The end \"%s\" is not equal to expected result \"%s\"" % (str(q.end()), str(r))
                    break
            elif command == "dequeue":
                if r != str(q.dequeue()):
                    err_msg = "Dequeue error"
                    break
            elif re.search("^enqueue.[0-9]+$", command):
                if r != str(q.enqueue(int(ops[i].split(".")[1]))):
                    err_msg = "Enqueue error"
                    break
            else:
                err_msg = "Test data error : Undefined queue operation."
                break
        # Validate the final queue result
        if output != q.__str__().rstrip():
            err_msg = "Unexpected output : (expected result) %s and (actual result) %s" % (output, q.__str__().rstrip())
        # Error case processing
        if err_msg:
            print("Test Run[%s/%s] %s" % (str(num_of_pass), str(num_of_tests), err_msg))
            assert False
        num_of_pass += 1

    print("Test Run[%s/%s] All tests passed" % (str(num_of_pass), str(num_of_tests)))
    assert True