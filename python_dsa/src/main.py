
import logging
import time

from  xcollections import XList, XLinkedList, XStack, XQueue, XDictionary, XLDictionary

log = logging.getLogger(f"{__name__}.dsa_test")

### List example
def list_example():
    print('## List Example ##')
    xlist = XList()
    xlist.append(1)
    print(xlist.size)
    print(len(xlist))
    xlist.append(2)
    print(xlist.size)
    print(len(xlist))
    xlist.append(3)

    print(xlist.size)
    print(len(xlist))
    print(xlist)

    print(xlist.find(5))
    xlist.insert(1,5)
    print(xlist)
    print(xlist.find(5))
    del xlist[-1]
    print(xlist)

### Linked List example

def linked_list_example():
    xll = XLinkedList()
    xll.insert_head(5)
    xll.insert_head(4)
    xll.insert_head(3)
    #print(len(xll))
    xll.traverse()
    print(xll)
    xll.append(7)
    xll.append(8)
    xll.insert_head(2)
    xll.insert_after(9,6)
    print(xll)

## Stack Example ##

def stack_example():
    print('## Stack Example ##')

    xstack = XStack()
    print(xstack.is_empty())
    xstack.push(1)
    print(f"Size {xstack.size()}")
    xstack.push(2)
    print(f"Size {xstack.size()}")
    print(xstack)
    print(xstack.peek())
    print(f"Size {xstack.size()}")
    print(xstack.pop())
    print(f"Size {xstack.size()}")
    print(xstack.pop())
    print(f"Size {xstack.size()}")
    print(xstack.pop())
    print(xstack)

    s1 ="hello"

    hello_stack = XStack()

    for i in s1:
        hello_stack.push(i)

    print(hello_stack)

    res_s =""
    for i in range(hello_stack.size()):
        res_s = res_s + str(hello_stack.pop())

    print(res_s)

## Queue Examples

def queue_example():
    print('## Queue ##')
    xq = XQueue()
    xq.add(1)
    xq.add(2)
    xq.add(3)
    print(xq)
    print(xq.poll())
    print(xq.poll())
    print(xq.poll())

## Dictionary Examples

def dictionary_example():
    print('## Dictionary ##')

    dl = XDictionary(4)
    print(dl.bucket)
    print(dl.data)

    dl.put("Python",3.13)
    dl.put("java",11)
    dl.put("PHP",5)
    dl["C++"] = 27

    print(dl.bucket)
    print(dl.data)

    print(dl.get("Python"))
    print(dl.get("C"))
    print(dl["java"])

    xld = XLDictionary(3)
    xld.put("python",3.14)
    xld.put("java",11)
    xld.put("C++",27)
    xld.put("PHP",5)
    for bucket in xld.bucket:
        print(bucket)
        print(bucket.size())

    

def main():
    
    start_time = time.time()
    list_example()
    linked_list_example()
    stack_example()
    queue_example()
    dictionary_example()
    print(time.time() - start_time)
    log.warning(time.time() - start_time)

if __name__ == "__main__":
    main()


